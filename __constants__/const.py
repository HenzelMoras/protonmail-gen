import sys
import subprocess
from random import choice
import time
try:
    from password_generator import PasswordGenerator
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'random-password-generator'])
try:
    from faker import Faker
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'faker'])



fake = Faker('en_US')
username = fake.name().replace(" ", fake.color_name())


pg = PasswordGenerator()
password = pg.generate()
confirm_pass = password

url = 'https://mail.protonmail.com/create/new?language=en'

domains = [
	'getnada.com', 
	'amail.club', 
	'banit.club',
	'cars2.club',
	'cmail.club',
	'banit.me',
	'duck2.club',
	'nada.email',
	'nada.ltd',
	'wmail.club'
]

email = username + '@' + choice(domains) 
service = 'https://getnada.com/api/v1/inboxes/'

