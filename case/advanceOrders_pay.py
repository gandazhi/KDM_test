# _*_ coding:utf-8 _*_

"""
author：gandazhi

README:
使用前修改 最新一个订单ListView的XPath(33行 div[4])

TestCase:
最新下一个预约订单，提交订单，订单状态变为审核中  state ='审核中' if state == order_state print u'订单状态变为审核中'
"""

from selenium import webdriver
from time import sleep


mobileEmulation = {'deviceName': 'Apple iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

formal_url = 'http://www.koudaimiao.com'
test_url = 'http://test.koudaimiao.com'

# 提交预约订单中尾款进行审核
driver.get(test_url+'/group')  # 跳到个人中心
driver.add_cookie({'name': 'PHPSESSID', 'value': 'oj6lhd1bhrgm2ll2monib8eki3'})
driver.get(test_url+'/Shop/personcenter/newpersoncenter')
sleep(2)
driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[2]/ul/div[2]/div[3]/div[2]/div[4]').click()  # 进入预约订单页
sleep(3)
driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[2]/ul/div/div[23]/div[1]').click()  # 点击最新的一个ListView
sleep(2)
driver.find_element_by_xpath('//*[@id="pay"]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="ok"]').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/p[2]').click()  # 审核后点击确定按钮

# 检查最新提交的订单状态
driver.get(formal_url+'/Shop/personcenter/newpersoncenter')  # 个人中心
sleep(1)
driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[2]/ul/div[2]/div[3]/div[2]/div[4]').click()  #
sleep(1)
driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[2]/ul/div/div[23]'
                             '/div[1]/div[3]').click()  # 进入最新的ListView
state = u'审核中'
order_state = driver.find_element_by_xpath('/html/body/div[2]').text

if state == order_state:
    print u'状态成功变为审核中，到后台去审核通过该订单'
else:
    print u'状态没有变为审核通过，错误Error'