from selenium import webdriver
import time

from datetime import datetime
from __constants__.const import url, username, password, confirm_pass, email, api, options,driver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup as bs
from __functions__.functions import inject_input, scroll_click_element, switch_frame, click_element

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
click_element(driver, '//*[@id="confirmModalBtn"]')

# check bot abuse 
try:
        click_element(driver, '//*[@id="verification-panel"]/div[3]/label/div')
        click_element(driver, '//*[@id="verification-panel"]/div[2]/label/div')
except:
        print("Looks like YOU have abused the bot!! Try Again later")
        input("Press enter/return key to exit.")
        driver.close()

# fill email 
scroll_click_element(driver, '//*[@id="emailVerification"]')
inject_input(driver, email ,xpath='//*[@id="emailVerification"]')
scroll_click_element(driver, '//*[@id="verification-panel"]/form[1]/div[1]/div[2]/button')

# get verification code from disposable mail
while True:
        try:
            uid = requests.get(f"{api}inboxes/{email}").json()
            uid = uid["msgs"][0]["uid"]
            print('uid: ',uid)
            break
        except:
            time.sleep(1)
            pass
html = requests.get(f"{api}messages/html/{uid}").content
soup = bs(html,"html5lib")
code = soup.find("code").text
    
scroll_click_element(driver, '//*[@id="codeValue"]')
inject_input(driver, code, css_selector='input[type = "text"]')

scroll_click_element(driver, '//*[@id="verification-panel"]/p[3]/button') # Complete setup btn
time.sleep(1)

scroll_click_element(driver, '//*[@id="confirmModalBtn"]')

for _ in range(0, 3): 
        scroll_click_element(driver, '//*[@id="pm_wizard"]/div/div[5]/button[1]')
        time.sleep(.5)
        scroll_click_element(driver, '//*[@id="pm_wizard"]/div/div[5]/button[2]')

print("\nAccount Details.\n")

username = "Username: " + username
password = "Password: " + password
with open("Accounts.txt", 'a') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M")+"\n")
        f.write(username+"\n")
        f.write(password+"\n")
        f.write("-------------------------------\n")
print(username)
print(password)
