#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 1 for ABE 651
Due 1-24-19

Excercises from ThinkPython2
@author: wagne216
"""

# Exercise 3.2, parts 1-4 (p.27)- goal: create & test a function

# 1 test existing example
def do_twice(f): #create function that repeats an input function
    f()
    f()
    
def print_spam(): # print string input 'spam' 
    print('spam')

do_twice(print_spam) # print "spam" twice

# 2 modify do_twice to include 2 arguments (inputs)
def do_twice(function, input): #create function that still repeats an input function
    function(input) 
    function(input)

# command
do_twice(print,'spam')  
 
# 3 Copy print_twice, from ThinkPython2 pg 21
def print_twice(bruce):
    print(bruce) # prints whatever the input is,in this case it is bruce
    print(bruce)
    
# 4 Use #2 to call #3 twice, with 'spam' as an argument
# command: 
do_twice(print_twice,'spam')