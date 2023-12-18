from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome() 
driver.get("https://www.nseindia.com/option-chain")
time.sleep(1)
data = driver.find_elements(By.XPATH,('//*[@id="equity_optionChainTable"]'))
arr1 = data[0].text.split("\n")
nify_options = []
for i in arr1[22:-1]:
    nify_options.append(i.split(" "))
    
for i in nify_options:
    print(i)
driver.close()