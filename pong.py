from tkinter import *
from random import randint
from random import uniform
from random import choice
import time
import tkinter.ttk as ttk

menu_principal = Tk()
menu_principal.attributes("-fullscreen", True)
# Jeux

fenetre_jeu = Toplevel(menu_principal)
fenetre_jeu.attributes("-fullscreen", True)

# écran de jeu
hauteur = 1080
largeur = 1920

canvas_jeu = Canvas(fenetre_jeu, width=largeur, height=hauteur, bg="black")
fenetre_jeu.title("Pong")
ligne_separatrice = canvas_jeu.create_line(
    (largeur / 2, 0), (largeur / 2, hauteur), fill="white", width=2, dash=(2, 4)
)

canvas_jeu.pack()
fenetre_jeu.withdraw()
# balle

t_balle = 30

# spawn au milieu de l'écran

balle = canvas_jeu.create_oval(
    largeur / 2 - t_balle,
    hauteur / 2 - t_balle,
    largeur / 2 + t_balle,
    hauteur / 2 + t_balle,
    fill="white",
)

# faire bouger la balle + rebondir + victoir

score = canvas_jeu.create_text(
    largeur / 2 - 3, 40, text="0   0", fill="white", font=("Arial", 50, "bold")
)
message_victoire = canvas_jeu.create_text(
    -1, -1, text="", fill="white", font=("Arial", 100, "bold")
)


