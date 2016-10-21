#!/usr/bin/python
# _*_ coding:UTF-8 _*_
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# 开启数据库服务：sudo service mysql start
import MySQLdb as mdb
# 创建连接,打开数据库连接
db = mdb.connect(host='127.0.0.1',user='root',passwd='',db='test')
# 使用cursor()方法获取操作游标 
cursor=db.cursor()
# 使用execute方法执行SQL语句
#cursor.execute("SELECT VERSION()")
#设置为utf-8编码
cursor.execute("SET NAMES utf8;")
#cursor.execute('SET CHARACTER SET utf8;')
#cursor.execute('SET character_set_connection=utf8;')

# 使用 fetchone() 方法获取一条数据。
data = cursor.fetchone()
print "Database version : %s " % data