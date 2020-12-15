def script():
    return "var q=document.documentElement.scrollTop=10000"#下拉滚动条到底部
    #使用方法driver.execute_script(js)
script()
'''滚动条到元素target = driver.find_element_by_id("id_keypair")
driver.execute_script("arguments[0].scrollIntoView();", target)'''
