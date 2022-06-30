# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:45:28 2022

@author: infob
"""
# https://allophysique.com/posts/python/python-labyrinthe/


from numpy.random import randint
import matplotlib.pyplot as plt

# On définit une class Pile
class Pile:
    # L'état de notre objet courant est initialisé avec un tableau vide
    def __init__(self):
        self.lst = [] 
    # On retourne une valeur à vide à notre objet
    def empty(self):
        return self.lst == [] 
    # On implémente l'état actuel de notre objet avec un paramètre X (qui peut être vu comme une coordonnée)
    def push(self, x):
        self.lst.append(x)
    # Enlève de la liste un élément situé à la position indiquée et le renvoie en valeur de retour.
    def pop(self):
        if self.empty():
            raise ValueError("pile vide") 
        return self.lst.pop()
# adapte le parcour défini par un trait rouge à la forme du labyrinthe   
def explorer(laby): 
    # On instancie une variable de type Pile()
    pile = Pile()
    # On implémente un élément à notre pile qui correspond au coordonnées et au paramètre laby passé à l'appel de la fonction
    pile.push((0, laby.q - 1)) 
    # on défini l'état à Faux pour une certaine coordonnée du tableau
    laby.tab[0][laby.q - 1].etat = False 
    # Tant que le programme continu on continu la boucle afin que notre trait rouge ne traverse pas les autres formes et suive le chemin du labyrinthe
    while True:
        i, j = pile.pop()
        if i == laby.p - 1 and j == 0:
            break
        if j > 0 and laby.tab[i][j].S and laby.tab[i][j-1].etat:
            pile.push((i, j)) 
            pile.push((i, j-1)) 
            laby.tab[i][j-1].etat = False
        elif i < laby.p-1 and laby.tab[i][j].E and laby.tab[i+1][j].etat: 
            pile.push((i, j))
            pile.push((i+1, j))
            laby.tab[i+1][j].etat = False
        elif j < laby.q-1 and laby.tab[i][j].N and laby.tab[i][j+1].etat: 
            pile.push((i, j))
            pile.push((i, j+1))
            laby.tab[i][j+1].etat = False
        elif i > 0 and laby.tab[i][j].W and laby.tab[i-1][j].etat: 
            pile.push((i, j))
            pile.push((i-1, j))
            laby.tab[i-1][j].etat = False
    return pile.lst

# On définit une classe Case
class Case:
    # On initialise la valeur de l'instance courante de l'objet avec des booléens (Faux par défaut)
    def __init__(self):
        self.N = False 
        self.W = False 
        self.S = False 
        self.E = False 
        self.etat = False

# On définit une classe Labyrinthe
class Labyrinthe:
    # On défini une fonction pour adapter la taille du loby (taille de la fenêtre)
    def __init__(self, p, q): # taille du laby
        self.p = p
        self.q = q
        # On créer le même espacement entre les formes peut importe la taille du lobby
        self.tab = [[Case() for j in range(q)] for i in range(p)]
    # On définit une fonction Show pour simplement afficher les bonnes formes à la bonne place (les traits)
    def show(self):
        # On affiche le cadre bleu autour du labyrinth
        plt.plot([0, 0, self.p, self.p, 0], [0, self.q, self.q, 0, 0], linewidth=2) 
        for i in range(self.p-1):
            for j in range(self.q):
                if not self.tab[i][j].E:
                    plt.plot([i+1, i+1], [j, j+1], 'b') 
        for j in range(self.q-1):
            for i in range(self.p):
                if not self.tab[i][j].N:
                    plt.plot([i, i+1], [j+1, j+1], 'b') 
        # On fait en sorte que la taille du labyrinth avec ses formes soit cohérentes. 
        # Enlever cette ligne et le labyrinth prendra la taille du loby peut importe les paramètres passés
        plt.axis([-1, self.p+1, -1, self.q+1])
        plt.show()

    # On définit une fonction solution afin d'afficher en rouge le parcour à faire du labyrinth 
    def solution(self):
        # Ici explorer : va nous permettre d'afficher la solution (en rouge) sans traverser les autres traits
        sol = explorer(self) 
        X, Y = [], []
        for (i, j) in sol:
            X.append(i+.5)
            Y.append(j+.5) 
        X.append(self.p-.5)
        Y.append(.5)
        plt.plot(X, Y, 'r', linewidth=2) 
        self.show()
# On définit une fonction creation afin de créer le labyrinth dans son ensemble avec la taille comprise du labyrinth en paramètre
def creation(p, q):
    # laby initialise un objet de type Labyrinthe avec des paramètres de taille
    laby = Labyrinthe(p, q)
    # On itialise un objet de type Pile
    pile = Pile()
    # On instancie deux variables de type Intergers avec des valeurs aléatoire
    i, j = randint(p), randint(q)
    print(i)
    print(j)
    # Et on implémente à la pile ces deux valeurs qui serviront à la résolution du labyrinthe
    pile.push((i, j)) 
    # Ce qui fera changer l'état du laby
    laby.tab[i][j].etat = True 
    # boucle si la pile n'est pas vide
    while not pile.empty():
        # on vide nos deux valeurs aléatoires de la pile si aucune valeur n'est spécifié
        i, j = pile.pop()
        v = []
        # en fonction de la forme on défini les points pour résoudre le labyrinthe en les nommants et en les placant sur le bon axe
        if j < q-1 and not laby.tab[i][j+1].etat:
            v.append('N')
        if i > 0 and not laby.tab[i-1][j].etat:
            v.append('W')
        if j > 0 and not laby.tab[i][j-1].etat:
            v.append('S')
        if i < p-1 and not laby.tab[i+1][j].etat:
            v.append('E') 
        if len(v) > 1:
            pile.push((i, j)) 
        if len(v) > 0:
            c = v[randint(len(v))] 
            if c == 'N':
                laby.tab[i][j].N = True
                laby.tab[i][j+1].S = True
                laby.tab[i][j+1].etat = True 
                pile.push((i, j+1))
            elif c == 'W':
                laby.tab[i][j].W = True 
                laby.tab[i-1][j].E = True 
                laby.tab[i-1][j].etat = True 
                pile.push((i-1, j))
            elif c == 'S':
                laby.tab[i][j].S = True 
                laby.tab[i][j-1].N = True 
                laby.tab[i][j-1].etat = True 
                pile.push((i, j-1))
            else:
                laby.tab[i][j].E = True 
                laby.tab[i+1][j].W = True 
                laby.tab[i+1][j].etat = True 
                pile.push((i+1, j))
    return laby

# On initialise le laby avec les paramètres correspondant à la taille du labyrinthe
laby = creation(7, 2)
# On appelle la solution qui affiche notre fenetre et qui résoud le labyrinthe
laby.solution()
