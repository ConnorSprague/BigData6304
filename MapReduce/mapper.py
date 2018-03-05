#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:18:06 2018

@author: d4rkmatter
"""

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #regex remove non alpha numeric or space
    line = re.sub('[^0-9a-zA-Z ]+', '', line)
    
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        #words to ignore
        ignore = ['and', 'or', 'the', 'but', 'for', 'if',
                  'to', 'you','a','of','I','it','in',
                  'she','was','that','as','on','at',
                  'all','so','with','had','be','is','The']
        if word not in ignore:
            print('%s\t%s' % (word, 1))