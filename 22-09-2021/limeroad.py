import cloudscraper
from lxml import html
import json
url = 'https://www.limeroad.com/blue-rayon-jaipur-fashion-mode-p17635640?imgIdx=3&src_id=navdeskEthnicSets__002'
scraper = cloudscraper.create_scraper()
# print(scraper.get(url))

def parse_data(url):
    page = scraper.get(url)
    tree = html.fromstring(page.content)


    # XPATH
    product_id = tree.xpath("//div[@class='dIb vT c6']/text()")
    product_name = tree.xpath('//h1/text()')    
    product_price = tree.xpath("//span[@class='sell']/text()")
    product_discount = tree.xpath("//span[@class='per']/text()")
    product_mrp = tree.xpath("//span[@class='mrp']/text()")
    average_rating = tree.xpath("//div[@class='c6 fs12 p40 taL ttC dT']/div[1]/text()")
    category_hierarchy = tree.xpath("//ul[@itemtype='http://schema.org/BreadcrumbList']/li/a /span/text()")

    items = {}
    items['product_id'] = product_id
    items['product_name'] = product_name
    items['product_price'] =  product_price
    items['product_discount'] =  product_discount   
    items['product_mrp'] = product_mrp    
    items['average_rating'] = average_rating
    items['category_hierarchy'] =category_hierarchy
    print(items)

parse_data(url)
