# -*- coding: utf-8 -*-
"""
Created on Sun May 30 15:27:05 2021

@author: bebo
"""

from tkinter import *
import math
import random
import time

################

def rotation_ligne(AutreCanvas, x0, y0, longueur, angle, couleur):

    angle = math.radians(angle) # math.radians permet de convertir en radians

    xf = int(x0+longueur*math.cos(angle))

    yf = int(y0+longueur*math.sin(angle))

    AutreCanvas.create_line(x0, y0, xf, yf, width=2, fill=couleur, dash=(4, 4))
########################
    
def etoile(AutreCanvas, x0, y0, couleur) :
     for angle in range(0,361,20) :

        rotation_ligne(AutreCanvas, x0, y0, random.randint(50,100), angle, couleur)
        
##########################
        
def etoile_aleatoire(AutreCanvas, couleur) :
    if couleur == "alea" :

        liste_couleurs = ['red','blue','red','cyan', 'green']

        couleur = random.choice(liste_couleurs)

    x0 = random.randint(50,450)

    y0 = random.randint(50,450)

    etoile(AutreCanvas, x0, y0, couleur)

    print(x0)
    print(y0)
  
####################### main
    
fen_princ = Tk()

fen_princ.title("ESSAI AVEC CANVAS")

fen_princ.geometry("900x900")


monCanvas = Canvas(fen_princ, width=800, height=800, bg='ivory', borderwidth=0, highlightthickness=0)

monCanvas.place(x=50,y=50)

#monCanvas.create_line(x1, y1, x2, y2, width=2, fill="#ff0000")

#monCanvas.create_line(1,1,100,100, width = 5,fill='red')  # width defaut 1 pixel

for i in range(6) :
   etoile_aleatoire(monCanvas, "alea")
 
fen_princ.mainloop()




