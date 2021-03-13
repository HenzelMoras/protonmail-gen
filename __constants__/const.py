import sys
import subprocess
try:
    from password_generator import PasswordGenerator
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'random-password-generator'])
try:
    from faker import Faker
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'faker'])

fake = Faker('en_US')
username = fake.name().replace(" ", "")

pg = PasswordGenerator()
password = pg.generate()

url = 'https://protonmail.com/'




