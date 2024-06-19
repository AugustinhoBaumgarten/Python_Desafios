from sys import displayhook
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


contatos_df = pd.read_excel("Enviar.xlsx")
displayhook(contatos_df)


navegador = webdriver.Chrome(executable_path='./chrome.exe')
navegador.get("https://www.whatsapp.com/?lang=pt_br")