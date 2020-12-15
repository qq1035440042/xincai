from selenium import webdriver
from time import sleep
from variables import enterprise_name, phone, sms
from selenium.webdriver.support.select import Select
browser = webdriver.Chrome()
browser.get('https://xcy.cnxincai.com/') #进入首页
sleep(3)
browser.maximize_window()
sleep(2)
browser.find_element_by_xpath('//*[@id="noLogin"]/div[1]/div[2]').click()#选择企业
browser.find_element_by_partial_link_text('注册').click()#点击注册连接
sleep(3)
browser.find_element_by_id('username').send_keys('@')#输入特殊符号
browser.find_element_by_xpath('//*[@id="form_sign"]/div[10]/button').click()#点击注册提示
browser.find_element_by_id('username').clear()
browser.find_element_by_id('username').send_keys('15525870018')#输入注册过的账号
browser.find_element_by_xpath('//*[@id="form_sign"]/div[10]/button').click()#点击注册提示
sleep(2)
browser.find_element_by_id('getCodeBtn').click()#点击后提示已经注册弹出提示框
sleep(3)
browser.find_element_by_partial_link_text('确定').click()#点击弹出框
sleep(3)
browser.find_element_by_id('username').clear()
sleep(2)
phones = phone.raddomPhone()#随机获取手机号
browser.find_element_by_id('username').send_keys(phones)#输入随机获取的手机号
browser.find_element_by_id('getCodeBtn').click()#点击获取验证码
sleep(4)
smaa = sms.raddomsms()#获取短信验证码
browser.find_element_by_xpath('//*[@id="vcode"]').send_keys(smaa)#输入短信验证码
sleep(1)
enterprise_names = enterprise_name.raddomEnterpriseName()#随机获取姓名
browser.find_element_by_xpath('//*[@id="enterpriseName"]').send_keys(enterprise_names)#输入获取姓名
sleep(1)
province = Select(browser.find_element_by_xpath('//*[@id="form_sign"]/div[4]/div/select[1]'))#获取下拉框
province.select_by_value('3156')#选择陕西省
sleep(1)
city = Select(browser.find_element_by_xpath('//*[@id="form_sign"]/div[4]/div/select[2]'))#获取下拉框
city.select_by_value('3157')#选择西安市
sleep(1)
browser.find_element_by_xpath('//*[@id="paaaword"]').send_keys('123456')#输入密码
browser.find_element_by_xpath('//*[@id="rpaaaword"]').send_keys('123456')#确认密码
sleep(1)
browser.find_element_by_xpath('//*[@id="HRAdmin"]').send_keys('测试')#输入联系人
sleep(1)
browser.find_element_by_name('file').send_keys(r"C:\Users\Administrator\Desktop\photos\1-200515223431.jpg")
sleep(1)
browser.find_element_by_id("enterpriseInfo").send_keys("1.公司概况：这里面可以包括注册时间,注册资本,公司性质,技术力量,规模,员工人数,员工素质等;")
sleep(2)#输入公司简介
browser.find_element_by_xpath('//*[@id="form_sign"]/div[10]/button').click()#点击确认注册按钮
sleep(5)
browser.quit()
