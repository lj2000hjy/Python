#!/usr/bin/python
# _*_ coding: UTF-8 _*_

# 元组（Tuple）
#元组的结构，访问，使用方法和列表基本一致，区别有二：
# 1）使用圆括号（）将各个数据项括起来；
# 2）元组的元素值不可修改。
a,b=('one','two')
print "a=%s,b=%s" % (a,b) #=> a=one,b=two

t=(range(1,10))
print type(t) #=> <type 'list'>
print t     #=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print t[3]  #=> 4
print t[2:8]    #=> [3, 4, 5, 6, 7, 8]
print len(t) #=> 9
num=range(len(t))
print num #=> [0, 1, 2, 3, 4, 5, 6, 7, 8]
for i in num:
    print 't[%d]=%d' %(i,t[i])
'''
t[0]=1
t[1]=2
t[2]=3
t[3]=4
t[4]=5
t[5]=6
t[6]=7
t[7]=8
t[8]=9
'''

# enumerate枚举类型
b=(1, 2, 3)
for index,item in enumerate(b):
    #print "{0}:{1}".format(index, item)
    #print "{index}:{item}".format(index=index,item=item)
    
    #print "%(index)s:%(item)s" % {'index':index,'item':item}
    print "%d : %d" % (index, item)
'''
0 : 1
1 : 2
2 : 3
'''
    
    
    
    