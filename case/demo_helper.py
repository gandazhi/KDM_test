# _*_ coding:utf-8 _*_

from unitl.helper import help
from unitl.unitls import url


class demo:

    helper = help()

    if __name__ == '__main__':
        helper.getUrl(url.test_url+'/group')
        helper.addCookie('PHPSESSID', '401dujrib3m7embi56mkoipc84')
        helper.getUrl(url.test_url+'/Shop/personcenter/newpersoncenter')
        helper.findByXPathClick('/html/body/div[4]/div[1]')
        helper.findByXPathClick('//*[@id="refreshContainer"]/div[2]/ul/div[10]/div[1]/div[1]/div[2]')
        helper.findByXPathClick('/html/body/div[3]/div[2]')
        helper.findByXPathClick('//*[@id="zhifu"]')
        helper.findByXPathSendKeys('//*[@id="time"]', '002017/06/19')  # 修改预约时间
        helper.findByXPathClick('//*[@id="payfor"]')
        helper.getUrl(url.test_url + '/Shop/personcenter/newpersoncenter')
        helper.findByXPathClick('//*[@id="refreshContainer"]/div[2]/ul/div[2]/div[3]/div[2]/div[4]')  # 进去预约订单
        helper.moveTo("mui('#refreshContainer').scroll().scrollToBottom(100);")  # 执行js，滑到屏幕最下面
        helper.findByXPathClick('//*[@id="refreshContainer"]/div[2]/ul/div/div[6]/div[1]/div[3]')  # //*[@id="refreshContainer"]/div[2]/ul/div/div[5]/div[1]/div[3]
        helper.findByXPathClick('//*[@id="pay"]')  # 立刻支付还款
        helper.findByXPathClick(helper.chooseInstallmentNum(1))  # 选择分期期数
        helper.findByXPathClick('//*[@id="ok"]')  # 点击立刻支付
        helper.findByXPathClick('/html/body/div[5]/p[2]')  # 提交审核完，点击确定

        helper.judge(helper.findByXPathText('/html/body/div[2]'), '审核中')