def deplacement_balle():

    points_pour_gg = int(saisie_pts.get())
    vitesse_depart = saisie_vitesse.get()

    if vitesse_depart == "Très lent":
        vitesse_depart = 1
    elif vitesse_depart == "Lent":
        vitesse_depart = 2
    elif vitesse_depart == "Moyen":
        vitesse_depart = 3
    else:
        vitesse_depart = 4

    color_bg = saisie_c_bg.get()

    canvas_jeu.itemconfigure(balle, fill=saisie_c_balle.get())
    canvas_jeu.itemconfigure(raquette_1, fill=saisie_c_r1.get())
    canvas_jeu.itemconfigure(raquette_2, fill=saisie_c_r2.get())
    canvas_jeu.configure(bg=color_bg)

    if color_bg == "white":
        canvas_jeu.itemconfigure(ligne_separatrice, fill="black")
        canvas_jeu.itemconfigure(score, fill="black")
        canvas_jeu.itemconfigure(message_victoire, fill="black")

    vitesse_x = choice([-vitesse_depart, vitesse_depart])
    vitesse_y = choice([-vitesse_depart, vitesse_depart])

    jeu_en_cour = True

    score_j1 = 0
    score_j2 = 0
    gagnant = ""

    points_pour_gg = int(saisie_pts.get())

    canvas_jeu.itemconfigure(score, text=str(score_j1) + "   " + str(score_j2))

    boost_balle_x = 1
    boost_balle_y = 1
    boost_raquette = 0

    annuler_bonus = None

    boost_joueur = 0

    effet_jaune = None
    effet_vert = None
    effet_rouge = None

    bouclier_j_1 = 0
    bouclier_j_2 = 0

    lieu_de_spawn_x = 0
    lieu_de_spawn_y = 0

    while jeu_en_cour == True:

        canvas_jeu.move(balle, vitesse_x * boost_balle_x, vitesse_y * boost_balle_y)
        position_balle = canvas_jeu.coords(balle)  # [gauche, haut, droite, bas]
        position_raquette_1 = canvas_jeu.coords(raquette_1)
        position_raquette_2 = canvas_jeu.coords(raquette_2)
        position_bonus_malus_jaune = canvas_jeu.coords(bonus_malus_jaune)
        position_bonus_malus_vert = canvas_jeu.coords(bonus_malus_vert)
        position_bonus_malus_rouge = canvas_jeu.coords(bonus_malus_rouge)

        if position_balle[3] >= hauteur or position_balle[1] <= 0:
            vitesse_y = -vitesse_y

        if len(canvas_jeu.find_overlapping(*position_raquette_1)) > 1:
            vitesse_x = -vitesse_x
            vitesse_x += 0.4
            canvas_jeu.move(balle, vitesse_x + 5, vitesse_y)
            if vitesse_y > 0:
                vitesse_y += 0.4
            else:
                vitesse_y -= 0.4
            boost_joueur = 1
            if bouclier_j_1 == 1:
                canvas_jeu.coords(
                    raquette_1,
                    15,
                    hauteur / 2 - t_raquette,
                    30,
                    hauteur / 2 + t_raquette,
                )
                bouclier_j_1 = 0

        if len(canvas_jeu.find_overlapping(*position_raquette_2)) > 1:
            vitesse_x = -vitesse_x
            vitesse_x -= 0.4
            canvas_jeu.move(balle, vitesse_x - 5, vitesse_y)
            if vitesse_y > 0:
                vitesse_y += 0.4
            else:
                vitesse_y -= 0.4
            boost_joueur = 2
            if bouclier_j_2 == 1:
                canvas_jeu.coords(
                    raquette_2,
                    largeur - 15,
                    hauteur / 2 - t_raquette,
                    largeur - 30,
                    hauteur / 2 + t_raquette,
                )
                bouclier_j_2 = 0

        if boost_balle_x != 1 or boost_balle_y != 1:
            annuler_bonus = randint(0, 1600)
            if annuler_bonus == 888:
                boost_balle_x = 1
                boost_balle_y = 1

        if boost_raquette == 1:
            annuler_bonus = randint(0, 2500)
            if annuler_bonus == 777:
                canvas_jeu.coords(
                    raquette_1,
                    15,
                    hauteur / 2 - t_raquette,
                    30,
                    hauteur / 2 + t_raquette,
                )
                canvas_jeu.coords(
                    raquette_2,
                    largeur - 15,
                    hauteur / 2 - t_raquette,
                    largeur - 30,
                    hauteur / 2 + t_raquette,
                )
                boost_raquette = 0
        if boost_raquette == 2:
            annuler_bonus = randint(0, 2500)
            if annuler_bonus == 666:
                canvas_jeu.coords(
                    raquette_1,
                    15,
                    hauteur / 2 - t_raquette,
                    30,
                    hauteur / 2 + t_raquette,
                )
                canvas_jeu.coords(
                    raquette_2,
                    largeur - 15,
                    hauteur / 2 - t_raquette,
                    largeur - 30,
                    hauteur / 2 + t_raquette,
                )
                boost_raquette = 0

        if position_balle[2] >= largeur:
            canvas_jeu.coords(
                balle,
                largeur / 2 - t_balle,
                hauteur / 2 - t_balle,
                largeur / 2 + t_balle,
                hauteur / 2 + t_balle,
            )
            score_j1 += 1
            canvas_jeu.itemconfigure(score, text=str(score_j1) + "   " + str(score_j2))
            if score_j1 >= points_pour_gg:
                gagnant = "Joueur 1"
                canvas_jeu.itemconfigure(message_victoire, text="Victore du " + gagnant)
                canvas_jeu.coords(message_victoire, largeur / 2, hauteur / 2)
                canvas_jeu.coords(balle, -1, -1, -1, -1)
                fenetre_jeu.update()
                time.sleep(5)
                canvas_jeu.coords(message_victoire, -100, -100)
                canvas_jeu.coords(
                    balle,
                    largeur / 2 - t_balle,
                    hauteur / 2 - t_balle,
                    largeur / 2 + t_balle,
                    hauteur / 2 + t_balle,
                )
                canvas_jeu.coords(
                    raquette_1,
                    15,
                    hauteur / 2 - t_raquette,
                    30,
                    hauteur / 2 + t_raquette,
                )
                canvas_jeu.coords(
                    raquette_2,
                    largeur - 15,
                    hauteur / 2 - t_raquette,
                    largeur - 30,
                    hauteur / 2 + t_raquette,
                )
                fenetre_rejouer.wm_deiconify()
                jeu_en_cour = False

        elif position_balle[0] <= 0:
            canvas_jeu.coords(
                balle,
                largeur / 2 - t_balle,
                hauteur / 2 - t_balle,
                largeur / 2 + t_balle,
                hauteur / 2 + t_balle,
            )
            score_j2 += 1
            canvas_jeu.itemconfigure(score, text=str(score_j1) + "   " + str(score_j2))
            if score_j2 >= points_pour_gg:
                gagnant = "Joueur 2"
                canvas_jeu.itemconfigure(message_victoire, text="Victore du " + gagnant)
                canvas_jeu.coords(message_victoire, largeur / 2, hauteur / 2)
                canvas_jeu.coords(balle, -1, -1, -1, -1)
                fenetre_jeu.update()
                time.sleep(5)
                canvas_jeu.coords(message_victoire, -100, -100)
                canvas_jeu.coords(
                    balle,
                    largeur / 2 - t_balle,
                    hauteur / 2 - t_balle,
                    largeur / 2 + t_balle,
                    hauteur / 2 + t_balle,
                )
                canvas_jeu.coords(
                    raquette_1,
                    15,
                    hauteur / 2 - t_raquette,
                    30,
                    hauteur / 2 + t_raquette,
                )
                canvas_jeu.coords(
                    raquette_2,
                    largeur - 15,
                    hauteur / 2 - t_raquette,
                    largeur - 30,
                    hauteur / 2 + t_raquette,
                )
                fenetre_rejouer.wm_deiconify()
                jeu_en_cour = False

        if len(canvas_jeu.find_overlapping(*position_bonus_malus_jaune)) > 1:
            canvas_jeu.coords(bonus_malus_jaune, 1, 1, 1, 1)
            effet_jaune = choice(
                ["accélère", "décélère", "y_boost", "x_boost", "rebond"]
            )
            if effet_jaune == "accélère":
                boost_balle_x = 1.5
                boost_balle_y = 1.5
            elif effet_jaune == "décélère":
                boost_balle_x = 0.5
                boost_balle_y = 0.5
            elif effet_jaune == "y_boost":
                boost_balle_y = 1.5
            elif effet_jaune == "y_boost":
                boost_balle_x = 1.5
            else:
                vitesse_x = -vitesse_x

        if len(canvas_jeu.find_overlapping(*position_bonus_malus_vert)) > 1:
            canvas_jeu.coords(bonus_malus_vert, largeur, hauteur, largeur, hauteur)
            effet_vert = choice(["grande_raquette", "bouclier"])
            if effet_vert == "grande_raquette":
                if boost_joueur == 1:
                    canvas_jeu.coords(
                        raquette_1, 15, hauteur / 2 - 120, 30, hauteur / 2 + 120
                    )
                    boost_raquette = 1
                elif boost_joueur == 2:
                    canvas_jeu.coords(
                        raquette_2,
                        largeur - 15,
                        hauteur / 2 - 120,
                        largeur - 30,
                        hauteur / 2 + 120,
                    )
                    boost_raquette = 1
                else:
                    pass

            elif effet_vert == "bouclier":
                if boost_joueur == 1:
                    bouclier_j_1 = 1
                    canvas_jeu.coords(
                        raquette_1, 15, hauteur / 2 - hauteur, 30, hauteur / 2 + hauteur
                    )
                elif boost_joueur == 2:
                    bouclier_j_2 = 1
                    canvas_jeu.coords(
                        raquette_2,
                        largeur - 15,
                        hauteur / 2 - hauteur,
                        largeur - 30,
                        hauteur / 2 + hauteur,
                    )

        if len(canvas_jeu.find_overlapping(*position_bonus_malus_rouge)) > 1:
            canvas_jeu.coords(bonus_malus_rouge, largeur, -hauteur, largeur, -hauteur)
            effet_rouge = choice(["petite_raquette", "balle_dangereuse"])
            if effet_rouge == "petite_raquette":
                if boost_joueur == 1:
                    canvas_jeu.coords(
                        raquette_2,
                        largeur - 15,
                        hauteur / 2 - 30,
                        largeur - 30,
                        hauteur / 2 + 30,
                    )
                    boost_raquette = 2
                elif boost_joueur == 2:
                    canvas_jeu.coords(
                        raquette_1, 15, hauteur / 2 - 30, 30, hauteur / 2 + 30
                    )
                    boost_raquette = 2
                else:
                    pass

            elif effet_rouge == "balle_dangereuse":
                lieu_de_spawn_x = randint(100, 1820)
                lieu_de_spawn_y = randint(50, 1030)
                canvas_jeu.coords(
                    balle,
                    lieu_de_spawn_x - t_balle,
                    lieu_de_spawn_y - t_balle,
                    lieu_de_spawn_x + t_balle,
                    lieu_de_spawn_y + t_balle,
                )

        bonus_malus()

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


