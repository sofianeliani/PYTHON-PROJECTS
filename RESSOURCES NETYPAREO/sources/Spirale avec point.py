# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:27:25 2021

@author: bebo
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # Fonction pour la 3D
import numpy as np

# Tableau pour les 3 axes
# Création d'un tableau de 100 points entre -4*pi et 4*pi
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)  # Création du tableau de l'axe z entre -2 et 2
r = z**2 + 1
x = r * np.sin(theta)  # Création du tableau de l'axe x
y = r * np.cos(theta)  # Création du tableau de l'axe y

# Tracé du résultat en 3D
fig = plt.figure()
ax = fig.gca(projection='3d')  # Affichage en 3D
ax.scatter(x, y, z, label='Courbe', marker='d')  # Tracé des points 3D
plt.title("Points 3D")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()