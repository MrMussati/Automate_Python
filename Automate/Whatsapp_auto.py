#importar as biblioteca
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

 
 # navegar ate o whatsapp web
servico = Service (ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
driver.get('https://web.whatsapp.com/')

while len(driver.find_elements(By.ID,'side')) < 1:
    sleep(1)


#defineir contato ou grupo
contatos = ['Bruno M Mussati' ]
mensagem = 'Ola, eu sou um bot'
 #buscar contattos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
    sleep (3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

    sleep(5)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    campo_mensagem.click()
    sleep(2)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)

    sleep(5)
    

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

    #campo de pesquisa copyable-text selectable-text"
    #campo para mensagem privada copyable-text selectable-text

