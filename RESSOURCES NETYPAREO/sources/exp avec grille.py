# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:23:32 2022

@author: BEBO
"""

import matplotlib.pyplot as plt
import numpy as np

x_min = 0
x_max = 10.0

x = np.arange(x_min, x_max, .01)
y = np.exp(x)

plt.plot(x,y)

plt.xlim(x_min,x_max)
plt.ylim(np.exp(x_min),np.exp(x_max))

plt.grid(True,which="both", linestyle='--')

plt.title('How to add a grid on a figure in matplotlib ?', fontsize=8)

plt.savefig("matplotlib_grid_03.png", bbox_inches='tight')
plt.show()
plt.close()