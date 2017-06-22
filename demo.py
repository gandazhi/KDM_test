# -*- coding: utf-8 -*-
from selenium import webdriver


formal_url = 'http://www.koudaimiao.com'
test_url = 'http://test.koudaimiao.com'

mobileEmulation = {'deviceName': 'Apple iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

