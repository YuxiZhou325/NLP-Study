'''
This is a script for Yilin to save some effort during her internship
Hope it helps :)
'''

import selenium

# Using Chrome to access web
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.bilibili.com')  # change the url to the webpage you need

# Select the id box
id_box = driver.find_element_by_name('sub_item')

# Send id information
id_box.send_keys('sub_item')