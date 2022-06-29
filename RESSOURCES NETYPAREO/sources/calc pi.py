# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:04:10 2021

@author: infob

# pi/4 = (1/1) -(1/3) + (1/5) -(1/7 ) ....
"""
import math
nbtour = 19000000

def pi(nbtour) :
    pi = 0
    for i in range(nbtour) :
        pi += float( 4 * ((-1) ** i) / ((2 * i) +1))
    print(pi)
    print(math.pi)
# pi = 3,141 592 653 589 793 238 462 643 383 279

#nbtour = int(input('entrez le nombre de tour \n'))

pi(nbtour)
