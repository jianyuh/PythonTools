# -*- coding:utf-8 -*-
# file: rename.py
#
#获取文件时间？排序？？

import os
import re
import string
perfix = 'h'						# perfix 为重命名后的文件起始字符
length = 2 							# length 为除去perfix后，文件名要达到的长度
base = 1								# 文件名的起始数
format_change = 'mp4'							# 文件的后缀名
format_source = 'srt'
# 函数PadLeft将文件名补全到指定长度
# str 为要补全的字符
# num 为要达到的长度
# padstr 未达到长度所添加的字符

'''
def PadLeft(str , num , padstr):
	stringlength = len (str)
	n = num - stringlength
	if n >=0 :
		str=padstr * n + str
	return str
# 为了避免误操作，这里先提示用户
print ("the files in %s will be renamed" % os.getcwd())
#input = (raw_input('press y to continue\n'))		# 获取用户输入
#if input != 'y':							# 判断用户输入，以决定是否执行重命名操作
#	exit()

'''

filenames = os.listdir(os.curdir)				# 获得当前目录中的内容
#print (filenames)

filenames_src = []
filenames_dst = []

#print (re.match('*.mp4',filenames))
for filename in filenames:
    t = filename.split('.')
    m = len(t)
    if t[m-1] == 'srt':
        filenames_src.append(t[0])

#print (filenames_src)

for filename in filenames:
    t= filename.split('.')
    m = len(t)
    if t[m-1] == 'mp4':
        filenames_dst.append(filename)
        
print (filenames_dst)

def compare(name1, name2):
    r = re.compile(r'(\d+)')
    id1 = r.search(name1)
    id2 = r.search(name2)
    print('compare1',id1.group(1),id2.group(1),string.atoi(id1.group(1)) < string.atoi(id2.group(1)))
    if (string.atoi(id1.group(1)) < string.atoi(id2.group(1))):
        return 1
    return 0

def compare2(name1, name2):
    r = re.compile(r'(\d+)')
    id1 = r.search(name1)
    id2 = r.search(name2)
    print('compare2',id1.group(1),id2.group(1),string.atoi(id1.group(1)) < string.atoi(id2.group(1)))
    if (string.atoi(id1.group(1)) >= string.atoi(id2.group(1))):
        return 1
    return 0

def sortlist(list):
    listend = len(list) - 1
    print listend
    for i in range(0,listend + 1):
        for j in range(i+1,listend + 1):
            #print(i,j,'hi')
            if(not compare(list[i],list[j])):
               temp = list[i]
               list[i] = list[j]
               list[j] = temp
               
def qsort1(list):
    if list == []:
        return []
    else:
        pivot = list[0]
        print pivot
        print [x for x in list[1:] if compare(x,pivot)]
        lesser = qsort1([x for x in list[1:] if compare(x,pivot)])
        print 'hi'
        greater = qsort1([ x for x in list[1:] if (compare2(x,pivot))])

        print 'return:', lesser + [pivot] + greater
        return lesser + [pivot] + greater

def qsort2(list):
    if list == []: 
        return []
    pivot = list[0]
    print pivot
    #print [x for x in list[1:] if compare(x,pivot)]
    l = qsort2([x for x in list[1:] if x < pivot])
    u = qsort2([x for x in list[1:] if not x < pivot])
    return l + [pivot] + u

filenames_dst = qsort1(filenames_dst)

#print (qsort2([1,10,2]))

#print(filenames_dst)


'''
i = 0;
for filename in filenames_dst:
    print(filename,filenames_src[i]+'.'+'mp4')
    os.rename(filename,filenames_src[i]+'.'+'mp4')
    i = i + 1
'''




'''
for filename in filenames:					# 遍历目录中内容，进行重命名操作
	# 判断当前路径是否为文件，并且不是“rename.py”
	if filename != "rename.py" and os.path.isfile(filename):
		name = str(i)					# 将i转换成字符
		#print name
		name = PadLeft(name,length,'0')	# 将name补全到指定长度
		#print name
		t = filename.split('.')				# 分割文件名，以检查其是否是所要修改的类型
		m = len(t)
		if format == '':					# 如果未指定文件类型，则更改当前目录中所有文件
			os.rename(filename,perfix+name+'.'+t[m-1])
		else:							# 否则只修改指定类型
			if t[m-1] == format:
				os.rename(filename,perfix+name+'.'+t[m-1])
			else:
				
	else:
'''

