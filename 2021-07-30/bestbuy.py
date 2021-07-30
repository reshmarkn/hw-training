from lxml import html

import requests

import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('best_buy.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logging.basicConfig(filename='best_buy.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}


url = 'https://www.bestbuy.com/site/apple-watch-series-3-gps-38mm-silver-aluminum-case-with-white-sport-band-silver-aluminum/5706617.p?skuId=5706617&intl=nosplash'
page = requests.get(url, headers=headers)
tree = html.fromstring(page.content)

product_name = tree.xpath('//h1[@class="heading-5 v-fw-regular"]/text()')[0]
product_brand = tree.xpath('//a[@data-track="Product_Title_Brand_Apple"]/text()')[0]
model = tree.xpath('//span[@class="product-data-value body-copy"]/text()')[0]
sku = tree.xpath('//div[@class="sku product-data"]/span[2]/text()')[0]
price = tree.xpath('//div[@class="priceView-hero-price priceView-customer-price"]/span/text()')[0]
image_url = tree.xpath('//button[@class="primary-button"]/img/@src')[0]
description = tree.xpath("//div[@class='product-description']/text()")[0]
features = tree.xpath("//div[@class='list-row']/p/text()")
rating = tree.xpath("//span[@class='ugc-c-review-average']/text()")[0]
reviews = tree.xpath("//span[@class='c-reviews-v4 ugc-review-container']/text()")[0]
percentage = tree.xpath("//span[@class='recommendPercent']/text()")[0]

rows = tree.xpath('//div[@class="category-wrapper row"]/div//li')
specifications = {}
for row in rows:
    keys = row.xpath('div//div[@class="row-title"]//text()')
    keys = ''.join(keys) if keys else ''
    values = row.xpath("div[@class='row-value col-xs-6 v-fw-regular']//text()")
    values = ''.join(values) if values else ''
    specifications.update({keys: values})

#CLEAN
price = ''.join(price).replace('$','') if price else ''

item={
'product_name' : product_name,
'product_brand' : product_brand,
'product_model' : model,
'sku' : sku,
'product_price' : price,
'image_url' : image_url,
'description' : description,
'features' : features,     
'rating' : rating,
'reviews' : reviews,
'percentage' : percentage,
'specification' : specifications
}
logger.info(item)
