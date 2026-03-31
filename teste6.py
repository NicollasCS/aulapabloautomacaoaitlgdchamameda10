from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://game-selenium.netlify.app/missao6/missao6.html")
time.sleep(2)


navegador.find_element(By.ID, "btnIrCriar").click()
time.sleep(1)


navegador.find_element(By.ID, "createEmail").send_keys("usuario@teste.com")
time.sleep(0.5)
navegador.find_element(By.ID, "createSenha").send_keys("123456")
time.sleep(0.5)

navegador.find_element(By.ID, "btnRegistrar").click()
time.sleep(1)


alerta = navegador.switch_to.alert
alerta.accept()
time.sleep(1)


navegador.find_element(By.ID, "loginEmail").send_keys("usuario@teste.com")
time.sleep(0.5)
navegador.find_element(By.ID, "loginSenha").send_keys("123456")
time.sleep(0.5)

navegador.find_element(By.ID, "btnLogin").click()
time.sleep(2)


navegador.find_element(By.ID, "missao6").click()
time.sleep(1)

navegador.find_element(By.CSS_SELECTOR, "button[onclick='proxima()']").click()

time.sleep(5)