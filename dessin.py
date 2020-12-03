import tkinter as tk
import random 

def choixCouleur ():
    global couleur
    couleur = input("choisissez une couleur ")

def dessineCercle ():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint (0, CANVAS_HEIGHT-100)
    canvas.create_oval(x, y, x + 100, y + 100, fill = couleur)

def dessineCarre ():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint (0, CANVAS_HEIGHT-100)
    canvas.create_rectangle(x, y, x + 100, y + 100, fill = couleur)

def dessineCroix ():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint (0, CANVAS_HEIGHT-100)
    canvas.create_line(x, y + 50, x + 100, y + 50, fill = couleur)
    canvas.create_line(x + 50, y, x + 50, y + 100, fill = couleur)

CANVAS_WIDTH, CANVAS_HEIGHT = 900, 600

root = tk.Tk()
root.title("mon dessin")

bouton_carre = tk.Button(root, text = "carré", command = dessineCarre)
bouton_carre.grid(column = 0, row = 2)

bouton_cercle= tk.Button(root, text = "cercle", command = dessineCercle)
bouton_cercle.grid(column = 0, row = 1)

bouton_croix = tk.Button(root, text = "croix", command = dessineCroix)
bouton_croix.grid(column = 0, row = 3)

bouton_couleur = tk.Button(root, text = "quelle couleur choisir", command = choixCouleur)
bouton_couleur.grid(column = 1, row = 0)

canvas = tk.Canvas(root , width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief= "raised", borderwidth = 10) 
canvas.grid (column = 1, row = 1, rowspan = 3, )


root.mainloop()