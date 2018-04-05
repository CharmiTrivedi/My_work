#! /usr/bin/python

import sys
import re

index = {}
for line in stdin:
        word, title = line.split('\t')
        index.setdefault(word, {})
        for title in title.split(','):
                doc_id, count = title.split(':')
                count = int(count)
                index[word].setdefault(doc_id, 0)
                index[word][doc_id] += count

for word in index:
        title_list = ["%s:%d" % (doc_id, index[word][doc_id])
                         for doc_id in index[word]]
        title = ','.join(title_list)
        print('%s\t%s' % (word, title))
