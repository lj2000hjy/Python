#!/usr/bin/python
# _*_ encoding:UTF-8 _*_

# 1,函数定义及其调用：
#define function:add （函数说明）
def add(x, y):   #函数头部，注意冒号，形参x,y
    z=x+y       #函数体
    return z    #返回值
#define main function
def main():
    a=12
    b=13
    c=add(a, b)   #函数调用，实参a,b
    print c #=> 25
    
main()           #无参函数调用

# 注意：这部分与C的存在的异同在于：
# 1，形参与实参的用法，无参函数，有参函数，默认参数等规则一致。
# 如def add(x,y=2)，调用可以是add（3）也可以是add（3,4），add（y=34，x）
# 2，C的形参需要指定数据类型,而Python不需要。

#Python的返回值允许有多个。
def test(n1, n2):
    print n1,
    print n2
    n=n1+n2
    m=n1*n2
    p=n1-n2
    e=n1**n2
    return n,m,p,e
    
print 'Entry programme1'
sum,multi,plus,powl=test(2, 10)   #一一对应的赋值方式
print 'sum=',sum
print 'multi=',multi
print 'plus=',plus
print 'powl=',powl
re=test(2, 10)
print type(re) #=> <type 'tuple'>
print re  #=> (12, 20, -8, 1024) 数据类型为：'tuple'
print re[0],re[1],re[2],re[3]
#=> 12 20 -8 1024

# 2，局部变量：
def f1():
    x=12     #局部变量
    print x #=> 12
    
def f2():
    y=13      #局部变量
    print y #=> 13
    
def f3():
    print x       #错误：没有定义变量x，这与“不需要预先定义数据类型”不矛盾
    print y
    
def main():
    f1()
    f2()
    #f3()#变量报错  
    
main()

# 3，修改全局变量的值：
def modifyGlobal():
    global x              #全局变量定义
    print 'write x =-1'
    x=-1
    
def main():
# printLocalx()
# printLocaly()
# readGlobal()
    modifyGlobal()
  
x=200
#y=100
print 'before modified global x=',
print x #=> before modified global x= 200
main()
print 'after modified global x=',
print x #=> after modified global x= -1
