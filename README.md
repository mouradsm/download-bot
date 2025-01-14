# Download Automático de Arquivos

Este é um script em Python que permite baixar automaticamente arquivos listados em uma página HTML. O script encontra links dentro de uma estrutura `<ul><li>` e faz o download dos arquivos, exibindo uma barra de progresso para cada arquivo.

## Requisitos

1. Python 3.7 ou superior.
2. Bibliotecas Python:
   - `requests`
   - `beautifulsoup4`
   - `tqdm`

### Instalação das Dependências

Use o pip para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

## Configuração

1. Abra o arquivo do script.
2. Substitua o valor da variável `URL` pelo link da página que contém os arquivos.
3. Altere o valor da variável `PASTA_DESTINO` para a pasta onde os arquivos serão salvos. O padrão é `downloads`.

## Uso

1. Execute o script no terminal ou prompt de comando:

```bash
python script_download.py
```

2. O script irá:
   - Acessar a página especificada em `URL`.
   - Encontrar todos os links dentro de uma estrutura `<ul><li><a>`.
   - Exibir o total de arquivos encontrados.
   - Baixar os arquivos um por um, mostrando uma barra de progresso para cada arquivo.

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

