import os
import requests
import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm


def baixar_arquivo(url, destination_path):
    """Downloads a file from the specified URL and saves it to the path provided, with progress bar."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_file_size = int(response.headers.get("content-length", 0))
        with open(destination_path, "wb") as arquivo, tqdm(
            total=total_file_size,
            unit="B",
            unit_scale=True,
            desc=os.path.basename(destination_path),
            ncols=80,
        ) as bar:
            for chunk in response.iter_content(chunk_size=1024):
                arquivo.write(chunk)
                bar.update(len(chunk))
    else:
        print(f"Error downloading {url}: {response.status_code}")


def extract_links_from_ul(url):
    """Finds all links within a structure <ul><li><a>."""
    resposta = requests.get(url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, "html.parser")

        return [link.get("href") for link in soup.select("ul li a[href]")]
    else:
        print(f"Erro ao acessar {url}: {resposta.status_code}")
        return []


def download_files_from_page(url, destination_folder):
    """Finds and downloads files from a web page."""
    links = extract_links_from_ul(url)
    file_count = len(links)
    if file_count == 0:
        print("No files found for download.")
        return

    print(f"Total files found: {file_count}\n")

    for i, link in enumerate(links, start=1):
        file_url = link if link.startswith("http") else f"{url}/{link}"
        file_name = os.path.basename(link)
        destination_path = os.path.join(destination_folder, file_name)
        print(f"Downloading files {i} de {file_count}: {file_name}")
        baixar_arquivo(file_url, destination_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download files from a given URL.")
    parser.add_argument("url", help="The URL to download files from.")
    parser.add_argument(
        "--destination",
        default="downloads",
        help="The destination folder to save files to.",
    )
    args = parser.parse_args()
    os.makedirs(args.destination, exist_ok=True)
    download_files_from_page(args.url, args.destination)
