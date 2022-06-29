# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:06:51 2021

@author: infob
"""
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = np.linspace(0,2*np.pi,30)
y = np.cos(x)
plt.plot(x,y)
plt.show()
time.sleep(6)

###########

theta = np.linspace(-4 * np.pi, 4 * np.pi,100)
z = np.linspace(-2,2,100)
r = z**2+1
x = r * np.sin(theta)
y = r * np.cos(theta)
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(x,y,z, label = 'COURBE')
plt.title('Courbe 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tightlayout()
plt.show()