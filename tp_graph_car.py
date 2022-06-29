from tkinter import *
import math
import random
import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from vincent.colors import brews
# for filename in ['RESSOURCES NETYPAREO\dataset_voitures.xls']:
#     print("\n")
#     data = pd.read_excel(filename, sheet_name='voitures')
#     print(filename, data.min())

for filename in glob.glob('RESSOURCES NETYPAREO\dataset_voitures.xls'):
    data = pd.read_excel(filename)
    df = pd.read_excel(filename, usecols="B, D, E")
    # print(filename, data['Modele'])
    print(df['Modele'])



# # Les listes des abscisses et ordonnées :
y=df['Modele']
x= sorted(df['Puissance'])

plt.figure(figsize=(10,10))
# On dessine le nuage de points : 
plt.plot(x, y,"o")
plt.show()

# plt.style.use('seaborn')
# plt.scatter(df['Modele'], df['Puissance'],marker="*",s=1000,edgecolors="black",c="yellow")
# plt.title("Excel sheet to Scatter Plot")
# plt.show()

