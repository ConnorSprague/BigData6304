#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 18:49:58 2018

@author: d4rkmatter
"""

import sys

#Read list of top 10keys
master_key = open('master_key.txt', 'r').read()
master_key = master_key.split('\n')
del master_key[10]
master_key = list(map(lambda x: x.rsplit('\t'), master_key))
for idx in range(0,10):
    master_key[idx] = master_key[idx][1]

####Word occurence routine
counter_list = [0,0,0,0,0,0,0,0,0,0] #Counters
counter = 0
chapter_count = 0

#Read from mapper.py pipe
for line in sys.stdin:
    key, value = line.split('\t')
    #Reset counters when 'CHAPTER' is found in stream
    if key == 'CHAPTER':
        print('=== Chapter '+str(chapter_count)+' ===')
        counter_list = [0,0,0,0,0,0,0,0,0,0]
        chapter_count += 1
    #IF key is in list of top words, find index of keyword and increment its counter
    elif key in master_key:
        index = master_key.index(str(key))
        counter_list[index]+=1
        print('Chapter '+str(chapter_count)+'  keyword: '+str(master_key[index])+
              '  occurence '+str(counter_list[index]))
    #Need to save/or clean up words and counts
    #Then Sort by each keyword, on chapter
        