def relancer_jeu():
    fenetre_rejouer.withdraw()
    deplacement_balle()


def ne_pas_relancer():
    fenetre_rejouer.withdraw()
    menu_principal.wm_deiconify()
    fenetre_jeu.withdraw()


# raqutte
t_raquette = 60
raquette_1 = canvas_jeu.create_rectangle(
    15, hauteur / 2 - t_raquette, 30, hauteur / 2 + t_raquette, fill="white"
)
raquette_2 = canvas_jeu.create_rectangle(
    largeur - 15,
    hauteur / 2 - t_raquette,
    largeur - 30,
    hauteur / 2 + t_raquette,
    fill="white",
)


def deplacement_raquette_1(event):

    position_raquette_1 = canvas_jeu.coords(raquette_1)
    vitesse = -25

    if position_raquette_1[1] > 10.0:
        canvas_jeu.move(raquette_1, 0, vitesse)


def deplacement_raquette_2(event):

    position_raquette_1 = canvas_jeu.coords(raquette_1)
    vitesse = 25

    if position_raquette_1[3] < 1070.0:
        canvas_jeu.move(raquette_1, 0, vitesse)


def deplacement_raquette_3(event):

    vitesse = -25
    position_raquette_2 = canvas_jeu.coords(raquette_2)

    if position_raquette_2[1] > 10.0:
        canvas_jeu.move(raquette_2, 0, vitesse)


