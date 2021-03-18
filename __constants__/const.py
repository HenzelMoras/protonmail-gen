import sys
import subprocess
from random import choice
import time
import requests
import random
import os.path
from os import path
try:
    from password_generator import PasswordGenerator
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'random-password-generator'])
try:
    from faker import Faker
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'faker'])
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.headless = False
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument('--log-level=3')

try:
    if path.exists('./webdriver/geckodriver'):
        driver = webdriver.Firefox(options = options, executable_path=r'./webdriver/geckodriver')          
    else:
        raise Exception('Driver not found .. Run Setup.py first')
except Exception as e:
    time.sleep(0.4)
    print('Error - '+ str(e))
    exit()

fake = Faker('en_US')
username = fake.name().replace(" ", "") + fake.year()[:2]


pg = PasswordGenerator()
password = pg.generate()
confirm_pass = password

url = 'https://mail.protonmail.com/create/new?language=en'


api = 'https://getnada.com/api/v1/'


domains = requests.get(f'{api}/domains').json()
domain_list = []
for i in domains:
    for k,v in i.items():
        if 'name' in k:
            domain_list.append(v) 

email = username[:6].lower() + fake.year()[:2]  + '@' + random.choice(domain_list)

