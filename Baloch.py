import os, platform

try:

    import requests

except:

    os.system('pip install requests')

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    import p_Fixed_Fixed

    

elif bit == '32bit':

    import Sarfraz32
