from tkinter import *

fenetre = Tk()

# écran de jeu
hauteur = 1080
largeur = 1920
canvas = Canvas(fenetre, width=largeur, height=hauteur, bg='black')
canvas.pack()

# balle

# spawn au milieu de l'écran 

balle = canvas.create_oval(largeur / 2, hauteur / 2, largeur / 2, hauteur / 2, fill='white')

fenetre.mainloop()
