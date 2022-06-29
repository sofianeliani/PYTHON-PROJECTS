# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:29:02 2021

@author: bebo
"""
from pylab import * 
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,2000)

y1 =x**3
y2 =-(x**2) # signe -

plt.plot(x, y1,"r")

plt.plot(x,y2,"turquoise")

plt.plot(y2,x,"green") ## rotation
axis ("equal")
plt.show()



