#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:33:58 2018

@author: d4rkmatter
"""

import sys

previous = None
running_sum = 0

for line in sys.stdin:
    key, value = line.split('\t')
    
    if key != previous:
        if previous is not None:
            print(str(running_sum)+ '\t')
        previous = key
        running_sum = 0
        
    running_sum = running_sum + int(value)
    
print(str(running_sum)+'\t'+previous)