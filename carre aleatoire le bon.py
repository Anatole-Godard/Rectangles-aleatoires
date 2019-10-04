from tkinter import *
import random

def color_aleatoire():
    "Changement aléatoire de la couleur du tracé"
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow','#ffd800','pink']
    c = random.randint(0,9)         # => génère un nombre aléatoire de 0 à 9
    return pal[c]
  
tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg=color_aleatoire())
canvas.pack()

def cercle_aleatoire(h_g, b_d, coul):
    x1 = random.randrange(h_g)
    y1 = random.randrange(b_d)
    x2 = x1 + random.randrange(h_g)
    y2 = y1 + random.randrange(b_d)
    canvas.create_oval(x1, y1, x2, y2, fill=coul)

def rectangle_aleatoire(largeur, hauteur, coul):
    x1 = random.randrange(largeur)
    y1 = random.randrange(hauteur)
    x2 = x1 + random.randrange(largeur)
    y2 = y1 + random.randrange(hauteur)
    canvas.create_rectangle(x1, y1, x2, y2, fill=coul)

for x in range(0, 30):
    rectangle_aleatoire(400, 400, color_aleatoire())
    cercle_aleatoire(400, 400, color_aleatoire())   

