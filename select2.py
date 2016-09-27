#!/usr/bin/python
# _*_ coding: UTF-8 _*_
# 导入模块
import MySQLdb as mdb
#connect to a database 'test'
db=mdb.connect(host='localhost',user='root',passwd='',db='test')

select_sql="SELECT * FROM user_info"
try:
    #使用字典cursor
    with db: #获取连接上的字典cursor，每一个cursor其实都是cursor的子类
        cursor=db.cursor(mdb.cursors.DictCursor)
        
    cursor.execute(select_sql)
    records=cursor.fetchall()
    #print records
    
    # 使用元组tuple与fetchone结合
    for row in records:
        print 'id=%d, name=%s, country=%s, age=%d, address=%s' % (row['id'],row['name'],row['country'],row['age'],row['address'])
    print '--------------------------------------------------------------'
finally:
    print '无论发生什么,我都执行...'
    cursor.close()
    db.close()


