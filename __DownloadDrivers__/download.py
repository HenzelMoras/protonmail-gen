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

print(os_arch)