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


def lancer_jeu():
    menu_principal.withdraw()
    jouer()
    

# Menu Principal

menu_principal.title("Pong")

texte_titre = Label(menu_principal, text='PONG')
btn_jouer = Button(menu_principal, text ='JOUER', command=lancer_jeu, bg = 'green', width = 12)
btn_quitter = Button(menu_principal, text='Quitter', command=menu_principal.destroy, bg = "red", width=12)

texte_titre.place(relx = 0.5, rely = 0.45, anchor = CENTER)
btn_jouer.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn_quitter.place(relx = 0.5, rely = 0.55, anchor = CENTER)
menu_principal.mainloop()
