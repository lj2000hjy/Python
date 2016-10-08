#!/usr/bin/python
# _*_ coding:UTF-8 _*_
# 1，字典定义
# 字典：由一对称之为键和值构成，用逗号间隔起来，用花括号括起来就构成了字典。语法结构：
# dict_name={key1:value1,key2:value2,key3:value3,……}
# 字典的数据项的值可以是字典，列表等数据类型。
# 2，基础操作
# 1）字典长度：
# len函数可以测得字典的数据项个数。
dic1={'a':'one','b':'two','c':'three'}
print type(dic1) #=> <type 'dict'>
print len(dic1) #=> 3

# 2）元素值的访问：
# Python的字典可以通过键获取其所对应的值，而序列型数据字符串，列表则是通过index索引来获取的。字典的元素的关系比较稀松，是无序的。
dic2={'a':'b','name':'jack','sex':'male','age':38}
print dic2['a']     #=> b
print dic2['sex']   #=>male
print dic2['age']   #=>38

# 3）元素值的修改：
# 通过键获取修改所对应的值。
dic2['name']='lau'
print dic2
#=> {'a': 'b', 'age': 38, 'name': 'lau', 'sex': 'male'}

# 4）元素项的删除：
# 通过del 字典名[键]来删除字典里的元素。
del dic2['sex']
print dic2 #=> {'a': 'b', 'age': 38, 'name': 'lau'}

# 5）元素项的增加：
# 通过字典名[新键]赋值的方式在字典里新增一个数据项。
dic2['qq']='3374978'
print dic2 #=> {'a': 'b', 'qq': '3374978', 'age': 38, 'name': 'lau'}

# in运算：
# 判断某键是否存在于字典里。
print 'name' in dic2
#=> True
# 注意：in运算查找的是Key值，而非value值。

# 四，字典的相关函数
# 1）clear函数：清空字典数据项。
print dic2  #=> {'a': 'b', 'qq': '3374978', 'age': 38, 'name': 'lau'}
dic2.clear()
print dic2 #=> {}

# 2）copy函数：字典复制，与源对象间的关系是备份关系。
dic3=dic1.copy()
print dic3 #=> {'a': 'one', 'c': 'three', 'b': 'two'}

# 3）get函数：获取某键锁对应的值，等价于dict_name[键]。
print dic3.get('name')  #=> None
print dic3.get('a')     #=> one

# 4）keys函数：获取字典所有的key。
print dic3.keys() #=> ['a', 'c', 'b']

# 5）values函数：获取字典所有的value。
print dic3.values() #=> ['one', 'three', 'two']

# 6）items函数：获取字典所有的key-value的列表对象。
print dic3 #=> {'a': 'one', 'c': 'three', 'b': 'two'}
print dic3.items() #=> [('a', 'one'), ('c', 'three'), ('b', 'two')]

# 7）update函数：更新字典里某键（key）的键值（value），如果更新的key原字典没有，则update就向字典里添加一项数据。
new={'age':37}
add={'name':'zhangsan'}
print dic3
#=> {'a': 'one', 'c': 'three', 'b': 'two'}
dic3.update(new)
dic3.update(add)
print dic3
#=> {'a': 'one', 'c': 'three', 'b': 'two', 'age': 37, 'name': 'zhangsan'}

# 8）dict函数：创建字典。
# 下面举例三种创建字典的方法：
# 创建空字典
d0=dict() 
print d0 #=> {}

# 通过赋值创建字典
d1=dict(name='jack',age=37,qq=3374978)
print d1    #=> {'qq': 3374978, 'age': 37, 'name': 'jack'}

# 使用一对列表创建字典
val=['lisi','649414754',25]
key=range(1,4)
d2=dict(zip(key,val))
print d2 #=> {1: 'lisi', 2: '649414754', 3: 25}

# 9）pop和popitem函数：pop方法通过键key获取其值value并从字典中删除该数据项；
# popitem函数则是随机移除一个数据项，返回值是元组。
val=['Tom','Jack','Rose','John','Mark']
key=range(1,6)
lst=zip(key,val)
print lst   #=> [(1, 'Tom'), (2, 'Jack'), (3, 'Rose'), (4, 'John'), (5, 'Mark')]
dic=dict(lst)
print dic   #=> {1: 'Tom', 2: 'Jack', 3: 'Rose', 4: 'John', 5: 'Mark'}
print dic.pop(2) #=> Jack
print dic.popitem() #=> (1, 'Tom')
print dic
#=> {3: 'Rose', 4: 'John', 5: 'Mark'}

# 10）实践应用：字典和for循环遍历字典。
# i）通过in运算和键，来访问字典的值。
key=range(1,6)
print key #=> [1, 2, 3, 4, 5]
val=['Tom','Jack','Rose','John','Mark']
lst=zip(key,val)
print lst #=> [(1, 'Tom'), (2, 'Jack'), (3, 'Rose'), (4, 'John'), (5, 'Mark')]
dic=dict(lst)
print dic #=> {1: 'Tom', 2: 'Jack', 3: 'Rose', 4: 'John', 5: 'Mark'}
for x in dic:
    #print x
    print dic[x]
#=> Tom
#=> Jack
#=> Rose
#=> John
#=> Mark

# ii）通过items函数返回值为（key，value）元组组成的列表来访问。
for (k,v) in dic.iteritems(): #iteritems比items执行效率高
    print 'dic[',k,']=',v
#=> dic[ 1 ]= Tom
#=> dic[ 2 ]= Jack
#=> dic[ 3 ]= Rose
#=> dic[ 4 ]= John
#=> dic[ 5 ]= Mark

# enumerate枚举类型
c = {'a':1, 'b':2, 'c':3}
d=c.iteritems()
print d #=> <dictionary-itemiterator object at 0x7f1d35c574c8>
enu=enumerate(d)
print enu #=> <enumerate object at 0x7f1d35c50d20>
for key,value in enu:
    #print "{0}:{1}".format(key, value)
    #print "{index}:{item}".format(index=key,item=value)
    
    #print "%(index)s:%(item)s" % {'index':key,'item':value}
    print "%s : %s" % (key, value)
'''
0 : ('a', 1)
1 : ('c', 3)
2 : ('b', 2)
'''