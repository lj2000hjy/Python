#!/usr/bin/python
# _*_ coding: UTF-8 _*_
   
# 列表的解析：[val_expr for val in list_name],其中：
# val_expr：是变量val的运算表达式，
# val用于存储for每次从list_name列表取出的元素的值，用每一个val_expr的值作为构建新列表的元素项。    
lst=range(1,10)
print lst #=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
lsts=[x**3 for x in lst]
print lsts
#=> [1, 8, 27, 64, 125, 216, 343, 512, 729]

#相关函数
# len（）函数
print len(lst) #=> 9

# count（）函数：统计列表里某元素项出现的次数
print lst.count(2) #=> 1

# insert函数：将对象添加到列表指定位置，列表里的元素顺序后移。
print lst.insert(2,10) #=> None

# append和extend针对python的列表
# 列表内的元素为对象，可以为数字、字符串、列表等等
# append添加的是一个对象, extend添加一个列表

# append函数：将对象添加到列表尾部位置
print lst.append(11) #=> None

li=[]
for x in lst:
    li.append(x)
print li
#=> [1, 2, 10, 3, 4, 5, 6, 7, 8, 9, 11]

# extend函数：将一个列表是所有元素以个体的方式添加到列表的尾部。
li1=range(1,6)
li2=range(6,11)
print li1 #=> [1, 2, 3, 4, 5]
print li2 #=> [6, 7, 8, 9, 10]

li1.extend(li2)
print li1 #=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# remove函数：删除列表的第一次出现的指定元素。
li=range(1,4)*3
print li #=> [1, 2, 3, 1, 2, 3, 1, 2, 3]
li.remove(2)
print li #=> [1, 3, 1, 2, 3, 1, 2, 3]

# pop函数：删除列表指定位置的元素或者列表的尾部元素
li=range(1,4)*3
li.pop()
print li #=> [1, 2, 3, 1, 2, 3, 1, 2]
li.pop(3)
print li #=> [1, 2, 3, 2, 3, 1, 2]

#去除二维列表[]，二维变一维
#嵌套循环实现
# isinstance函数可以判定数据的类型。
li=[1,2,4,range(1,4),5,range(1,4),6]
print li #=> [1, 2, 4, [1, 2, 3], 5, [1, 2, 3], 6]
k=0
for li1 in li:
    # 判断类型 isinstance(obj, type),type为str,list,int等
    if isinstance(li1,list):
        j=0
        for li2 in li1:
            li.insert(k+j,li2)
            li.remove
            j=j+1
        del li[k+j]
    k=k+1
print li
#=> [1, 2, 4, 1, 2, 3, 5, 1, 2, 3, 6]

# 单循环实现：
li=[1,2,4,range(1,4),5,range(1,4),6]
print li #=> [1, 2, 4, [1, 2, 3], 5, [1, 2, 3], 6]
b=[]
for i in li:
    if isinstance(i,list):
        b.extend(i)
    else:
         b.append(i)
print(b)
#=> [1, 2, 4, 1, 2, 3, 5, 1, 2, 3, 6]

# enumerate枚举类型
a = [1, 2, 3]
print enumerate(a) #<enumerate object at 0x7f1966192dc0>

for index, item in enumerate(a):
    #print "{0}:{1}".format(index, item)
    #print "{index}:{item}".format(index=index,item=item)
    
    #print "%(index)s:%(item)s" % {'index':index,'item':item}
    print "%d : %d" % (index, item)

'''
0:1
1:2
2:3
'''

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']  
print [b + '+' + g for b in boys for g in girls if b[0] == g[0]]  
#=> ['chris+clarice', 'arnold+alice', 'bob+bernice']

print [(i, j) for i in range(3) for j in range(i)]
#=> [(1, 0), (2, 0), (2, 1)]

print [(i,j) for i in range(3) for j in range(3)]
#=> [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

print { i:j for i,j in zip(range(3),range(3))}
#=> {0: 0, 1: 1, 2: 2}


