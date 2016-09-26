#!/usr/bin/python
# _*_ coding:utf-8 _*_

# 正则模块re
# 1）正则表达式的常见应用：
# 验证字符串：如合法的邮件地址，HTTP地址等。
# 查找字符串
# 替换字符串
# 提取字符串
# 2）基本概念：
# 正则表达式：是一段文本或者一个公式，用来描述用某种模式去匹配一类字符串的公式，并且该公式具有一定的模式。
# 匹配：给定一段文本或者字符串，使用正则表达式从文本或字符串中查找出符合正则表达式的字符串。有可能文本或字符串存在不止一个部分满足给定的正则表达式，这是每一个这样的部分被称为一个匹配。
# 元字符：一次只能匹配一个字符或者一个位置。故元字符分：匹配字符的元字符和匹配位置的元字符。
# i）匹配字符的元字符
# ^string：匹配所有以string字符串开始的行
# string$：匹配所有以string字符串结尾的行
# $^：匹配空行
# \bStr：\b匹配以Str开始的单词（等价于\<）
# Str\b：\b匹配以Str结尾的单词（等价于\>）

# ii）匹配位置的元字符 
# \w：匹配单词里字符（字母，数字和下划线）
# \W：匹配单词里非字符
# \d：匹配单词里数字
# \D：匹配单词里非数字
# \s：匹配单词里空格字符
# \S：匹配单词里非空格字符
import re
s='Hello www.jeapedu.com'
res=r'\bjea'
print re.findall(res,s) #=> ['jea']
res=r'edu\b'
print re.findall(res,s) #=> ['edu']

s='''
ahello
www.baidu.com
hello world
nice hellod world
piece of helloe world
'''
res=r'\hello'
print 'hello:',re.findall(res,s) #=> hello: ['hello', 'hello', 'hello', 'hello']

s='a1b2c3d'
res='\w\d'
print re.findall(res,s) #=> ['a1', 'b2', 'c3']
res='\w\d\w'
print re.findall(res,s) #=> ['a1b', 'c3d']

# 字符集：用方括号括起来的字符集合，如果其中的任何一个字符被匹配，则它就会找到该匹配项，反字符集可在字符前加^。
s='''Plz write a mail to zhangbocheng189@163.com
or 649414754@qq.com,thanks!'''
res=r'\w[\w\.-]+@[\w\.-]+\.\w{2,4}'
# *表示匹配0次及其以上，+表示匹配1次及以上。
print re.findall(res,s) #=> ['zhangbocheng189@163.com', '649414754@qq.com']

# 分组或子模式：把一个正则表达式的全部或者部分分成一个或多个组。
# 其中，分组使用的字符是“（”和“）”。
s='''www.baidu.comwww.BaidU.comwww.bAIDU.comwww.baidu.comwww.Baidu.com'''
res1=r'(b|B)\w*(u|U)'
#*表示匹配0次及其以上，+表示匹配1次及以上。
res2=r'[bB]\w*(u|U)'
res3=r'[bB]\w*[uU]'
print res1+':' #=> (b|B)\w*(u|U):
print re.findall(res1,s)    #=> [('b', 'u'), ('B', 'U'), ('b', 'U'), ('b', 'u'), ('B', 'u')]
print res2+':' #=> [bB]\w*(u|U):
print re.findall(res2,s) #=> ['u', 'U', 'U', 'u', 'u']
print res3+':' #=> [bB]\w*[uU]:
print re.findall(res3,s) #=> ['baidu', 'BaidU', 'bAIDU', 'baidu', 'Baidu']

# 限定符：用于指定允许特定字符或字符集自身重复出现的次数。
# （pattern）？：重复0次或者1次，等价于{0,1}
# （pattern）*：至少重复0次，等价于{0,}
# （pattern）+：至少重复1次，等价于{1，}
# （pattern）{m:n}：重复至少m次，至多m次
# （pattern）？？：使用重复0次或者1次
# （pattern）*？：尽可能少地使用重复的第一个匹配
# （pattern）+？：尽可能少地使用重复但至少使用一次
s='''Tell to me 110-123-1114119 or call 4008-6688-9988
   or 13306247965'''
res=r'\d+\D\d+\D\d+'
#*表示匹配0次及其以上，+表示匹配1次及以上。
res1=r'\d{11}'
print re.findall(res,s)  #=> ['110-123-1114119', '4008-6688-9988']
print re.findall(res1,s) #=> ['13306247965']

# 通配符：匹配限定长度的字符串，例如点号匹配任意一个字符。
s='hello www.baidu.com'
print '----------------compile--------------------'
res='[\s\.]'
pat=re.compile(res)
print pat.findall(s) #=> [' ', '.', '.']
print pat.split(s)  #=> ['hello', 'www', 'baidu', 'com']
print '----------------split--------------------'
res='[\s\.]'
print re.findall(res,s) #=> [' ', '.', '.']
print re.split(res,s)   #=> ['hello', 'www', 'baidu', 'com']
 
# 补充一点小知识
# 1，sys模块：包含了与Python的解释器和它的环境有关的函数。
# 2，dir函数：列举模块定义的标识符，如函数、类和变量。
# 当为dir提供一个模块名称的时候，返回模块定义的名称列表，否则返回当前模块中定义的名称列表。
import sys
for i in sys.argv:
    print i #=> /home/ubuntu/workspace/regular.py

print dir() #=> ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'i', 'pat', 're', 'res', 'res1', 'res2', 'res3', 's', 'sys']







