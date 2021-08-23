from lxml import html
import requests
url ='https://www.amazon.com/b?node=10509644011&ref=sr_nr_n_1'
base_url = 'https://www.amazon.com/'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
def parse_data(url):
    page = requests.get(url,headers=headers)
    tree = html.fromstring(page.content)
    price_list = tree.xpath('//div[@id="priceRefinements"]/ul[1]/li/span/a/@href')

    print(price_list)
parse_data(url)