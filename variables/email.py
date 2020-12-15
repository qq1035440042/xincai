import  random

def random_email():
    Email_addreaa = ['@qq.com','@163.com',]
    return ("".join(random.choice("0123456789") for i in range(8)) + random.choice(Email_addreaa))
random_email()
