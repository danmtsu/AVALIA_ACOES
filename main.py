from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://economia.uol.com.br/cotacoes/bolsas/')
sleep(2)
input_busca = driver.find_element(By.ID, 'filled-normal')

input_busca.send_keys('PETR3.SA')
sleep(4)
input_busca.send_keys(Keys.ENTER)

sleep(7)
span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
cotacao_PETR = span_val.text
print(f'valor petrobras = {cotacao_PETR}')

input('')