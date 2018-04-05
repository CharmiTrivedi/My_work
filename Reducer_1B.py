#!/usr/bin/env python
import sys
import csv
import collections

if __name__=="__main__":
    current_key = None
    word = None
    new_dict = {}
    
    for line in sys.stdin:
        line = line.strip()
        word = line.split('\t')[0]
        filename = line.split('\t')[1]
        filename = filename.strip()
        if word in new_dict:
            if filename not in new_dict[word]:
                new_dict[word][filename]=1
            else:
                new_dict[word][filename]+=1
	else:
            new_dict[word] = {}
            new_dict[word][filename]=1
    if current_key == word:
        if word in new_dict :
            if filename not in new_dict[word]:
                new_dict[word][filename]=1
            else:
                new_dict[word][filename]+=1
    else:
        new_dict[word] = {}
        new_dict[word][filename]=1
    for word in new_dict:
        sys.stdout.write("{0}\t{1}\n".format(word,new_dict[word]))

