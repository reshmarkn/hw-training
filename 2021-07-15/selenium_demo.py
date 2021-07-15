from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Btech Vazha 2.0')

searchButton=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()