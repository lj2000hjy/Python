#!/usr/bin/python
# _*_ encoding:UTF-8 _*_

# 1，while语句：与C在表达上有区别，c有while与do……while形式；Python下：while与while……else……形式
# 1）while形式下：

i=1
while i < 5:
    print 'Welcome you!'
    i = i+1

# 2）while……else……形式下：
i=1
while i<5:
    print 'Welcome you!'
    i=i+1
else:
    print "While over!"  #循环正常结束

# 注意：如果while非正常状态结束（即不按循环条件结束），则else语句不执行。
i=1
while i<5:
    print 'Welcome you!'
    i=i+1
    if i==2:
        print 'While……'
        break
else:
    print "While over!"

#补充：continue语句:在while循环体中出现时，本次循环continue之下的语句不被执行，直接进入下一次循环。
i=1
while i<=5:
    if i==2 or i==4:
        print 'While……continue'
        i=i+1
        continue
    print 'Welcome you!'
    i=i+1
else:
    print "While over!"

# 遍历：逐一访问列表里的各个元素通过for循环来依次取出列表的各个元素项的值。
lst=[1,2,3,4,5]
li=lst*3
print li
#=> [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
i=0
for val in li:
    print 'li[%d]' % i,val
    i+=1
    
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


# 元组（Tuple）
#元组的结构，访问，使用方法和列表基本一致，区别有二：
# 1）使用圆括号（）将各个数据项括起来；
# 2）元组的元素值不可修改。
t=(range(1,10))
print type(t)
print t
print t[3]
print t[2:8]