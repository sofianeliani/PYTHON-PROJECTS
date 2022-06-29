# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:29:02 2021

@author: bebo
"""
import math
import time
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,num=100)
y1 =x*x
plt.plot(x, y1,"g--")
plt.show()
time.sleep(0.5)
plt.plot(y1,x)
plt.show()
time.sleep(0.5)
y2 =-(x*x)
plt.plot(x,y2)
plt.show()
time.sleep(0.5)
plt.plot(y2,x)
plt.show()
time.sleep(0.5)
  
for k in range (2):
    
    plt.plot(x, y1,"r--")
    plt.plot(y1,x)
    plt.show()
    time.sleep(0.5)
   
    plt.plot(x,y2)
    plt.plot(y2,x)
    plt.show()
    time.sleep(0.5)
    k+=k
     
plt.plot(x, y1,"r--") 
plt.plot(y1,x)
plt.plot(x,y2)
plt.plot(y2,x)
plt.show()
time.sleep(0.5)

x = np.linspace( -1,1,100) 
plt.plot(x, y1,"r--")
y4 = np.sin(10*x)*y1
plt.plot(x,y4)
plt.show()
time.sleep(2)

x = np.linspace( -2,5,100) 
y4 = np.sin(10*x)*y1
plt.plot(x,y4)
plt.show()
