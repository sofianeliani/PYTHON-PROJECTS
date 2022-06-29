# -*- coding: utf-8 -*-
"""
Created on Sun May  2 22:05:45 2021

@author: bebo
"""
# http://tkinter.fdex.eu/doc/caw.html#Canvas

from tkinter import *


largeur = 400
hauteur = 200
root = Tk()
canvas = Canvas(root,width = largeur, height = hauteur, background = "white")
canvas.pack(fill = "both",expand = True)
x0,y0 = 100,100
dx = +5
dy = +5

rect = canvas.create_rectangle(x0,y0,x0+20,y0+20,width = 2,fill = "red")

def activer():
     global x0, y0, dx, dy
     x0 = x0 + dx
     y0 = y0 + dy
     
     canvas.coords(rect,x0,y0,x0+20,y0+20)
     
     if x0 < 0 or x0 > largeur:
         dx = -dx
     if y0 < 0 or y0 > hauteur:
         dy = -dy
         
     canvas.after(50,activer) # fait deplacer le carre apres 50 milli seconde
     return
 
def action_activer():
      activer()
      return
  
bouton_couleur = Button(root,text = "activer-accélérer", width = 20, command = action_activer)
bouton_couleur.pack(pady = 10)
 
bouton_quitter = Button(root,text = "Quitter" ,width = 20, command=root.quit)
bouton_quitter.pack(side = BOTTOM,pady = 10)
  
root.mainloop()
 
     
