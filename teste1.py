from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://game-selenium.netlify.app/missao1/missao1.html")

time.sleep(3)

btnDireita = driver.find_element(By.ID, "btnDireita")
btnBaixo = driver.find_element(By.ID, "btnBaixo")
missao1 = driver.find_element(By.ID, "missao1")

for _ in range(70):
    btnDireita.click()

for _ in range(20):
    btnBaixo.click()

missao1.click()