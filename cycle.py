#!/usr/bin/python
# _*_ coding:UTF-8 _*_

# 1，while语句：与C在表达上有区别，c有while与do……while形式；Python下：while与while……else……形式
# 1）while形式下：
i=1
while i < 5:
    print 'Welcome you!'
    i = i+1 #或 i+=1

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