def deplacement_raquette_4(event):

    vitesse = 25
    position_raquette_2 = canvas_jeu.coords(raquette_2)

    if position_raquette_2[3] < 1070.0:
        canvas_jeu.move(raquette_2, 0, vitesse)


fenetre_jeu.bind("<Tab>", deplacement_raquette_1)
fenetre_jeu.bind("<Shift_L>", deplacement_raquette_2)
fenetre_jeu.bind("<Up>", deplacement_raquette_3)
fenetre_jeu.bind("<Down>", deplacement_raquette_4)

# Menu Principal

menu_principal.title("Pong")

texte_titre = Label(menu_principal, text="PONG", font=("Arial", 50, "bold"))
btn_jouer = Button(
    menu_principal,
    text="JOUER",
    command=lancer_parametre,
    bg="green",
    fg="white",
    font=("Arial", 50, "bold"),
)
btn_quitter = Button(
    menu_principal,
    text="Quitter",
    command=menu_principal.destroy,
    bg="red",
    font=("Arial", 50, "bold"),
)

texte_titre.place(relx=0.5, rely=0.30, anchor=CENTER)
btn_jouer.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_quitter.place(relx=0.5, rely=0.7, anchor=CENTER)

# rejouer

fenetre_rejouer = Toplevel(menu_principal)
fenetre_rejouer.geometry("500x500+720+270")
fenetre_rejouer.title("Pong")


texte_rejouer = Label(fenetre_rejouer, text="Rejouer ?")

btn_oui = Button(
    fenetre_rejouer, text="Oui ! :D", command=relancer_jeu, bg="green", width=12
)
btn_non = Button(
    fenetre_rejouer, text="Nop !", command=ne_pas_relancer, bg="red", width=12
)

texte_rejouer.place(relx=0.5, rely=0.30, anchor=CENTER)

btn_oui.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_non.place(relx=0.5, rely=0.6, anchor=CENTER)

# BULLES BONUS/MALUS

# Jaune : affecte les deux joueurs
# Vert : affecte le joueur qui a touché la balle en dernier
# Rouge : affecte l’autre joueur
bonus_malus_jaune = canvas_jeu.create_oval(1, 1, 1, 1, fill="yellow", width=3)
bonus_malus_vert = canvas_jeu.create_oval(
    largeur, hauteur, largeur, hauteur, fill="green", width=3
)
bonus_malus_rouge = canvas_jeu.create_oval(
    largeur, -hauteur, largeur, -hauteur, fill="red", width=3
)


