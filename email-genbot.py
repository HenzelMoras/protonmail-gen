from selenium import webdriver
import time
import os.path
from os import path
from __constants__.const import url

try:
    if path.exists('./webdriver/geckodriver'):
        driver = webdriver.Firefox(executable_path=r'./webdriver/geckodriver')        
    else:
        raise Exception('Driver not found .. Run Setup.py first')
except Exception as e:
    time.sleep(0.4)
    print('Error - '+ str(e))
    exit()

driver.get(url)


time.sleep(1)
