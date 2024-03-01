from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
from time import sleep


def get_data():
    

    options = Options()
    options.add_argument('--headless')
    companys = ['PETR3.SA','MGLU3.SA','VIVT3.SA']
    valores = list()
    data_hora = list()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://economia.uol.com.br/cotacoes/bolsas/')

    for company in companys:
        sleep(2)
        input_busca = driver.find_element(By.ID, 'filled-normal')

        input_busca.send_keys(company)
        sleep(4)
        input_busca.send_keys(Keys.ENTER)

        sleep(7)
        span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
        cotacao_company = span_val.text
        valores.append(cotacao_company)
        data_hora.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print(f'valor {company} = {cotacao_company}')

    dados = {
        'company': companys,
        'value': valores ,
        'time_hour': data_hora
    }
    return dados

def convert_to_excel(dados: dict, file_name:str):
    df_companys = pd.DataFrame(dados)
    df_companys.to_excel(f'./{file_name}.xlsx')


data_company = get_data()
convert_to_excel(data_company,"company")