def bonus_malus():
    spawn = randint(0, 1500)
    lieu_de_spawn_x = 0
    lieu_de_spawn_y = 0

    if spawn == 1:
        lieu_de_spawn_x = randint(100, 1820)
        lieu_de_spawn_y = randint(50, 1030)
        canvas_jeu.coords(
            bonus_malus_jaune,
            lieu_de_spawn_x - t_balle,
            lieu_de_spawn_y - t_balle,
            lieu_de_spawn_x + t_balle,
            lieu_de_spawn_y + t_balle,
        )
    if spawn == 2:
        lieu_de_spawn_x = randint(100, 1820)
        lieu_de_spawn_y = randint(50, 1030)
        canvas_jeu.coords(
            bonus_malus_vert,
            lieu_de_spawn_x - t_balle,
            lieu_de_spawn_y - t_balle,
            lieu_de_spawn_x + t_balle,
            lieu_de_spawn_y + t_balle,
        )
    if spawn == 3:
        lieu_de_spawn_x = randint(100, 1820)
        lieu_de_spawn_y = randint(50, 1030)
        canvas_jeu.coords(
            bonus_malus_rouge,
            lieu_de_spawn_x - t_balle,
            lieu_de_spawn_y - t_balle,
            lieu_de_spawn_x + t_balle,
            lieu_de_spawn_y + t_balle,
        )


# paramètres


def test():
    print(saisie_vitesse.get())


fenetre_parametre = Toplevel(menu_principal)
fenetre_parametre.attributes("-fullscreen", True)

fenetre_parametre.title("Pong")

texte_parametre = Label(
    fenetre_parametre, text="Paramètres du jeu", font=("Arial", 20, "bold")
)
texte_pts = Label(fenetre_parametre, text="Nombre de points pour gagner :")
texte_vitesse = Label(
    fenetre_parametre, text="Vitesse de la balle en début de partie :"
)
texte_balle = Label(fenetre_parametre, text="Couleur de la balle :")
texte_r1 = Label(fenetre_parametre, text="Couleur de la raquette du J1 :")
texte_r2 = Label(fenetre_parametre, text="Couleur de la raquette du J2 :")
texte_bg = Label(fenetre_parametre, text="Couleur du fond d'écran :")

saisie_pts = Entry(fenetre_parametre, width=4)

choix_vitesse = ["Très lent", "Lent", "Moyen", "Rapide"]
saisie_vitesse = ttk.Combobox(fenetre_parametre, values=choix_vitesse, width=9)

choix_couleur = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
saisie_c_balle = ttk.Combobox(fenetre_parametre, values=choix_couleur, width=9)
saisie_c_r1 = ttk.Combobox(fenetre_parametre, values=choix_couleur, width=9)
saisie_c_r2 = ttk.Combobox(fenetre_parametre, values=choix_couleur, width=9)
saisie_c_bg = ttk.Combobox(fenetre_parametre, values=choix_couleur, width=9)


btn_jouer_2 = Button(
    fenetre_parametre,
    text="JOUER",
    command=lancer_jeu,
    bg="green",
    font=("Arial", 20, "bold"),
)
btn_retour = Button(
    fenetre_parametre,
    text="Retour",
    command=retour,
    bg="red",
    font=("Arial", 20, "bold"),
)

texte_parametre.place(relx=0.5, rely=0.2, anchor=CENTER)
texte_pts.place(relx=0.52, rely=0.40, anchor=CENTER)
texte_vitesse.place(relx=0.35, rely=0.40, anchor=CENTER)
texte_balle.place(relx=0.35, rely=0.45, anchor=CENTER)
texte_r1.place(relx=0.35, rely=0.5, anchor=CENTER)
texte_r2.place(relx=0.35, rely=0.55, anchor=CENTER)
texte_bg.place(relx=0.35, rely=0.60, anchor=CENTER)

saisie_pts.place(relx=0.575, rely=0.40, anchor=CENTER)
saisie_pts.insert(0, "5")
saisie_vitesse.place(relx=0.43, rely=0.40, anchor=CENTER)
saisie_vitesse.insert(0, "Lent")
saisie_c_balle.place(relx=0.43, rely=0.45, anchor=CENTER)
saisie_c_balle.insert(0, "white")
saisie_c_r1.place(relx=0.43, rely=0.5, anchor=CENTER)
saisie_c_r1.insert(0, "white")
saisie_c_r2.place(relx=0.43, rely=0.55, anchor=CENTER)
saisie_c_r2.insert(0, "white")
saisie_c_bg.place(relx=0.43, rely=0.6, anchor=CENTER)
saisie_c_bg.insert(0, "black")

btn_jouer_2.place(relx=0.55, rely=0.5, anchor=CENTER)
btn_retour.place(relx=0.55, rely=0.58, anchor=CENTER)


fenetre_parametre.withdraw()
fenetre_rejouer.withdraw()

fenetre_parametre.mainloop()
fenetre_rejouer.mainloop()
menu_principal.mainloop()
