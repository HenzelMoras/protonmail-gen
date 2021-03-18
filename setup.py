import subprocess
import sys
from __drivers__.download import get_firefox_version, setup_firefox

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def main():

    my_packages = ['requests', 'clint', 'faker', 'selenium', 'colorama', 'random-password-generator', 'bs', 'requests']

    for package in my_packages:
        install(package)
        print('\n')
    
    print('checking whether Firefox is installed')
    firefox_ver = get_firefox_version()
    if firefox_ver != None:
        print(' firefox is installed')
        print(' proceeding to with geckodriver setup')
        setup_firefox(firefox_ver)
    else:
        print('Error - Firefox is not installed ... install firefox to proceed!')
        exit()
    print("Setup Completed")    

if __name__== '__main__':
    main()