# _*_ coding:utf-8 _*_
import demo

a = 'ss'
b = '/bb'

print a+b
"""
    //*[@id="refreshContainer"]/div[2]/ul/div/div[3]/div[1] 预约订单 第3个ListView 除去支付方式的XPath  第3个ListView div[3]
    //*[@id="refreshContainer"]/div[2]/ul/div/div[4]/div[1] 预约订单 第4个ListView 除去支付方式的XPath  第4个ListView div[4]
    区别：第三个ListView是div[3]  第四个ListView是div[4]
    
    //*[@id="refreshContainer"]/div[2]/ul/div/div[15]/div[1]/div[3]/div[3]/div[3]/span
    //*[@id="refreshContainer"]/div[2]/ul/div/div[14]/div[1]/div[3]/div[3]/div[3]/span
    
    
    //*[@id="refreshContainer"]/div[2]/ul/div/div[4]/div[1]/div[3]
    //*[@id="refreshContainer"]/div[2]/ul/div/div[3]/div[1]/div[3]
    
    
    //*[@id="refreshContainer"]/div[1]/ul/div/div[2]/div[1]/div[2]/div[3]/div[2]/span
    //*[@id="refreshContainer"]/div[1]/ul/div/div[1]/div[1]/div[2]/div[3]/div[2]/span
"""

c = u'2'
d = u'3'
print int(d) - int(c)
e = u'd,e,a'
print e.replace(',', '')

def s():
    print u'只想了s()'

def r():
    print u'执行了r()'

if __name__ == '__main__':
    s()
    r()
    browser = demo.driver
    browser.get(demo.test_url+'/group')
