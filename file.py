#!/usr/bin/python
# _*_ coding:UTF-8 _*_

# 文件操作
# 1，读文件
# 在以'r'读模式打开文件以后可以调用read函数一次性将文件内容全部读出，也可以指定每次read读多少字节，例如：

fn='test1.txt'
fp=open(fn,'r') #以读的方式打开文件,文件必须首先存在
print 'reading pos:',fp.tell()
r=fp.read(20) #读取文件内容返回字符串
print 'have read:\"'+r+'\''
print 'reading pos:',fp.tell()
print fp.read()
fp.close()

# 2，写文件
# 如果想将某些内容写入文件，可以以'w'写的方式打开文件（如果文件不存在会创建），并且清空文件之前的内容。
fw='test.txt' 
fp=open(fw,'w') 
fp.write('www.google.com') 
fp.close()

# 3，读写文件r+，w+
# 二者区别在于：r+是必须针对已存在的文件；w+可以创建未存在的文件。
fn='rplus.txt'
fp=open(fn,'w+')    
r=fp.read(12)     
print r     
fp.close()

# 4,追加写入文件a
# ‘w'写模式打开的文件只能把内容写入文件，原有内容将被清除，若想保留，则用‘a'追加写模式。
fn='rplus.txt'
fp=open(fn,'w+')
fp.write('aaaaa\n')
fp.close()
fa=open('rplus.txt','a')
fa.write('bbbbb\n')
fa.close()
fa=open(fn,'r')
r=fa.read()
print r
fa.close()

# 格式化读写文件
# 1，格式化写文件
# 调用write函数，使用格式化控制符来格式化写入字符串。
fn='wformat.txt'
fw=open(fn,'w')
fw.write('%10s\t %3s\t %6s\n'%('name','age','sex'))
fw.write('%10s\t %3s\t %6s\n'%('张三',78,'male'))
fw.write('%10s\t %3s\t %6s\n'%('李四',50,'male'))
fw.write('%10s\t %3s\t %6s\n'%('王五',80,'male'))
fw.write('%10s\t %3s\t %6s\n'%('张强',90,'female'))
fw.close()

# 2，读成列表
# 文件的readlines函数可以将文本文件的若干行文本一一映射成列表的若干项，即文本文件的每一行映射成列表的一个数据项，每个数据项都是字符串。
fr=open('templist.txt','r')
print fr.readlines()
fr.close()

# 3，读成一行文件
# 调用readline函数读一行内容，而read函数是一次性将文件的内容全部读回。另外，可以用strip函数去掉\n和空格。
fr=open('templist.txt','r')
print fr.readline().strip().strip('\n')
print fr.readline().strip().strip('\n')
print fr.readline().strip().strip('\n')
fr.close()

# split格式化数据
fr=open('wformat.txt','r')
line1=fr.readline()
print line1
line2=fr.readline()
print line2
print line2.split('\t')
fr.close()

# 读取文件（格式化）的内容：
fr=open('wformat.txt','r')
while (1==1):
    line=fr.readline()
    if(line==''):
        break
    else:
        print line
fr.close()

# 5，读写子目录文件
# 只需指定文件时描述好路径即可，但是注意两点：1）转义字符的问题；2）不能创建文件夹，文件夹必须预先存在。
fn='test.txt' 
fp=open(fn,'w+') 
fp.write('www.python.com') 
fp.close()




