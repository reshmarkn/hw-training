from lxml import html
import requests
import json
url = "https://www.childrensplace.com/us/p/Boys-Uniform-Short-Sleeve-Pique-Polo-5-Pack-3001296-NJ"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}

USD =' $'
Brand = 'Childrens_place'
page = requests.get(url,headers=headers)
tree = html.fromstring(page.content)
data = tree.xpath('//script[@id="__NEXT_DATA__"]/text()')
json_data = json.loads(data[0])

variants={}
colours=[]

data_list = json_data.get('props', {}).get('initialState', {}).get('ProductDetail', {}).get('currentProduct', {}).get('colorFitsSizesMap', [])
fits_list = data_list[0].get('fits', [])

for col in data_list:
    colors_name =col.get('color', {}).get('name', '')
    colours.append(colors_name)

if fits_list:
    size = []
    fits = []
    for f in fits_list:
        fit = f.get('fitName')
        fits.append(fit) if fit else ''
        if fit == 'regular':
            sizes = f.get('sizes', [])
            for s in sizes:
                s_name = s.get('sizeName')
                size.append(s_name) if s_name else ''
    
variants.update({'colours': colours})
variants.update({'FIT': fits})
variants.update({'SIZE': size})

product_name = tree.xpath("//div[@class='title-wrapper']/h1/text()")[0]
product_price = json_data.get('props', {}).get('initialState', {}).get('ProductDetail', {}).get('currentProduct', {}).get('offerPrice', '')
product_image = tree.xpath('//*[@id="overlayWrapper"]/div[2]/div/div[3]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/div/img/@src')[0]
product_description = tree.xpath("//ul[@class='sc-gsTCUz dsuMfS list-content']/li/text()")

items={
    "product_name" : product_name,
    "pdp_url" : url,
    "currency" : USD,
    "product_price" : product_price,
    "product_brand" : Brand,
    "product_image" : product_image,
    "product_description" : product_description,
    "varients":variants
}
print(items)
