# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:20:58 2021

@author: bebo
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 500) #☻ de -1 à 1

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(-2,2) # de -2 à 2
plt.ylim(-2,2) # de -2 à 2

ax.set_aspect('equal') #même taille x et y

###### cercle y^2 + x^2 = 1

yc = np.sqrt(1-(x**2)) # ne pas utiliser math.sqrt !!!!

plt.plot(x ,yc ,"blue" )
plt.plot( x , -yc, "green" )

# essayez de colorier les surfaces avec différentes couleurs usage de
# fill_between

plt.axhline(y = 0, color = 'black')
plt.axvline(x =0, color = 'cyan')

plt.show()
