# os architecture
# get platform , arch for firefox
# get firefox version
# get geckodriver url
# download geckodriver

import sys
import os
import subprocess


def os_arch():
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
    if sys.platform.startswith('linux'):
        platform = 'linux'
        architecture = os_arch()
    else:
        raise RuntimeError('could not determine geckodriver download URL for this platform.')
    return platform,architecture

def get_firefox_version():
    """
    returns the firefox `version` installed on the client
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




