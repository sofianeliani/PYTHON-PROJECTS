# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:31:42 2021

@author: bebo
"""
from pylab import * 
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D

#x=np.linspace(-2,2,200)

# x^2 + y^2 = z^2 tg^2 (angle)
#Creation de la spirale
for i in range(100) :
    theta = np.linspace(-4 * np.pi, 4 * np.pi, i)
    zc = np.linspace(-2, 0, i)  # Création du tableau de l'axe z entre -2 et 2
    rc = zc**2 + 1
    xc = rc * np.sin(theta)  # Création du tableau de l'axe x
    yc = rc * np.cos(theta)  # Création du tableau de l'axe y
    
# Creation de la sphere
r = 1
pi = np.pi
cos = np.cos
sin = np.sin
phi, teta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
x = r*sin(phi)*cos(teta)
y = r*sin(phi)*sin(teta)
z = r*cos(phi)   
    
# Tracé de la spirale en 3D
fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')  # Affichage en 3D
ax1.plot(xc, yc, zc)  # Tracé de la courbe 3D
   # plt.title("Courbe 3D")
   #ax.set_xlabel('X')
   # ax.set_ylabel('Y')
   # ax.set_zlabel('Z')
   #plt.tight_layout()
time.sleep(1)

#Set colours and render
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    x, y, z,  rstride=1, cstride=1, color='pink', alpha=0.6, linewidth=0)

ax.scatter(x,y,z,color="lightcyan",s=20)

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])
ax.set_aspect("auto")
#plt.tight_layout()
plt.show()