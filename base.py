#!/usr/bin/python
# -*- coding: utf-8 -*-

int_var = 34;
print int_var;  #=> 34
print 12/2;     #=> 6
print 12.0/2;   #=> 6.0
print 12/2.0;   #=> 6.0


# '''三引号方式
str = '''
this is one line;
this is two line;
I'm a "good" student.
'''
print str;
#=>  this is one line;
#=>  this is two line;
#=>  I'm a "good" student.

# 查看变量的类型函数type()
print type(str);    #=> <type 'str'>

str_var=ur'''这是一行，
这是第二行，
这是第三行
'''
print str_var;
print type(str_var); #=> <type 'unicode'>

member = 3,4,5;
lists=[2,4,5,6];
print type(member); #=> <type 'tuple'>
print type(lists);  #=> <type 'list'>

# 输入函数raw_input()
# 注意：raw_input()输入的均是字符型。
name = raw_input('请输入你的名字:');
print "Hello, %s." % name;
#=> Hello, jacklau.

# 查看帮助函数help():
# help(id);
# 注意：
#Python的注释#：仅支持单行注释；
#另外，Python编程具有严格的缩进格式。