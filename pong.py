from tkinter import *
from random import randint
from random import uniform
from random import choice
import time

menu_principal = Tk()
menu_principal.attributes('-fullscreen',True )
# Jeux

fenetre_jeu = Toplevel(menu_principal)
fenetre_jeu.attributes('-fullscreen',True )

# écran de jeu
hauteur = 1080
largeur = 1920

canvas_jeu = Canvas(fenetre_jeu, width=largeur, height=hauteur, bg='black')
fenetre_jeu.title("Pong")
canvas_jeu.create_line((largeur/2, 0), (largeur/2, hauteur), fill='white', width= 2, dash = (2, 4))

canvas_jeu.pack()

# balle

t_balle = 30

# spawn au milieu de l'écran 

balle = canvas_jeu.create_oval(largeur / 2 - t_balle, hauteur / 2 - t_balle, largeur / 2 + t_balle, hauteur / 2 + t_balle, fill='white')

# faire bouger la balle + rebondir


def deplacement_balle():

    vitesse_x = choice([-1, 1])
    vitesse_y = choice([-1, 1])

    while True:

        canvas_jeu.move(balle, vitesse_x, vitesse_y)
        position_balle = canvas_jeu.coords(balle) #[gauche, haut, droite, bas] 
        position_raquette_1 = canvas_jeu.coords(raquette_1)
        position_raquette_2 = canvas_jeu.coords(raquette_2)
        print(position_raquette_1)
        print(position_raquette_2)


        if position_balle[2] >= largeur or position_balle[0] <= 0:
            vitesse_x = -vitesse_x
        if position_balle[3] >= hauteur or position_balle[1] <= 0:
            vitesse_y = -vitesse_y
        if position_balle[0] <= position_raquette_1[2] and position_raquette_1[1]<= position_balle[3] and position_raquette_1[3] >= position_balle[1]:
            vitesse_x = -vitesse_x
            vitesse_x += 0.4
            if vitesse_y > 0:
                vitesse_y += 0.4
            else:
                vitesse_y -= 0.4
        if position_balle[2] >= position_raquette_2[0] and position_raquette_2[1]<= position_balle[3] and position_raquette_2[3] >= position_balle[1]:
            vitesse_x = -vitesse_x
            vitesse_x -= 0.4
            if vitesse_y > 0:
                vitesse_y += 0.4
            else:
                vitesse_y -= 0.4

        fenetre_jeu.update()
        time.sleep(0.01)


def lancer_jeu():
    menu_principal.withdraw()
    deplacement_balle()
    

# raqutte
t_raquette = 60
raquette_1 = canvas_jeu.create_rectangle(15, hauteur / 2 - t_raquette, 30, hauteur / 2 + t_raquette, fill='white')
raquette_2 = canvas_jeu.create_rectangle(largeur-15, hauteur / 2 - t_raquette, largeur-30, hauteur / 2 + t_raquette, fill='white')

def deplacement_raquette_1(event):

    position_raquette_1 = canvas_jeu.coords(raquette_1)
    vitesse = -10

    if position_raquette_1[1] > 10.0:
        canvas_jeu.move(raquette_1, 0, vitesse)


def deplacement_raquette_2(event):

    position_raquette_1 = canvas_jeu.coords(raquette_1)
    vitesse = 10

    if position_raquette_1[3] < 1070.0:
        canvas_jeu.move(raquette_1, 0, vitesse)

def deplacement_raquette_3(event):

    vitesse = -10
    position_raquette_2 = canvas_jeu.coords(raquette_2)

    if position_raquette_2[1] > 10.0:
        canvas_jeu.move(raquette_2, 0, vitesse)

def deplacement_raquette_4(event):

    vitesse = 10
    position_raquette_2 = canvas_jeu.coords(raquette_2)

    if position_raquette_2[3] < 1070.0:
        canvas_jeu.move(raquette_2, 0, vitesse)


fenetre_jeu.bind("<Tab>", deplacement_raquette_1)
fenetre_jeu.bind("<Shift_L>", deplacement_raquette_2)
fenetre_jeu.bind("<Up>", deplacement_raquette_3)
fenetre_jeu.bind("<Down>", deplacement_raquette_4)

# Menu Principal

menu_principal.title("Pong")

texte_titre = Label(menu_principal, text='PONG')
btn_jouer = Button(menu_principal, text ='JOUER', command=lancer_jeu, bg = 'green', width = 12)
btn_quitter = Button(menu_principal, text='Quitter', command=menu_principal.destroy, bg = "red", width=12)

texte_titre.place(relx = 0.5, rely = 0.45, anchor = CENTER)
btn_jouer.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn_quitter.place(relx = 0.5, rely = 0.55, anchor = CENTER)

menu_principal.mainloop()
