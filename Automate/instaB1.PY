#importar as biblioteca
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui as pg

 
 # passo 1 - entrar no instagram
servico = Service (ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://instagram.com/')
sleep(7)
# passo 2 - fazer login

navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('dailyofgrow ')

navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('Cannabis1533')

navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div').click()

sleep(10)

# passo 3 - clicar no agora nao

navegador.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div/div/button').click()
#//*[@id="mount_0_0_Aq"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div

print(pg.position())





# passo 4 - clicar no agora nao da notificacao

navegador.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]').click()
sleep(7)

# passo 5 - clicar na barra de pesquisa

navegador.find_element(By.XPATH,'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').click()

sleep(7)
# passo 6 - digitar por hashtag

navegador.find_element(By.XPATH,'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys('#cannabiscommunity')

# passo 7 - clicar na perfil da hastaga

navegador.find_element(By.XPATH,'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()

sleep(7)

# passo 8 - clicar na primeira foto
navegador.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()



# passo 9 - clicar no coracao
navegador.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()

# passo 10 - clicar no comentario
navegador.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button').click()



# passo 11 - digitar o comentario
navegador.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys('Nice')  

# passo 12 - clicar no botao de enviar
navegador.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()


# passo 13 - clicar no botao de proxima foto
navegador.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div/div/a').click()

# passo 14 - clicar no coracao
navegador.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()





