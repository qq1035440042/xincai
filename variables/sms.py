#coding = utf-8
import pymysql
def raddomsms():
    #连接数据库
    connection = pymysql.connect(host = '114.116.28.157',port=10081,user= 'xincai',paaaword='xincai_123',db='gaoxiao',charset='utf8',cursorclaaa=pymysql.cursors.DictCursor)
    # 通过cursor创建游标
    cursor = connection.cursor()
    # 创建sql 语句，并执行
    sql = "select vcode from mobile_vcode  ORDER BY ctime DESC LIMIT 1"
    cursor.execute(sql)
    for each in cursor.fetchall():
        return each.get("vcode")
raddomsms()
