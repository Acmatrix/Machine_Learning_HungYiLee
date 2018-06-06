# -*- coding: utf-8 -*-
content=open("words.txt").read()
array=content.split(" ")
orderindex=0
for i in range(len(array)):
    if array.index(array[i])==i:
        print("%s %s %s"%(array[i],orderindex,array.count(array[i])))
        orderindex=orderindex+1