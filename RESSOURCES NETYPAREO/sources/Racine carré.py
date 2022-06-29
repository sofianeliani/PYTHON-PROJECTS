# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:16:09 2021

@author: infob
"""

# y = a*x^2+b*x+c
# delta = b^2 - 4 *a*c
# si delta = 0 x = square(delta) / 2*a
# si delta > 0 x1 = (-b + square(delta)) /2*a et x2 = (-b -square(delta))/ 2*a
# si delta < 0 pas de racine réelle.

import math

a = float(input('entrez a \n'))
b = float(input('entrez b \n'))
c = float(input('entrez c\n'))



delta = float(b**2 - 4*a*c)

print ('delta \n',delta)

if delta == 0 :
    x = -b / 2*a
    print('x \n', x)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a
    print('x1 x2 \n', x1,x2)
if delta <0 :
    print('pas de racine réelle\n')