# Download Automático de Arquivos

Este é um script em Python que permite baixar automaticamente arquivos listados em uma página HTML. O script encontra links dentro de uma estrutura `<ul><li>` e faz o download dos arquivos, exibindo uma barra de progresso para cada arquivo.

## Requisitos

1. Python 3.7 ou superior.
2. Bibliotecas Python:
   - `requests`
   - `beautifulsoup4`
   - `tqdm`

### Instalação das Dependências

Crie um virtual env para separar as bibliotecas que serão instaladas no projeto (opcional):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Use o pip para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## Uso

1. Execute o script no terminal ou prompt de comando, fornecendo a URL e a pasta de destino como argumentos:

```bash
python bot.py <URL> --destination <PASTA_DESTINO>
```

   - Substitua `<URL>` pelo link da página que contém os arquivos.
   - Substitua `<PASTA_DESTINO>` pela pasta onde os arquivos serão salvos (opcional, o padrão é `downloads`).

2. O script irá:
   - Acessar a página especificada na URL fornecida.
   - Encontrar todos os links dentro de uma estrutura `<ul><li><a>`.
   - Exibir o total de arquivos encontrados.
   - Baixar os arquivos um por um, mostrando uma barra de progresso para cada arquivo.

### Exemplo de Uso

Para baixar arquivos do site `https://example.com/files` para a pasta `meus_downloads`:

```bash
python bot.py https://class.devsamurai.com.br/ --destination meus_downloads
```

Se você quiser usar a pasta de destino padrão (`downloads`):

```bash
python bot.py https://class.devsamurai.com.br/
```

### Exemplo de Saída

```plaintext
Total de arquivos encontrados: 5

Baixando arquivo 1 de 5: arquivo1.pdf
arquivo1.pdf:  34%|█████▍                 | 120k/350k [00:01<00:02, 102kB/s]
Baixando arquivo 2 de 5: arquivo2.zip
arquivo2.zip: 100%|███████████████████████| 5.00M/5.00M [00:02<00:00, 2.2MB/s]
```

## Personalização

- **Filtros de Links**: Caso os arquivos tenham uma extensão específica (ex.: `.pdf`, `.zip`), você pode ajustar o seletor no método `encontrar_links`:

```python
return [link.get('href') for link in soup.select('ul li a[href]') if link.get('href').endswith('.pdf')]
```

- **Estrutura HTML Específica**: Caso a `<ul>` tenha uma classe ou ID específico, ajuste o seletor:

```python
soup.select('ul.classe-especifica li a[href]')
```

## Observações

- Certifique-se de que você tem permissão para baixar os arquivos do site especificado.
- Links relativos serão automaticamente convertidos para absolutos com base na URL fornecida.
- Caso o site utilize autenticação, pode ser necessário incluir cabeçalhos HTTP ou cookies no script.

## Suporte

Se você tiver problemas ou perguntas, entre em contato ou abra uma solicitação de ajuda. Ficarei feliz em ajudar!
