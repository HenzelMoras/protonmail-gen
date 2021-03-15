# os architecture
# get platform , arch for firefox
# get firefox version
# get geckodriver url
# download geckodriver

import sys
import os
import subprocess
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
finally:
    import requests
import urllib, time
from io import BytesIO
import tarfile
try:
    from clint.textui import progress
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'clint'])
finally:
    from clint.textui import progress


def os_arch():
    """
    :returns: 'os_arch' of the linux client
    """
    os_arch = '32'
    output = subprocess.check_output(['uname', '-m'])
    if type(output) != str:
        output = output.decode('utf-8')
    if 'x86_64' in output:
        os_arch = '64'
    else:
        os_arch = '32'
    return os_arch

def get_platform_arch_firefox():
    """
    :returns: 'platform' and 'architecture' of the linux client
    """ 
    if sys.platform.startswith('linux'):
        platform = 'linux'
        architecture = os_arch()
    else:
        raise RuntimeError('could not determine geckodriver download URL for this platform.')
    return platform,architecture

def get_firefox_version():
    """
    returns the firefox 'version' installed on the client
    """
    platform, _ = get_platform_arch_firefox()
    if platform == 'linux':
        try:
            with subprocess.Popen(['firefox', '--version'], stdout=subprocess.PIPE) as proc:
                version = proc.stdout.read().decode('utf-8').replace('Mozilla Firefox', '').strip()
        except:
            return None
    else:
        return
    return version

def get_latest_geckodriver_version():
    """
    :return: the 'latest version' of geckodriver to be concatenated with the download url
    """
    url = requests.get('https://github.com/mozilla/geckodriver/releases/latest').url
    if '/tag/' not in url:
        return
    return url.split('/')[-1]

def get_download_url_firefox(version):
    """
    :returns: 'download url' for geckodriver
    """
    platform, architecture = get_platform_arch_firefox()

    return 'https://github.com/mozilla/geckodriver/releases/download/' + version + '/geckodriver-' + version + '-' + platform + architecture + '.tar.gz'

def download_tar_file(url,save_path):
    """
    :returns: downloads the tar file from 'url' and extracts to 'save_path'
    """
    print('Downloading...')

    response = requests.get(url)

    total_length = sum(len(chunk) for chunk in response.iter_content(8196))

    if total_length is None or total_length == 0:
        print('Download Failed')
        exit()

    with tarfile.open(fileobj=BytesIO(response.content), mode='r|gz') as my_tar_file:
        for _chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            pass
        print('Download Successful')
        my_tar_file.extractall(save_path)

def setup_firefox(firefox_ver):
    """
    :returns: downloads webdriver and saves it in ./webdriver
    """

    if firefox_ver != None:
        print('Installed version - ' + str(firefox_ver))
        latest_driver = get_latest_geckodriver_version()
        print('Latest geckodriver version - ' + latest_driver)
        download_link = get_download_url_firefox(latest_driver)
        download_tar_file(download_link, './webdriver')
    else:
        print('Firefox is not installed')
    