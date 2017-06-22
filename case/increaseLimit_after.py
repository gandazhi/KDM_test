# _*_ coding:utf-8 _*_

from time import sleep

import demo


def init():
    browser = demo.driver
    return browser


def getUrl(url):
    init().get(url)


def addCookie():
    init().add_cookie({'name': 'PHPSESSID', 'value': 'oj6lhd1bhrgm2ll2monib8eki3'})


