#!/usr/bin/env python
import sys
import os

if __name__=="__main__":
    current_key = None
    word = None
    list1=[]
    for line in sys.stdin:
        word, filename = line.split('\t')
        filename = filename.strip()
	if word == current_key:
	    if filename not in list1:
		list1.append(filename)
	else:
	    if current_key is not None:
		sys.stdout.write("{0}\t{1}\n".format(current_key,list1))
	    current_key=word
	    list1=[]
	    list1.append(filename)
    if current_key:
	sys.stdout.write("{0}\t{1}\n".format(current_key,list1))

