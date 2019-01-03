from tkinter import *
from random import randint
from random import uniform
from random import choice
import time


# Jeux

fenetre_jeu = Tk()

# écran de jeu
hauteur = 1012
largeur = 1920

canvas_jeu = Canvas(fenetre_jeu, width=largeur, height=hauteur, bg='black')
fenetre_jeu.title("Pong")

canvas_jeu.pack()

# balle

t_balle = 30

# spawn au milieu de l'écran 

balle = canvas_jeu.create_oval(largeur / 2 - t_balle, hauteur / 2 - t_balle, largeur / 2 + t_balle, hauteur / 2 + t_balle, fill='white')

# faire bouger la balle + rebondir



def jouer():

    vitesse_x = choice([-1, 1])
    vitesse_y = choice([-1, 1])

    while True:

        canvas_jeu.move(balle, vitesse_x, vitesse_y)
        position = canvas_jeu.coords(balle) #[gauche, haut, droite, bas] 


        if position[2] >= largeur or position[0] <= 0:
            vitesse_x = -vitesse_x
        if position[3] >= hauteur or position[1] <= 0:
            vitesse_y = -vitesse_y

        fenetre_jeu.update()
        time.sleep(0.01)

        print(position)




# Menu Principal

menu_principal = Tk()


canvas_menu = Canvas(menu_principal, width=largeur, height=hauteur, bg='black')
menu_principal.title("Pong")

btn_jouer = Button(menu_principal, text ='JOUER', command=jouer)
btn_quitter = Button(menu_principal, text='Quitter', command=menu_principal.destroy,bg = "grey", width=12)
canvas_menu.grid(row = 0, column = 0, columnspan =3)

btn_jouer.grid(row = 1, column = 2)
btn_quitter.grid(row = 2, column = 2)
menu_principal.mainloop()
