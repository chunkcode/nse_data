from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
driver.get("https://www.nseindia.com/market-data/live-equity-market")
time.sleep(1)
data = driver.find_elements(By.XPATH,('//*[@id="tableLiveMarket-equity-stock"]'))
arr1 = data[0].text.split("\n")
arr2 = data[0].text.split("\n")[20:]
i = 0
values = []
while i < len(arr2):
    if len(arr2[i].split(" ")) > 12:
        values.append(arr2[i].split(" "))
        i = i+1
    else:
        values.append(arr2[i].split(" ")+arr2[i+1].split(" "))
        i = i+2
for val in values: 
 print(val)
