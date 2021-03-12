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

