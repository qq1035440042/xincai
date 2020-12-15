from selenium import webdriver
from time import sleep
from variables import enterprise_new_phone,enterprise_name,email,phone,scroll_bar
browser = webdriver.Chrome()
browser.get('https://xcy.cnxincai.com/') #进入首页
sleep(3)
browser.maximize_window()
sleep(2)
browser.find_element_by_xpath('//*[@id="noLogin"]/div[1]/div[2]').click()#选择企业
sleep(2)
newphones = enterprise_new_phone.Etphone()#获取新注册的用户
browser.find_element_by_xpath('//*[@id="form_sign"]/div[1]/input').send_keys(newphones)#输入账号
browser.find_element_by_xpath('//*[@id="form_sign"]/div[2]/input').send_keys('123456')#输入密码
browser.find_element_by_xpath('//*[@id="form_sign"]/button').click()#点击登录
sleep(3)

browser.find_element_by_xpath('//*[@id="layui-layer1"]/span[1]/a').click()#
sleep(3)
browser.find_element_by_xpath('//*[@id="nav"]/li[1]/a/cite').click()#
sleep(1)
browser.find_element_by_xpath('//*[@id="nav"]/li[1]/ul/li[1]/a').click()#点击企业信息
sleep(1)
Enterprise_information = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/iframe')#切换到企业信息窗口
browser.switch_to.frame(Enterprise_information)
sleep(1)
browser.find_element_by_id("enterpriseName").clear()#清空
name = enterprise_name.raddomEnterpriseName()
browser.find_element_by_id("enterpriseName").send_keys(name)#输入名称
sleep(1)
browser.find_element_by_xpath('//*[@id="enterpriseImg"]').send_keys(r'C:\Users\Administrator\Desktop\photos\t014eb4c55fbd48bf79.jpg')
sleep(1)
browser.find_element_by_id('addreaa').send_keys('陕西省西安市清华科技园')
sleep(2)
S1 = browser.find_element_by_xpath('//*[@id="uploadForm"]/div[1]/div[6]/div/div')#下拉框
S1.click()
browser.find_element_by_xpath('//*[@id="uploadForm"]/div[1]/div[6]/div/div/dl/dd[1]').click()#选择下拉框内容
S1.click()
browser.find_element_by_xpath('//*[@id="uploadForm"]/div[1]/div[6]/div/div/dl/dd[2]').click()
S1.click()
browser.find_element_by_xpath('//*[@id="uploadForm"]/div[1]/div[6]/div/div/dl/dd[3]').click()
S1.click()
browser.find_element_by_xpath('//*[@id="uploadForm"]/div[1]/div[6]/div/div/dl/dd[4]').click()
S1.click()
browser.find_element_by_xpath('//*[@id="uploadForm"]/div[1]/div[6]/div/div/dl/dd[5]').click()
sleep(2)
phones = phone.raddomPhone()#随机获取手机号
browser.find_element_by_id('telPhone').send_keys(phones)
sleep(1)
emails = email.random_email()#随机获取邮箱
browser.find_element_by_id('mailbox').send_keys(emails)
sleep(1)
browser.find_element_by_xpath('//*[@id="enterpriseInfo"]').clear()
browser.find_element_by_xpath('//*[@id="enterpriseInfo"]').send_keys('1.公司概况：这里面可以包括注册时间,注册资本,公司性质,技术力量,规模,员工人数,员工素质等;')
sleep(1)
js = scroll_bar.script()
browser.execute_script(js)#下拉滚动条
industry = browser.find_element_by_xpath('//*[@id="uploadForm"]/div[2]/div[2]/div/div')#遍历企业所属行业
for digital in range(1,7):
    industry.click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="uploadForm"]/div[2]/div[2]/div/div/dl/dd[%s]'% digital).click()
    sleep(1)
money = browser.find_element_by_xpath('//*[@id="uploadForm"]/div[2]/div[3]/div/div')
for digital in range(1,17):
    money.click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="uploadForm"]/div[2]/div[3]/div/div/dl/dd[%s]'% digital).click()
    sleep(1)
browser.find_element_by_xpath('//*[@id="registerCapital"]').send_keys('5000000')
#browser.quit()