#!/usr/bin/python
# _*_ encoding:UTF-8 _*_
# 何查看字符串有哪些内置方法： dir(str)
#1、字符串概念
#字符串："abcd1234" 或 'abcd1234'
#子字符串："abc"

# 2、字符编码：ascii unicode utf8
#python默认的文件编码是ascii，只能表示键盘上的数字，unicode是一个标准，能表示世界上所有的字符，utf8是Unicode的实现

# 3、字符串的len方法需注意字符的编码
a="1234"
# 输出函数print()
print len(a);   #=> 4
b="我是中国人"; #默认是ascii码，一个中文字符占用3个byte
print len(b);   #=> 15
c=u"我是中国人";    #u表示转换为Unicode码
print len(c);       #=> 5

d=b.decode('UTF-8');    #转换为unicode码
print len(d);           #=> 5

e="I'm a good student.";    
print e; #=>I'm a good student.

# 4、转义符让文本更好处理
f='I\'s very "good"';
print f; #=> I's very "good"

# 原字符串（输出）
g=r'this is one line\nthis is two line'; #r表示反斜杠不要转移
print g; #=> this is one line\nthis is two line

# 6、访问子字符串，序列的切片
s='abcde'; #序列的下标从0开始
print s[0]; #=> a
print s[-1];    #=> e
print s[len(s)-1];  #=> e

#成员有是有序排列的,可以通过下标偏移量访问到它的一个或者向个成员
#s[start:end:+1step]
#start:表示从哪个位置开始切片
#end:表示到哪个位置结束，但是不包括这个位置，不是表示切的个数
#+-step：表示步长，+表示从左边向右边切，-表示从右边向左边切
#特殊的位置，0表示第一个原始，-1表示最后一个原始
#s[:] 表示整个序列本身，s[:-1] 并不是表示整个序列，因为右边是开区间，是取不到的

print s[0:2:1]; #=> ab
print s[0:2:2]; #=> a
print s[0:4:2]; #=> ac
print s[1:3];   #=> bc
print s[:-1];   #=> abcd

t=u'我的名字叫jacklau.';
print t[0:12:2]; #=> 我名叫aka

# 7.替换字符串
old='abc'; #字符串一旦赋值，就不可改变，字符串是不能修改的，而是另外新建立了对象
#S.replace(old, new[, count]) -> string
new=old.replace('a',"I'm "); 
print new;  #=> I'm bc
print old;  #=> abc

# 查看变量的内存地址函数id()
print id(new); #=> 140010310048000
print id(old); #=> 140010310690856

# 8、查找子字符串
# S.find(sub [,start [,end]]) -> int
# 返回 -1就是没有找到
# 若找到则返回单词的起始位置索引
k='this is world';
print k.find('world'); #=> 8
print k[8:]; #=> world
m='world,that world,this world,world is world.';
print m.find('world');      #=> 0
print m.find('world',11);   #=> 11

# 9、字符串拼接
# 格式化控制符：%f浮点数；%s字符串;%d双精度浮点数
# 用+，超级丑陋之千万别用，会生成多个字符串
# 字符串模板 
# %s 字符串占位符
# %d 数字的占位符
# join是优秀的拼接方案
s1="my name is %s." % 'jacklau';
print s1; #=> my name is jacklau.
s2='my name is %s.' % 'jacklau';
print s2; #=> my name is jacklau.

# % 是一一对应的关系,位置从0开始
format_string="my name is %s, my year is %d." % ('jacklau',37);
print format_string;
#=> my name is jacklau, my year is 37.

str="this is {1} {0}.".format('my','apple');
print str; #=> this is apple my.
# 这种方式要多写很多符合，较上面.format方法麻烦些
str2="this is %(whose)s %(fruit)s." % {'whose':'my','fruit':'apple'};
print str2; #=> this is my apple.

s1='a';
s2='b';
s3='cde';
#join里面跟的是一个list
result=''.join([s1,s2,s3]);
print result; #=> abcde
result2=','.join([s1,s2,s3]);
print result2;  #=> a,b,cde

# 10、字符串运算
# 加法：
str3='www.baidu.com';
str4='python';
# 逗号运算符（，）：可以实现连接字符串和数字型数据
print str3,str4; #=> www.baidu.com python
print str3+str4; #=> www.baidu.compython

# 乘法：相当于同一个字符（串）的n次相加（Python独有的）
print str3*2; #=> www.baidu.comwww.baidu.com

# (not)in运算：判断一个字符（串）是否在某个字符串里面，(不)存在返回为真，否则为假
print 'w' in str3;  #=> True
print 'k' in str3;  #=> False
print 't' not in str3; #=> True

# 统计指定的子串在原字符串中有多少个
print str3.count('w'); #=> 3

strs='one,two,three,four';
print strs.split(','); #=> ['one', 'two', 'three', 'four']

url='''<a href="http://www.jinxiutuwen.com/blog/detail/2334543.html" class="test">百度一下</a>'''
print url[url.find('href')+6:url.find('html')+4];
#=> http://www.jinxiutuwen.com/blog/detail/2334543.html

