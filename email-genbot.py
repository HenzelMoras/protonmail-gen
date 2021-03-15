from selenium import webdriver
import time
import os.path
from os import path
from __constants__.const import url,username,password,confirm_pass
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

# switch drivers context to iframe and fill username
WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
        (By.TAG_NAME, 'iframe')))
time.sleep(.5)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, 'username'))).click
time.sleep(2)

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, 'username'))).send_keys(username)

time.sleep(.5)

# switch to default context and fill password
driver.switch_to.default_content()

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, 'password'))).click

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, 'password'))).send_keys(password)
time.sleep(1)

# confirm_pass
WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, 'passwordc'))).click

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, 'passwordc'))).send_keys(confirm_pass)
time.sleep(1)

# create account
driver.switch_to.frame(driver.find_element_by_class_name("bottom"))

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div/div/footer/button')))

driver.find_element_by_xpath('/html/body/div/div/footer/button').click()


# confirm creation 
driver.switch_to.default_content()

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="confirmModalBtn"]')))

driver.find_element_by_xpath('//*[@id="confirmModalBtn"]').click()   


# Email verification 

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="id-signup-radio-email"]')))

driver.find_element_by_xpath('//*[@id="id-signup-radio-email"]').click()

