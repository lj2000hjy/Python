#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

# 导入模块
import sys
sys.path.append("db_conn")
import connectdb

cursor=connectdb.cursor
db=connectdb.db

sql="INSERT INTO user_info(name,country,age,address) \
    VALUES \
    ('%s','%s','%d','%s')" % ('jerry','china',36,'beijing')
    
try:
    # 用execute执行插入操作,%s形式是为了防止sql注入
    reCount = cursor.execute(sql)
    # 提交到数据库执行
    # 注意：一定要写上conn.commit();事物不提交,将回滚。
    db.commit()
except:
    db.rollback()
finally:
    # 关闭操作游标
    cursor.close()
    # 关闭数据库连接
    db.close()

print reCount #=> 1
