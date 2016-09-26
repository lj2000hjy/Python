#!/usr/bin/python
# _*_ encoding:UTF-8 _*_
import random

num=random.randint(0,10)
 
print('--------小俊工作室----------')
def strToint(temp):
    try:
        g=int(temp)
        return g
    except:
        print('出错啦！请输入一个非0数字哦')

temp=input('输入一个非0数字吧：')
guess=strToint(temp)
n=0
while(guess!=num and n<2):
    if(guess>num):
        print('大了大了，你还有'+(str)(2-n)+'次机会哦')
        n=n+1
    else:
        print('小了小了，你还有'+(str)(2-n)+'次机会哦')
        n=n+1
    temp=input('再猜一个数字吧：')
    guess=int(temp)

if(n==2):
    print('太遗憾了，你已经没有机会了')
else:
    print('你太厉害了，猜对了！')

print("游戏结束")