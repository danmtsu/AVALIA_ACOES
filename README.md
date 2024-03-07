# Coleta de Dados de Cotação de Empresas

Este script Python utiliza Selenium para coletar dados de cotação de empresas financeiras do site economia.uol.com.br. Ele faz isso de forma automatizada para as empresas fornecidas na lista `companys`.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- Selenium
- Pandas
- Webdriver Manager
- ChromeDriver (automagicamente gerenciado pelo Webdriver Manager)

Você pode instalar as dependências executando:

pip install -r requirements.txt


## Utilização

1. Edite a lista `companys` com os códigos de empresas que deseja obter as cotações.
2. Execute o script `main.py`.
3. Os dados serão coletados e salvos em um arquivo Excel com o nome especificado.

## Notas

- Este script foi projetado para ser executado em segundo plano (headless) usando o navegador Chrome.
- Certifique-se de ter uma conexão com a internet ao executar o script, pois ele acessa informações online.
- Os dados coletados incluem o valor da cotação e a hora da coleta.
