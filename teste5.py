from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://game-selenium.netlify.app/missao5/missao5.html")

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.ID, "login")))

usuarios = [
["user01","João Silva","joao@gmail.com","123456","1990-05-10","48999999999","Florianopolis","SC","admin"],
["user02","Maria Souza","maria@gmail.com","654321","1995-08-20","48988888888","Sao Jose","SC","user"],
["user03","Pedro Lima","pedro@gmail.com","111111","1988-02-15","48977777777","Palhoca","SC","suporte"],
["user04","Ana Costa","ana@gmail.com","222222","1992-11-30","48966666666","Biguacu","SC","teste"],
["user05","Lucas Rocha","lucas@gmail.com","333333","2000-01-01","48955555555","Curitiba","PR","dev"]
]

for u in usuarios:
    driver.execute_script("""
    document.getElementById('login').value = arguments[0];
    document.getElementById('nome').value = arguments[1];
    document.getElementById('email').value = arguments[2];
    document.getElementById('senha').value = arguments[3];
    document.getElementById('dataNascimento').value = arguments[4];
    document.getElementById('telefone').value = arguments[5];
    document.getElementById('cidade').value = arguments[6];
    document.getElementById('estado').value = arguments[7];
    document.getElementById('obs').value = arguments[8];
    """, *u)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(0.5)


wait.until(EC.element_to_be_clickable((By.ID, "missao5"))).click()

time.sleep(10)