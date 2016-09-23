#!/usr/bin/python
# _*_ encoding:UTF-8 _*_

# 1，表达式：
# 是由数字，运算符，数字分组符号括号，自由变量和约束变量等以能求得数值的有意义排列方法所得的组合。表示通常有操作数和操作符两部分组成。
# 分类：算术表达式；关系表达式，逻辑表达式(and/or/not)
# 2，分支语句：
# 1）形式一：(if <condition>：)
sex='male'
if sex == 'male':
    print 'Man'

# 2）形式二：(if <condition>： else (if <condition>:))
sex=raw_input('Please input your sex:')
if sex == 'm' or sex=='male':
    print 'Man'
else:
    print 'Woman'
    
# 3）形式三：(if <condition>： elif <condition>: else ))（这是Python有而C没有的形式）
count = int(raw_input('Please input your score:'))
if count >= 90:
    print '优秀'
elif count >=80:
    print '优良'
elif count >= 70:
    print '合格'
elif count >= 60:
    print '及格'
else:
    print '不及格'
    
# 注意：Python没有switch语句。