#!/usr/bin/env python

import sys
import os
if __name__=="__main__":
    for line in sys.stdin:
	words =  line.split()
        filename = os.getenv('map_input_file')
        filename = os.path.split(filename)[-1]
        for word in words:
            sys.stdout.write("{0}\t{1}\n".format(word,filename))
            
            
            

