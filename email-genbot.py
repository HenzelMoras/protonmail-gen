from selenium import webdriver
import time
import os.path
from os import path
from datetime import datetime
from __constants__.const import url, username, password, confirm_pass, email, service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup as bs
from __functions__.functions import inject_input, scroll_click_element, switch_frame, click_element

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
switch_frame(driver, tag_name='iframe')

inject_input(driver, username, id='username')


# switch to default context and fill password
driver.switch_to.default_content()

inject_input(driver, password, id='password')

# confirm_pass
inject_input(driver, confirm_pass, id='passwordc')



# create account
switch_frame(driver, class_name="bottom")

# move the page before confirming
scroll_click_element(driver, '/html/body/div/div/footer/button')


# confirm creation 
driver.switch_to.default_content()

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="confirmModalBtn"]')))

driver.find_element_by_xpath('//*[@id="confirmModalBtn"]').click()   


# Email verification selection
click_element(driver, '//*[@id="id-signup-radio-email"]')

"""
# fill email 
email_verification = '//*[@id="emailVerification"]'

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, email_verification)))

driver.find_element_by_xpath(email_verification).send_keys(email)


click_send_box = '/html/body/div[2]/div/div/div/form/div/div/form[1]/div[1]/div[2]/button'


# send the email for verification
driver.find_element_by_xpath(click_send_box).click()

# check tem-mail box and retrive code
while True:
    try:
        uid = requests.get(f"https://getnada.com/api/v1/inboxes/{email}").json()
        uid = uid["msgs"][0]["uid"]
        print(uid)
        break
    except:
        time.sleep(1)
        pass

html = requests.get(f"https://getnada.com/api/v1/messages/html/{uid}").content
soup = bs(html,"html5lib")
code = soup.find("code").text
print(code)

# submit verification
verification_code = '//*[@id="codeValue"]'

WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, verification_code)))

driver.find_element_by_xpath(verification_code).send_keys('123')
"""
# complete setup

complete_Setup = '/html/body/div[2]/div/div/div/form/div/div/p[3]/button'

code_input = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type = "text"]')))
for i in code_input:
        code_input.send_keys(i)
        time.sleep(.1)


print(' \nsaving account details\n')
with open('account.txt', 'a') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M")+"\n")
        f.write(username+"\n")
        f.write(password+"\n")
        f.write("-------------------------------\n")
print(username)
print(password)
