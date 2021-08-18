url='https://www.python.org/'
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
#               '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept - encoding': 'gzip, deflate, br',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/91.0.4472.101 Safari/537.36 '
#   }
import requests
import random
PROXY_LIST = requests.get("http://68.183.58.145/torproxies", headers={"x-api-key": "_/&IWn<rJ5hDTdq"}).json()
PROXY = random.choice(PROXY_LIST)
proxies = {"http": "http://%s" % PROXY, "https": "https://%s" % PROXY}
response = requests.get(url,proxies=proxies, timeout=5)
print(proxies)
print(response)