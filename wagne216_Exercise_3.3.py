#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 1 for ABE 651
Due 1-24-19

Excercises from ThinkPython2
@author: wagne216
"""

# Exercise 3.3, (p.27)- goal: create grid via function
# 1. Version 1 recreate 2x2 grid from p. 27 in thinkPython2
def do_twice(f): #create function that repeats an input function
    f()
    f()
    
def do_thrice(f)
    f()
    f()
    f()
    
def print_mult(a,b,c,d) #print up to 4 arguments in succession
    print(a)
    print(b)
    print(c)
    print(d)
    
def create_grid_tbt(n):
    print('+',4*'- ','+',4*'- ','+')

    print('|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|')

    print('+',4*'- ','+',4*'- ','+')

    print('|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|')

    print('+',4*'- ','+',4*'- ','+')

#command: 
    create_grid(1)
    
# 2 Version 1. draw 4x4 grid 
def create_grid_fbf(n):
    print('+',4*'- ','+',4*'- ','+',4*'- ','+',4*'- ','+')

    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')

    print('+',4*'- ','+',4*'- ','+',4*'- ','+',4*'- ','+')

    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')

    print('+',4*'- ','+',4*'- ','+',4*'- ','+',4*'- ','+')

    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')

    print('+',4*'- ','+',4*'- ','+',4*'- ','+',4*'- ','+')

    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')
    print('|', 8*' ','|', 8*' ','|', 8*' ','|', 8*' ','|')

    print('+',4*'- ','+',4*'- ','+',4*'- ','+',4*'- ','+')

#1 Version 2- improved 2x2 (shortened): 
# define4 different building blocks to grid:
a = "+ - - - - +" 
b = "|         |"
c = " - - - - +"
d = "         |"

def create_grid(n): # n specifiesno. of rows and col's (square)
    print(a+c*(n-1)) # row with plus and minuses
    print(b+d*(n-1)) # row with only vert lines, spaces
    print(a+c*(n-1))
    print(b+d*(n-1))
    print(a+c*(n-1))

# execute: 
    create_grid(2)
    
# 2 Version 2-improved 4x4 (shortened):
def create_grid(n): # n specifies no. of rows and col's (square)
    print(a+c*(n-1)) # row with plus and minuses
    print(b+d*(n-1)) # row with only vert lines, spaces
    print(a+c*(n-1))
    print(b+d*(n-1))
    print(a+c*(n-1))
    print(b+d*(n-1))
    print(a+c*(n-1))
    print(b+d*(n-1))
    print(a+c*(n-1))

# execute: 
    create_grid(4)
