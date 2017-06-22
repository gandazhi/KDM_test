# _*_ coding:utf-8 _*_

"""
    下一个预约订单，到个人中心预约订单中找到这个订单
    点击立即支付后，判断字符是否一致
    
"""
import sys
from time import sleep

import demo


def init():
    browser = demo.driver
    return browser


def addCookie():
    init().add_cookie({'name': 'PHPSESSID', 'value': 'oj6lhd1bhrgm2ll2monib8eki3'})


def getUrl(url):
    init().get(url)


def findByXPathClick(xpath):
    try:
        init().find_element_by_xpath(xpath).click()
    except Exception:
        print '定位不到元素,停止运行'
        sys.exit(0)

def findByXPathSendKeys(xpath, sendKeys):
    try:
        init().find_element_by_xpath(xpath).send_keys(sendKeys)
    except Exception:
        print '定位不到元素，停止运行'
        sys.exit(0)


def chooseInstallmentNum(num):
    if num == 1:
        return '/html/body/div[4]/div/div[3]/div/div[2]/span[1]'
    elif num == 3:
        return '/html/body/div[4]/div/div[3]/div/div[2]/span[2]'
    elif num == 6:
        return '/html/body/div[4]/div/div[3]/div/div[2]/span[3]'
    elif num == 9:
        return '/html/body/div[4]/div/div[3]/div/div[2]/span[4]'
    elif num == 12:
        return '/html/body/div[4]/div/div[3]/div/div[2]/span[5]'
    elif num == 18:
        return '/html/body/div[4]/div/div[3]/div/div[2]/span[6]'
    else:
        print '参数错误，分期只有1,3,6,9,12,18'


def moveTo(js):
    init().execute_script(js)


def judge(text, customStr):
    if text == customStr:
        print '状态改变成功，现在的状态是'+text
    else:
        print '状态改变失败，现在的状态是'+text


def findByXPathText(xpath):
    try:
        text = init().find_element_by_xpath(xpath).text
        return text
    except Exception:
        print '定位不到元素，停止运行'
        sys.exit(0)

if __name__ == '__main__':

    getUrl(demo.test_url+'/group')
    sleep(3)
    addCookie()
    getUrl(demo.test_url+'/Shop/personcenter/newpersoncenter')
    sleep(1)
    findByXPathClick('/html/body/div[4]/div[1]')
    sleep(1)
    findByXPathClick('//*[@id="refreshContainer"]/div[2]/ul/div[10]/div[1]/div[1]/div[2]')
    sleep(1)
    findByXPathClick('/html/body/div[3]/div[2]')
    sleep(1)
    findByXPathClick('//*[@id="zhifu"]')
    sleep(1)
    findByXPathSendKeys('//*[@id="time"]', '002017/06/19')  # 修改预约时间
    sleep(1)
    findByXPathClick('//*[@id="payfor"]')
    sleep(1)
    getUrl(demo.test_url+'/Shop/personcenter/newpersoncenter')
    sleep(1)
    findByXPathClick('//*[@id="refreshContainer"]/div[2]/ul/div[2]/div[3]/div[2]/div[4]')  # 进去预约订单
    sleep(1)

    moveTo("mui('#refreshContainer').scroll().scrollToBottom(100);")  # 执行js，滑到屏幕最下面

    sleep(3)
    findByXPathClick('//*[@id="refreshContainer"]/div[2]/ul/div/div[3]/div[1]/div[3]')
    sleep(1)
    findByXPathClick('//*[@id="pay"]')  # 立刻支付还款
    sleep(1)
    findByXPathClick(chooseInstallmentNum(6))  # 选择分期期数
    sleep(1)
    findByXPathClick('//*[@id="ok"]')  # 点击立刻支付
    findByXPathClick('/html/body/div[5]/p[2]')  # 提交审核完，点击确定

    judge(findByXPathText('/html/body/div[2]'), '审核中')





