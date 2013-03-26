# -*- coding:utf-8 -*-
import os
filenames = os.listdir(os.curdir)				# 获得当前目录中的内容
#print (filenames)
for filename in filenames:
        if filename != "getfilename.py" and os.path.isfile(filename):
                print(filename)
