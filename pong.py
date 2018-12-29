from tkinter import *


fenetre = Tk()

# écran de jeu
hauteur = 1080
largeur = 1920
canvas = Canvas(fenetre, width=largeur, height=hauteur, bg='black')

# balle

t_balle = 30
mouv = -1
# spawn au milieu de l'écran 

balle = canvas.create_oval(largeur / 2 - t_balle, hauteur / 2 - t_balle, largeur / 2 + t_balle, hauteur / 2 + t_balle, fill='white')

# faire bouger la balle

direction_x = 0
direction_y = 0
def mouvement_balle():
    pass

    
canvas.pack()
fenetre.mainloop()
