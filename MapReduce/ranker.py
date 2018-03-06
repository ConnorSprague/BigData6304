#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 18:49:58 2018
Assignment for CompSci 6304 Big Data and Cloud Management

Assignment #1
Simple wordcount with MapReduce

Connor Sprague
Gaurang Rathod
Yogesh Lad
"""

import sys

#Read list of top 10keys
master_key = open('master_key.txt', 'r').read()
master_key = master_key.split('\n')
del master_key[10]
master_key = list(map(lambda x: x.rsplit('\t'), master_key))
for idx in range(0,10):
    master_key[idx] = master_key[idx][1]

with open("output.txt", "a") as myfile:
    myfile.write('The Current Keywords \n')
    for xy in range(0,10):    
        myfile.write(str(master_key[xy])+'\n')
    myfile.write('\nEnd of Keywords \n')

####Word occurence routine
counter_list = [0,0,0,0,0,0,0,0,0,0] #Counters
counter = 0
chapter_count = 0

#Flag holder for output summary


#Read from mapper.py pipe
for line in sys.stdin:
    key, value = line.split('\t')
    #Reset counters when 'CHAPTER' is found in stream
    if key == 'CHAPTER':
        print('=== Chapter '+str(chapter_count)+' ===')
        #write to output.txt occurences of words in each chapter
        with open("output.txt", "a") as myfile:
            myfile.write('=== Chapter '+str(chapter_count)+ ' =====\n')
            for idx1 in range(0,10):
                if counter_list[idx1] != 0:
                    myfile.write('Keyword * '+str(master_key[idx1])+' * appeared '+
                                 str(counter_list[idx1])+' times \n')
                else:
                    myfile.write('Keyword * '+str(master_key[idx1])+' * DOES NOT APPEAR\n')
            myfile.write('\n')
        #reset counters increment chapter
        counter_list = [0,0,0,0,0,0,0,0,0,0]
        chapter_count += 1
    #IF key is in list of top words, find index of keyword and increment its counter
    elif key in master_key:
        index = master_key.index(str(key))
        counter_list[index]+=1
        print('Chapter '+str(chapter_count)+'  keyword: '+str(master_key[index])+
              '  occurence '+str(counter_list[index]))
        
#Account for last chapter not having terminating 'CHAPTER' String

#write to output.txt occurences of words in each chapter
with open("output.txt", "a") as myfile:
    myfile.write('=== Chapter '+str(chapter_count)+ ' =====\n')
    for idx1 in range(0,10):
        if counter_list[idx1] != 0:
            myfile.write('Keyword * '+str(master_key[idx1])+' * appeared '+
                         str(counter_list[idx1])+' times \n')
        else:
            myfile.write('Keyword * '+str(master_key[idx1])+' * DOES NOT APPEAR\n')
    myfile.write('\n')