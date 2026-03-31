from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://game-selenium.netlify.app/missao5/missao5.html")

time.sleep(2)

usuarios = [
["user01","Joao Silva","joao@gmail.com","123456","1990-05-10","48999999999","Florianopolis","SC","admin"],
["user02","Maria Souza","maria@gmail.com","654321","1995-08-20","48988888888","Sao Jose","SC","user"],
["user03","Pedro Lima","pedro@gmail.com","111111","1988-02-15","48977777777","Palhoca","SC","suporte"],
["user04","Ana Costa","ana@gmail.com","222222","1992-11-30","48966666666","Biguacu","SC","teste"],
["user05","Lucas Rocha","lucas@gmail.com","333333","2000-01-01","48955555555","Curitiba","PR","dev"]
]

for u in usuarios:
    driver.find_element(By.ID, "login").send_keys(u[0])
    driver.find_element(By.ID, "nome").send_keys(u[1])
    driver.find_element(By.ID, "email").send_keys(u[2])
    driver.find_element(By.ID, "senha").send_keys(u[3])

    # 💥 CORREÇÃO DA DATA
    driver.execute_script(
        "document.getElementById('dataNascimento').value = arguments[0];",
        u[4]
    )

    driver.find_element(By.ID, "telefone").send_keys(u[5])
    driver.find_element(By.ID, "cidade").send_keys(u[6])
    driver.find_element(By.ID, "estado").send_keys(u[7])
    driver.find_element(By.ID, "obs").send_keys(u[8])

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(1)

driver.find_element(By.ID, "missao5").click()

time.sleep(10)