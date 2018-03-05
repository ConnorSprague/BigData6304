#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

previous = None
running_sum = 0

for line in sys.stdin:
    key, value = line.split('\t')
    
    
    if key != previous:
        if previous is not None:
            print(str(running_sum) + '\t' + previous)
        previous = key
        running_sum = 0
        
    running_sum += int(value)
    
print(str(running_sum)+'\t'+previous)
