from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# abre o navegador
driver = webdriver.Chrome()

# entra no site
driver.get("https://game-selenium.netlify.app/missao3/missao3.html")

time.sleep(3)  # espera carregar (simples)


btnEsq = driver.find_element(By.ID, "esq")
btnCima = driver.find_element(By.ID, "cima")
missao3 = driver.find_element(By.ID, "missao3")

for i in range(23):
    btnEsq.click()
for i in range(7):
    btnCima.click()
for i in range(100):
    btnEsq.click()
missao3.click()
    