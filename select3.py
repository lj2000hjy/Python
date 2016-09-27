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
        cursor=db.cursor()
        
    cursor.execute(select_sql)
    # 获取数据表中所有记录集
    records=cursor.fetchall()
    #print records
    
    #获得链接对象的描述信息
    desc=cursor.description
    #print desc
    '''
    ({'country': 'china', 'age': 38L, 'address': 'Shanghai', 'id': 1L, 'name': 'jack'}, {'country': 'china', 'age': 36L, 'address': 'beijing', 'id': 2L, 'name': 'jack'}, {'country': 'china', 'age': 36L, 'address': 'beijing', 'id': 3L, 'name': 'jack'}, {'country': 'china', 'age': 39L, 'address': 'Shanghai', 'id': 4L, 'name': 'lau'}, {'country': 'china', 'age': 36L, 'address': 'beijing', 'id': 5L, 'name': 'jerry'}, {'country': 'china', 'age': 36L, 'address': 'beijing', 'id': 6L, 'name': 'jerry'})
    '''
    #指定占位符宽度
    print '--------------------------------------------------------------'
    print '%1d %9s %15s %10d %15s' % (desc[0][0],desc[1][0],desc[2][0],desc[3][0],desc[4][0])
    print '--------------------------------------------------------------'
    
    # 使用元组tuple与fetchone结合
    for row in records:
        print '%1d %9s %15s %10d %15s' % row
    print '--------------------------------------------------------------'
finally:
    print '无论发生什么,我都执行...'
    cursor.close()
    db.close()


