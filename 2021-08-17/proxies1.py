import requests


proxy = '103.83.118.10:53281'

try:
    r= requests.get('https://www.python.org/',proxies = {'http':proxy, 'https':proxy},timeout=3)
    print(r.status_code)
except:
    print("failed")
    pass
