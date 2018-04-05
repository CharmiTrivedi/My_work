#!/usr/bin/env python
import sys
import re
import os
import string

if __name__=="__main__":
    filename = os.environ['map_input_file']
    filename = filename.split('/')[-1]

    for line in sys.stdin:
        line = line.lower()
        line = line.split()
        for word in line:
            word = word.strip()
            word = word.translate(None, string.punctuation)
            if len(word) > 1:
                sys.stdout.write("{0} \t {1}".format(word,filename))
