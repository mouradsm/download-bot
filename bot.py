import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Configurações
URL = "https://class.devsamurai.com.br/"  # Substitua pelo URL do site com a lista de arquivos
PASTA_DESTINO = "downloads"  # Nome da pasta onde os arquivos serão salvos

# Cria a pasta destino, se não existir
os.makedirs(PASTA_DESTINO, exist_ok=True)

def baixar_arquivo(url, caminho_destino):
    """Baixa um arquivo do URL especificado e o salva no caminho fornecido, com barra de progresso."""
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        tamanho_total = int(resposta.headers.get('content-length', 0))
        with open(caminho_destino, 'wb') as arquivo, tqdm(
            total=tamanho_total,
            unit='B',
            unit_scale=True,
            desc=os.path.basename(caminho_destino),
            ncols=80
        ) as barra:
            for chunk in resposta.iter_content(chunk_size=1024):
                arquivo.write(chunk)
                barra.update(len(chunk))
    else:
        print(f"Erro ao baixar {url}: {resposta.status_code}")

def encontrar_links(url):
    """Encontra todos os links dentro de uma estrutura <ul><li><a>."""
    resposta = requests.get(url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        # Encontra todos os links dentro de <ul><li>
        return [link.get('href') for link in soup.select('ul li a[href]')]
    else:
        print(f"Erro ao acessar {url}: {resposta.status_code}")
        return []

def baixar_arquivos_da_pagina(url, pasta_destino):
    """Encontra e baixa arquivos de uma página da web."""
    links = encontrar_links(url)
    total_arquivos = len(links)
    if total_arquivos == 0:
        print("Nenhum arquivo encontrado para download.")
        return

    print(f"Total de arquivos encontrados: {total_arquivos}\n")
    
    for i, link in enumerate(links, start=1):
        # Verifica se o link é relativo ou absoluto
        arquivo_url = link if link.startswith('http') else f"{url}/{link}"
        nome_arquivo = os.path.basename(link)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        print(f"Baixando arquivo {i} de {total_arquivos}: {nome_arquivo}")
        baixar_arquivo(arquivo_url, caminho_destino)

# Inicia o processo
baixar_arquivos_da_pagina(URL, PASTA_DESTINO)
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Configurações
URL = "https://seusite.com/arquivos"  # Substitua pelo URL do site com a lista de arquivos
PASTA_DESTINO = "downloads"  # Nome da pasta onde os arquivos serão salvos

# Cria a pasta destino, se não existir
os.makedirs(PASTA_DESTINO, exist_ok=True)

def baixar_arquivo(url, caminho_destino):
    """Baixa um arquivo do URL especificado e o salva no caminho fornecido, com barra de progresso."""
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        tamanho_total = int(resposta.headers.get('content-length', 0))
        with open(caminho_destino, 'wb') as arquivo, tqdm(
            total=tamanho_total,
            unit='B',
            unit_scale=True,
            desc=os.path.basename(caminho_destino),
            ncols=80
        ) as barra:
            for chunk in resposta.iter_content(chunk_size=1024):
                arquivo.write(chunk)
                barra.update(len(chunk))
    else:
        print(f"Erro ao baixar {url}: {resposta.status_code}")

def encontrar_links(url):
    """Encontra todos os links dentro de uma estrutura <ul><li><a>."""
    resposta = requests.get(url)
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        # Encontra todos os links dentro de <ul><li>
        return [link.get('href') for link in soup.select('ul li a[href]')]
    else:
        print(f"Erro ao acessar {url}: {resposta.status_code}")
        return []

def baixar_arquivos_da_pagina(url, pasta_destino):
    """Encontra e baixa arquivos de uma página da web."""
    links = encontrar_links(url)
    total_arquivos = len(links)
    if total_arquivos == 0:
        print("Nenhum arquivo encontrado para download.")
        return

    print(f"Total de arquivos encontrados: {total_arquivos}\n")
    
    for i, link in enumerate(links, start=1):
        # Verifica se o link é relativo ou absoluto
        arquivo_url = link if link.startswith('http') else f"{url}/{link}"
        nome_arquivo = os.path.basename(link)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        print(f"Baixando arquivo {i} de {total_arquivos}: {nome_arquivo}")
        baixar_arquivo(arquivo_url, caminho_destino)

# Inicia o processo
baixar_arquivos_da_pagina(URL, PASTA_DESTINO)
