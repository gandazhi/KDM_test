# -*- coding: utf-8 -*-
"""
author：gandazhi
已知问题：模拟打开浏览器时，有概率出现一直加载网页的情况  添加cookie绕过登录

README
下单商城首页第一个商品
使用之前记得修改 商品定金：money（46行）  商品总价commodity_piece（55行）  预约时间time(格式00yyyy/mm/dd 66行)   最新下的订单ListView的XPath(90行最后[15])

TestCase:
下商城首页订单  检查商城首页ListView 上的定金 --> 进入商品详情页 查看商品定金  if money == piece:  print 定金正确
检查尾款： 尾款 + 定金 == 总价 if retainage + piece = 商品总价:  print 尾款正确
下单后检查使用的喵币，下单的时候，记录喵币保存到coin中，下单后跳转到个人中心，记录喵币数量保存到coin_now
使用的喵币为：coin - coin_now
喵币比例为1:100
检查喵币抵扣是否正确：if float（expend_coin / 100) == retainage: print 使用喵币抵扣金额正确
检查商品首页上的定金价格与订单中的定金价格是否一致
检查额度是否减少
"""
from selenium import webdriver
from time import sleep


mobileEmulation = {'deviceName': 'Apple iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

formal_url = 'http://www.koudaimiao.com'  # 正式服url
test_url = 'http://test.koudaimiao.com'  # 测试服url

driver.get(test_url+'/group')  # 进入首页
sleep(3)
driver.find_element_by_class_name('getit').click()  # 点击知道了
driver.add_cookie({'name': 'PHPSESSID', 'value': 'oj6lhd1bhrgm2ll2monib8eki3'})  # 通过cookie绕过登录
sleep(3)
driver.get(test_url+'/Shop/personcenter/newpersoncenter')  # 进入个人中心
sleep(3)
before_limit = driver.find_element_by_xpath('//*[@id="myTargetElement"]').text
before_limit = str(before_limit).replace(',', '')
print u'之前的额度', before_limit

driver.find_element_by_class_name('index_bottom_mune_rect').click()  # 进入首页
sleep(2)
driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[2]/ul/div[10]/div[1]/div[1]').click()
sleep(2)

# 判断商品ListView上的定金和商品详细页上的定金是否相同
piece = driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[1]/ul/div[3]/div[1]/span[1]/b').text
print piece
money = u'9.80'
if money == piece:
    print u'定金价格正确'
else:
    print u'定金价格不正确'

# 尾款+定金是否等于总价格 判断尾款是否正确
retainage = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[2]/span').text
print retainage
commodity_piece = 98.0
if (float(piece) + float(retainage)) == commodity_piece:
    print u'尾款正确'
else:
    print u'尾款错误'

# 测试下单逻辑
driver.find_element_by_xpath('/html/body/div[3]/div[2]').click()  # 点击立即下单
sleep(1)
driver.find_element_by_xpath('//*[@id="zhifu"]').click()  # 点确认订单
sleep(1)
time = '002017/0606'
driver.find_element_by_id('time').send_keys(time)  # 输入预约时间

coin = driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[1]/ul/div[4]/div/span/span').text
print u'现有喵币：', coin

sleep(1)
driver.find_element_by_id('payfor').click()  # 确认下订单
sleep(1)

driver.get(test_url+'/Shop/personcenter/newpersoncenter')  # 跳转到个人中心
sleep(1)
coin_now = driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[2]/ul/div[2]/div[3]/div[6]/div/span[2]').text
after_limit = driver.find_element_by_xpath('//*[@id="myTargetElement"]').text
after_limit = str(after_limit).replace(',', '')
print u'购买之后的额度', after_limit

expend_coin = int(coin) - int(coin_now) + 200

print u'消耗了喵币:', expend_coin

print int(before_limit), int(after_limit)
use_limit = int(before_limit) - int(after_limit)


if float(expend_coin / 100) == float(retainage):
    print u'使用喵币抵扣金额正确'
else:
    print u'使用喵币抵扣金额错误'

driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[2]/ul/div[2]/div[3]/div[2]/div[1]').click()  # 跳到个人中心
sleep(1)
order_price = driver.find_element_by_xpath('//*[@id="refreshContainer"]/div[2]/ul/div/div[19]'
                                           '/div[1]/div[3]/div[3]/div[3]/span').text
print u'订单中的价格', order_price
if money == order_price:
    print u'商品首页中价格与订单中的价格相同'
else:
    print u'商品首页中价格与订单中的价格不相同'