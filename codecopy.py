# -*- coding:utf-8 -*-
import os
filenames = os.listdir(os.curdir)
print (filenames)
outputfile = "output.txt"
output = open(outputfile,"w")
for filename in filenames:
  if filename != "codecopy.py" and filename != outputfile and filename[-1] != '~' and os.path.isfile(filename):
    print (filename)
    sourcecode = open(filename,"r")
    output.write('///////')
    output.write(filename)
    output.write("\n")
    output.write(sourcecode.read())
    output.write("\n\n")
