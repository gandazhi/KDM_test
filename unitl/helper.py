# _*_ coding:utf-8 _*_
import sys
from time import sleep

import demo


class Init():

    def getBrowser(self):
        browser = demo.driver
        return browser

class help():

    def addCookie(self, name, value):
        Init().getBrowser().add_cookie({'name': name, 'value': value})
        sleep(1)

    def getUrl(self, url):
        Init().getBrowser().get(url)
        sleep(1)

    def findByXPathClick(self, xpath):
        try:
            Init().getBrowser().find_element_by_xpath(xpath).click()
            sleep(1)
        except Exception:
            print '定位不到元素,停止运行'
            sys.exit(0)

    def findByXPathSendKeys(self, xpath, sendKeys):
        try:
            Init().getBrowser().find_element_by_xpath(xpath).send_keys(sendKeys)
            sleep(1)
        except Exception:
            print '定位不到元素，停止运行'
            sys.exit(0)

    def chooseInstallmentNum(self, num):
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

    def moveTo(self, js):
        Init().getBrowser().execute_script(js)

    def judge(self, text, customStr):
        if text == customStr:
            print '状态改变成功，现在的状态是' + text
        else:
            print '状态改变失败，现在的状态是' + text

    def findByXPathText(self, xpath):
        try:
            text = Init().getBrowser().find_element_by_xpath(xpath).text
            sleep(1)
            return text
        except Exception:
            print '定位不到元素，停止运行'
            sys.exit(0)