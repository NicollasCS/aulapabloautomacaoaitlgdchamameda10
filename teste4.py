from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://game-selenium.netlify.app/missao4/missao4.html")

time.sleep(2)

produtos = [
    ["001","Intel","i5-10400","CPU","1200","900","10ª geração"],
    ["002","AMD","Ryzen_5-5600","CPU","1100","850","observacao AM4"],
    ["003","NVIDIA","RTX 3060","GPU","2500","2000","observacao 12GB"],
    ["004","AMD","RX 6600","GPU","1800","1400","observacao 8GB"],
    ["005","Kingston","16 GB","RAM","300","200","observacao DDR4"],
    ["006","Corsair","32 GB","RAM","600","450","observacao DDR4"],
    ["007","Samsung","1 TB","SSD","500","350","observacao NVMe"],
    ["008","WD","500 GB","SSD","300","200","observacao SATA"],
    ["009","Corsair","600 W","Fonte","400","280","80 Plus"],
    ["010","ASUS","modelo B450","Placa-mãe","700","500","observacao AM4"]
]

for p in produtos:
    driver.find_element(By.ID, "codigo").send_keys(p[0])
    driver.find_element(By.ID, "marca").send_keys(p[1])
    driver.find_element(By.ID, "tipo").send_keys(p[2])
    driver.find_element(By.ID, "categoria").send_keys(p[3])
    driver.find_element(By.ID, "preco").send_keys(p[4])
    driver.find_element(By.ID, "custo").send_keys(p[5])
    driver.find_element(By.ID, "obs").send_keys(p[6])

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(0.2)

driver.find_element(By.ID, "missao4").click()

time.sleep(10)