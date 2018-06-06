# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:10:36 2018

@author: bisheng
"""
inputfile=open('words.txt','r')
message=inputfile.read()
array=message.split(' ')
d = dict()
l=list()
for i in range(len(array)):
    if array[i] in d:
        d[array[i]]=d[array[i]]+1
    else:
        d[array[i]]=1
        l.append(array[i])
inputfile.close()
output=open('result.txt','w')
for i in range(len(l)):
    tem= str(i)+' '+l[i]+' '+str(d[l[i]])+'\n'
    print(tem)
    output.write(tem)
output.close()
    
    