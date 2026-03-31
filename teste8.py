from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


URL = "https://game-selenium.netlify.app/missao8/missao8.html"  


driver = webdriver.Chrome()
driver.get(URL)

driver.maximize_window()

time.sleep(1)


driver.find_element(By.ID, "cartao").send_keys("1234567890123456")

driver.find_element(By.ID, "senha").send_keys("1234")

driver.find_element(By.ID, "valor").send_keys("950")

select = driver.find_element(By.ID, "acao")
for option in select.find_elements(By.TAG_NAME, "option"):
    if option.get_attribute("value") == "sacar":
        option.click()
        break

driver.find_element(By.ID, "form").submit()

time.sleep(1)


driver.find_element(By.ID, "missao8").click()

time.sleep(1)

print("MISSÃO AUTOMATIZADA COM SUCESSO")