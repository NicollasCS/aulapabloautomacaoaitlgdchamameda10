from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://game-selenium.netlify.app/missao7/missao7.html")
time.sleep(2)

navegador.find_element(By.ID, "btnStart").click()
time.sleep(1)

for i in range(1, 11):
    id_soco = "soco" + str(i) 
    navegador.find_element(By.ID, id_soco).click()
    time.sleep(0.3) 

# 3. Finalizar a Luta (o botão deve aparecer após o soco10)
time.sleep(1)
navegador.find_element(By.ID, "btnFinalizar").click()
time.sleep(1)

navegador.find_element(By.ID, "missao7").click()
time.sleep(1)

navegador.switch_to.alert.accept()

time.sleep(5)