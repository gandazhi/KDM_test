# _*_coding:utf-8_*_
import demo
from unitl.unitls import url
from unitl.helper import help


class seckillOrders:
    helper = help()
    helper.getUrl(url.test_url+'/group')
    helper.addCookie('PHPSESSID', 'oj6lhd1bhrgm2ll2monib8eki3')
    helper.getUrl(url.test_url+'/Shop/personcenter/newpersoncenter')
    before_limit = helper.findByXPathText('//*[@id="myTargetElement"]')
    print before_limit

    helper.getUrl(url.test_url+'/Activity/Seckill/seckill')
    shopPrice = helper.findByXPathText('//*[@id="refreshContainer"]/div[1]/ul/div/div[1]/div[1]/div[2]/div[4]/span/span')  # 商城listView中的价格
    sellNums = helper.findByXPathText('//*[@id="refreshContainer"]/div[1]/ul/div/div[1]/div[1]/div[2]/div[3]/div[2]/span')  # 购买之前的价格

    helper.findByXPathClick('//*[@id="refreshContainer"]/div[1]/ul/div/div[1]/div[1]/div[2]')
    helper.findByXPathClick('/html/body/div[3]/div[2]')
    helper.findByXPathClick('//*[@id="zhifu"]')
    helper.findByXPathSendKeys('//*[@id="time"]', '002017/06/07')
    helper.findByXPathClick('//*[@id="payfor"]')


# browser = demo.driver
# browser.get(demo.formal_url+'/group')
# browser.add_cookie({'name': 'PHPSESSID', 'value': 'oj6lhd1bhrgm2ll2monib8eki3'})
# browser.get(demo.formal_url+'/Shop/personcenter/newpersoncenter')  # 跳到个人中心，保存现在的额度
# before_limit = browser.find_element_by_xpath('//*[@id="myTargetElement"]').text
#
# # 购买一个秒杀商品，购买之前保存价格和已售数量
# browser.get(demo.formal_url+'/Activity/Seckill/seckill')
# shopPrice = browser.find_element_by_xpath('//*[@id="refreshContainer"]/div[1]/ul/div/div[1]'
#                                            '/div[1]/div[2]/div[4]/span/span').text  # 保存商城ListView中的价格
# sellNums = browser.find_element_by_xpath('//*[@id="refreshContainer"]/div[1]/ul/div/div[1]'
#                                          '/div[1]/div[2]/div[3]/div[2]/span').text   # 保存购买之前的销量
#
# browser.find_element_by_xpath('//*[@id="refreshContainer"]/div[1]/ul/div/div[1]/div[1]/div[2]').click()
# browser.find_element_by_xpath('/html/body/div[3]/div[2]').click()
# browser.find_element_by_xpath('//*[@id="zhifu"]').click()
# browser.find_element_by_xpath('//*[@id="time"]').send_keys('002017/06/07')
# browser.find_element_by_xpath('//*[@id="payfor"]').click()
#
# # 购买秒杀商品后，对比商品listView中的价格和订单中心中的价格
# browser.get(demo.formal_url+'/Activity/Seckill/seckill')
# new_sellNums = browser.find_element_by_xpath('//*[@id="refreshContainer"]/div[1]/ul/div/div[1]'
#                                              '/div[1]/div[2]/div[3]/div[2]/span').text
# if (int(new_sellNums) - int(sellNums)) == 1:
#     print u'秒杀商品正常+1'
# else:
#     print u'检查有没其他人同时下单，如果没有则秒杀商品销量错误'
# browser.get(demo.formal_url+'/Shop/personcenter/newpersoncenter')
