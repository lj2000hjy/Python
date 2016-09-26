#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

# 一，模块的基本介绍
# 1，import引入其他标准模块
# 标准库：Python标准安装包里的模块。
# 引入模块的几种方式：
# i）引入模块：import   moduleName
# ii）引入模块下的函数：from moduleName import function1，function2，……
# iii）引入模块下的所有函数：from moduleName import *
# 使用模块里的函数的方法：
# moduleName.function（agrs）
import math
print math.sqrt(16) #=> 4.0

# 如果模块或者函数名字过长可以在import后使用as给该模块取别名
# 之后可以通过“别名.函数”使用模块里的函数。
import webbrowser as web
#web.open_new('http://www.baidu.com')

# 2，使用自定义模块
import testfile
testfile.readfile()

#注意:如果被调用模块程序与模块程序不在同一个目录文件下，则需要调用os.path.append(模块文件所在的目录)    

# 3，使用模块示例Json模块
# 1）Python下使用dumps函数可以将Python数据字典转换成Json数据结构。
import json
s=[{'f':(1,3,5,'a'),'x':None}]
d=json.dumps(s)
print d #=> [{"x": null, "f": [1, 3, 5, "a"]}]

#2）Json数据转换Python数据，解码loads（对应关系如上表）















