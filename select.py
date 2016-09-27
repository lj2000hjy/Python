#!/usr/bin/python
# _*_ coding: UTF-8 _*_
# 导入模块
import sys
sys.path.append("db_conn")
print sys.path
import connectdb

cursor=connectdb.cursor
db=connectdb.db
# 数据库查询操作
# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall():接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

insert_sql="INSERT INTO user_info(id,name,country,age,address)VALUES('%d','%s','%s','%d','%s')"%(1,'jack','china',38,'Shanghai')

select_sql="SELECT * FROM user_info"

update_sql='UPDATE user_info SET name="jack" WHERE id=3'

delete_sql='DELETE FROM user_info WHERE id=4'
try:
    '''
    cursor.execute(update_sql)
    # 注意：一定要写上conn.commit();事物不提交,将回滚。
    db.commit()
    
    cursor.execute(delete_sql)
    # 注意：一定要写上conn.commit();事物不提交,将回滚。
    db.commit()
    
    cursor.execute(insert_sql)
    # 注意：一定要写上conn.commit();事物不提交,将回滚。
    db.commit()
    '''
    
    
    cursor.execute(select_sql)
    #records=cursor.fetchall()
    #print records
    #获得结果集的记录总数
    numrows=int(cursor.rowcount)
    
    
    '''
        *************************** 1. row ***************************
        id: 1
        name: jack
        country: china
        age: 38
        address: Shanghai
    '''
    # 使用元组tuple与fetchone结合
    for i in range(numrows):
        row=cursor.fetchone() #每次取出一条记录集
        print row #=> (1L, 'jack', 'china', 38L, 'Shanghai')
        print len(row) #=> 5
        #print 'id={0},name={1},country={2},age={3},address={4}'.format(row[0],row[1],row[2],row[3],row[4])
        print 'id=%d, name=%s, country=%s, age=%d, address=%s' % (row[0],row[1],row[2],row[3],row[4])
 
finally:
    print '无论发生什么,我都执行...'
    cursor.close()
    db.close()


