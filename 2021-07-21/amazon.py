from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from lxml import html

class Amazon():

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get("http://www.amazon.in")
        self.driver.maximize_window()
        sleep(1)

        self.start()

    def start(self):

        searchbox = self.driver.find_element_by_xpath('//input[@type="text"]')
        searchbox.send_keys('Mobiles')
        searchButton = self.driver.find_element_by_xpath('//input[@id="nav-search-submit-button"]')
        searchButton.click()
        drop = self.driver.find_element_by_xpath("//a[@aria-label='See more, Brand']")
        drop.click()  

        try:
            Apple = self.driver.find_element_by_xpath('//li[@aria-label="Apple"]/span/a')
            Apple.click()
        except NoSuchElementException:
                print("Element does not exist")
        
        sleep(2)

        sort_by = Select(self.driver.find_element_by_xpath("//select[@class='a-native-dropdown a-declarative']"))
        sort_by.select_by_visible_text("Price: Low to High")

        sleep(5)
        
        self.parse_product()

    def parse_product(self):
        
        item={}

        tree = html.fromstring(self.driver.page_source)
        for info in tree.xpath('//div[contains(@data-component-type ,"s-search-result")]'):
            product_name = info.xpath('div//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
            product_price = info.xpath('div//span[@class="a-offscreen"]/text()')
            item["product_name"] = product_name
            item["product_price"] = product_price
            print(item)  
        
        try:
            pagination_links = self.driver.find_element_by_xpath('//li[contains(@class , "a-last")]/a')
            pagination_links.click()
            sleep(5)
            self.parse_product()

        except NoSuchElementException:
            self.driver.close()

obj=Amazon()
