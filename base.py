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

#查看模块里有哪些方法: dir(list)
print dir(list)
#=> ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']