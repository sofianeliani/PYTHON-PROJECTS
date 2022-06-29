# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:37:28 2022

@author: BEBO
"""
import time
import math
import numpy as np
import matplotlib.pyplot as plt

#x=np.linspace(-1,1,num=100)
#for x in (np.linspace(0,1,10)):
for x in range (30): 
    print("x ",x)
    
    y1 = math.exp(x)
    print(" y1 ",y1)
    
    plt.plot(x, y1,"r--")
    plt.show()
    time.sleep(0.5)
print("\n")

#for x in (np.linspace(0,1,10)):
for x in range (30):
    if x!=0 :
        y2 = 1/x
        print(y2)
        plt.plot(x, y2,"b")
        plt.show()
        time.sleep(0.5)
print("\n")
 
#for x in (np.linspace(0,1,10)): 
for x in range (30):
    y3 = math.log(x)
    print(y3)
    plt.plot(x, y3,"g")
    plt.show()
    time.sleep(0.5)
    

