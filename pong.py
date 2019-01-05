from tkinter import *
from random import randint
from random import uniform
from random import choice
import time
import tkinter.ttk as ttk

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
fenetre_jeu.withdraw()
# balle

t_balle = 30

# spawn au milieu de l'écran 

balle = canvas_jeu.create_oval(largeur / 2 - t_balle, hauteur / 2 - t_balle, largeur / 2 + t_balle, hauteur / 2 + t_balle, fill='white')

# faire bouger la balle + rebondir + victoir

score = canvas_jeu.create_text(largeur / 2 - 3, 40, text= '0   0', fill = 'white', font = ('Arial', 50, 'bold'))
message_victoire = canvas_jeu.create_text(-1, -1, text= '', fill = 'white', font = ('Arial', 100, 'bold'))

def deplacement_balle():

    points_pour_gg = int(saisie_pts.get())
    vitesse_depart = saisie_vitesse.get()

    if vitesse_depart == 'Très lent':
        vitesse_depart = 1
    elif vitesse_depart == 'Lent':
        vitesse_depart = 2
    elif vitesse_depart == 'Moyen':
        vitesse_depart = 3
    else:
        vitesse_depart = 4


    vitesse_x = choice([-vitesse_depart, vitesse_depart])
    vitesse_y = choice([-vitesse_depart, vitesse_depart])
    
    jeu_en_cour = True

    score_j1 = 0
    score_j2 = 0
    gagnant = ''

    points_pour_gg = int(saisie_pts.get())
    
    canvas_jeu.itemconfigure(score, text = str(score_j1) + '   ' + str(score_j2))


    while jeu_en_cour == True :

        canvas_jeu.move(balle, vitesse_x, vitesse_y)
        position_balle = canvas_jeu.coords(balle) #[gauche, haut, droite, bas] 
        position_raquette_1 = canvas_jeu.coords(raquette_1)
        position_raquette_2 = canvas_jeu.coords(raquette_2)



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

        if position_balle[2] >= largeur:
            canvas_jeu.coords(balle, largeur / 2 - t_balle, hauteur / 2 - t_balle, largeur / 2 + t_balle, hauteur / 2 + t_balle)
            score_j1 += 1
            canvas_jeu.itemconfigure(score, text = str(score_j1) + '   ' + str(score_j2))
            if score_j1 >= points_pour_gg:
                gagnant = 'Joueur 1'
                canvas_jeu.itemconfigure(message_victoire, text = 'Victore du ' + gagnant)
                canvas_jeu.coords(message_victoire, largeur / 2, hauteur / 2)
                canvas_jeu.coords(balle, -1, -1, -1, -1)
                fenetre_jeu.update()
                time.sleep(5)
                canvas_jeu.coords(message_victoire, -100, -100)
                canvas_jeu.coords(balle, largeur / 2 - t_balle, hauteur / 2 - t_balle, largeur / 2 + t_balle, hauteur / 2 + t_balle)
                canvas_jeu.coords(raquette_1, 15, hauteur / 2 - t_raquette, 30, hauteur / 2 + t_raquette)
                canvas_jeu.coords(raquette_2, largeur-15, hauteur / 2 - t_raquette, largeur-30, hauteur / 2 + t_raquette)
                menu_principal.wm_deiconify()
                fenetre_jeu.withdraw()
                jeu_en_cour = False

        elif position_balle[0] <= 0:
            canvas_jeu.coords(balle, largeur / 2 - t_balle, hauteur / 2 - t_balle, largeur / 2 + t_balle, hauteur / 2 + t_balle)
            score_j2 += 1
            canvas_jeu.itemconfigure(score, text = str(score_j1) + '   ' + str(score_j2))
            if score_j2 >= points_pour_gg:         
                gagnant = 'Joueur 2'
                canvas_jeu.itemconfigure(message_victoire, text = 'Victore du ' + gagnant)
                canvas_jeu.coords(message_victoire, largeur / 2, hauteur / 2)
                canvas_jeu.coords(balle, -1, -1, -1, -1)
                fenetre_jeu.update()
                time.sleep(5)
                canvas_jeu.coords(message_victoire, -100, -100)
                canvas_jeu.coords(balle, largeur / 2 - t_balle, hauteur / 2 - t_balle, largeur / 2 + t_balle, hauteur / 2 + t_balle)
                canvas_jeu.coords(raquette_1, 15, hauteur / 2 - t_raquette, 30, hauteur / 2 + t_raquette)
                canvas_jeu.coords(raquette_2, largeur-15, hauteur / 2 - t_raquette, largeur-30, hauteur / 2 + t_raquette)
                menu_principal.wm_deiconify()
                fenetre_jeu.withdraw()
                jeu_en_cour = False

        fenetre_jeu.update()
        time.sleep(0.01)

    

def lancer_parametre():
    fenetre_parametre.wm_deiconify()
    menu_principal.withdraw()
    

def retour():
    menu_principal.wm_deiconify()
    fenetre_parametre.withdraw()


def lancer_jeu():
    fenetre_jeu.wm_deiconify()
    fenetre_parametre.withdraw()

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
btn_jouer = Button(menu_principal, text ='JOUER', command=lancer_parametre, bg = 'green', width = 12)
btn_quitter = Button(menu_principal, text='Quitter', command=menu_principal.destroy, bg = "red", width=12)

texte_titre.place(relx = 0.5, rely = 0.45, anchor = CENTER)
btn_jouer.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn_quitter.place(relx = 0.5, rely = 0.55, anchor = CENTER)

# rejouer

fenetre_rejouer = Toplevel(menu_principal)
fenetre_rejouer.geometry("500x500+720+270")
fenetre_rejouer.title("Pong")


texte_rejouer = Label(fenetre_rejouer, text='Rejouer ?')

texte_rejouer.place(relx = 0.5, rely = 0.30, anchor = CENTER)


# paramètres

def test():
    print(saisie_vitesse.get())

fenetre_parametre = Toplevel(menu_principal)
fenetre_parametre.attributes('-fullscreen',True )

fenetre_parametre.title("Pong")

texte_parametre = Label(fenetre_parametre, text='Paramètres du jeu')
texte_pts = Label(fenetre_parametre, text='Nombre de points pour gagner :')
texte_vitesse = Label(fenetre_parametre, text='Vitesse de la balle en début de partie :')

saisie_pts = Entry(fenetre_parametre, width= 3)

choix_vitesse = ['Très lent', 'Lent', 'Moyen', 'Rapide']
saisie_vitesse = ttk.Combobox(fenetre_parametre, values = choix_vitesse, width = 9)




valider_pts = Button(fenetre_parametre, text ='Valider', command=test)
btn_jouer_2 = Button(fenetre_parametre, text ='JOUER', command=lancer_jeu, bg = 'green', width = 12)
btn_retour = Button(fenetre_parametre, text='Retour', command=retour, bg = "red", width=12)

texte_parametre.place(relx = 0.5, rely = 0.45, anchor = CENTER)
texte_pts.place(relx = 0.35, rely = 0.6, anchor = CENTER)
texte_vitesse.place(relx = 0.35, rely = 0.65, anchor = CENTER)

saisie_pts.place(relx = 0.41, rely = 0.6, anchor = CENTER)
saisie_vitesse.place(relx = 0.43, rely = 0.65, anchor = CENTER)

btn_jouer_2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn_retour.place(relx = 0.5, rely = 0.55, anchor = CENTER)
valider_pts.place(relx = 0.45, rely = 0.6, anchor = CENTER)



fenetre_parametre.withdraw()

fenetre_parametre.mainloop()
fenetre_rejouer.mainloop()
menu_principal.mainloop()


