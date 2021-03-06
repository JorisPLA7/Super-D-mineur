#!/usr/bin/env python3
"""Minesweeper game"""

##PROGRAMME SOUS LICENSE G.P.L (see README.md) ........ Joris Placette ........ 2017

def initialisation(largeur, Longueur, difficulté):  # initialise le dessous de grille
    global tableau
    tableau = []
    for i in range(Longueur):  # positionnement des mines
        lignes = [" " for i in range(largeur)]
        for i in range(len(lignes)):
            mine = random.randint(0, 35)
            if mine <= difficulté:
                lignes[i] = "o"
        tableau.append(lignes)

    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] != "o":
                nb = 0  # compteur pour les numéros
                try:
                    if tableau[i - 1][j - 1] == "o":
                        nb += 1
                except:
                    pass
                try:
                    if tableau[i - 1][j] == "o":
                        nb += 1
                except:
                    pass
                try:
                    if tableau[i - 1][j + 1] == "o":
                        nb += 1
                except:
                    pass
                try:
                    if tableau[i][j - 1] == "o":
                        nb += 1
                except:
                    pass
                try:
                    if tableau[i][j + 1] == "o":
                        nb += 1
                except:
                    pass
                try:
                    if tableau[i + 1][j - 1] == "o":
                        nb += 1
                except:
                    pass
                try:
                    if tableau[i + 1][j] == "o":
                        nb += 1
                except:
                    pass
                try:
                    if tableau[i + 1][j + 1] == "o":
                        nb += 1

                except:
                    pass

                if nb != 0:
                    tableau[i][j] = str(nb)


def init_plateau():  # crée la liste "affichée" à l'utilisateur
    global plateau
    plateau = [[] for i in range(len(tableau))]
    for i in range(len(plateau)):
        plateau[i] = [0 for j in range(len(tableau[i]))]
        # un tableau qui contient des zéros pour l'instant, signifiant "case non découverte"


def liberer():
    meme = 0
    while meme == 0:
        save = plateau
        for i in range(15):

            for i in range(len(tableau)):
                for j in range(len(tableau[i])):
                    if plateau[i][j] == " ":
                        try:
                            if tableau[i - 1][j] != "o":
                                plateau[i - 1][j] = tableau[i - 1][j]
                        except:
                            pass
                        try:
                            if tableau[i + 1][j] != "o":
                                plateau[i + 1][j] = tableau[i + 1][j]
                        except:
                            pass
                        try:
                            if tableau[i][j - 1] != "o":
                                plateau[i][j - 1] = tableau[i][j - 1]
                        except:
                            pass
                        try:
                            if tableau[i][j + 1] != "o":
                                plateau[i][j + 1] = tableau[i][j + 1]

                        except:
                            pass
                        try:
                            if tableau[i - 1][j - 1] != "o":
                                plateau[i - 1][j - 1] = tableau[i - 1][j - 1]
                        except:
                            pass
                        try:
                            if tableau[i - 1][j - 1] != "o":
                                plateau[i - 1][j - 1] = tableau[i - 1][j - 1]
                        except:
                            pass
                        try:
                            if tableau[i + 1][j - 1] != "o":
                                plateau[i + 1][j - 1] = tableau[i + 1][j - 1]
                        except:
                            pass
                        try:
                            if tableau[i + 1][j + 1] != "o":
                                plateau[i + 1][j + 1] = tableau[i + 1][j + 1]
                        except:
                            pass
        if save == plateau:
            meme = 1


def positionnement(x, y, action):
    if action == "rightclick":  # on place le drapeau (d) ou le point d'interrogation (?)
        if plateau[x][y] == 0:
            plateau[x][y] = "d"

        elif plateau[x][y] == "d":
            plateau[x][y] = "?"

        elif plateau[x][y] == "?":
            plateau[x][y] = 0

    elif action == "leftclick":
        if tableau[x][y] == "o":
            print("boom")
            findujeu()

        if tableau[x][y] != "o":
            plateau[x][y] = tableau[x][y]

        liberer()
    victoire()


def findujeu():  # défaite
    #print("game over")
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if tableau[i][j] == "o":
                if plateau[i][j] == "d":
                    plateau[i][j] = "green"
                else:
                    plateau[i][j] = "bomb"
            if plateau[i][j] == "d" and tableau[i][j] != "o":
                plateau[i][j] = "fail"
    refreshcanvas()
    # voir sur tk pour l'affichage de la fin


def victoire():  # dans le mainloop : vérifie les conditions de victoire
    toutes_mines_trouvées = True
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):

            if tableau[i][j] == "o":
                toutes_mines_trouvées = toutes_mines_trouvées and plateau[i][j] == "d"

            if plateau[i][j] == "d" and tableau[i][j] != "o":
                toutes_mines_trouvées = False

    if toutes_mines_trouvées == True:
        #print("Bravo !")
        for i in range(len(tableau)):
            for j in range(len(tableau[i])):
                if tableau[i][j] == "o":
                    plateau[i][j] = "gold"
                    # actions de fin de partie
                    # rejouer ?


def key(event):
    print("pressed", repr(event.char))


def callback(event):  # clic gauche

    x, y = event.x // 20, event.y // 20
    positionnement(x, y, "leftclick")
    refreshcanvas()


def call2(event):  # clic droit
    x, y = event.x // 20, event.y // 20
    positionnement(x, y, "rightclick")
    refreshcanvas()


def createNewDraw():
    pulldata()
    global w
    w = Canvas(aside, width=(cacheData['xLen'] * 20), height=(cacheData['yLen'] * 20), background='white')
    w.pack()  # on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
    w.bind("<Key>", key)
    w.bind("<Button-1>", callback)
    w.bind("<Button-3>", call2)
    w.pack()
    initialisation(cacheData['xLen'], cacheData['yLen'], cacheData['p'])
    init_plateau()
    refreshcanvas()
    # checkbutton.pack()
    starter.destroy()


'''à changer'''


# réccupération des données de l'utilisateur
def pulldata():
    # récupération des données
    cacheData["p"] = int(p.get())
    cacheData["xLen"] = int(xLen.get())
    cacheData["yLen"] = cacheData["xLen"]


def refreshcanvas():
    w.delete("all")

    for x in range(len(tableau)):
        for y in range(len(tableau[x])):

            # print('x = {} y = {}  b = {}'.format(x,y,cacheData['draw'][x][y]))
            a = (x * 20 + 1, y * 20 + 1)
            b = ((a[0] + 18), a[1] + 18)
            # if cacheData['draw'][x][y] == 0 : w.create_rectangle(a[0], a[1], b[0], b[1], fill="white")
            if plateau[x][y] == ' ':
                w.create_rectangle(a[0], a[1], b[0], b[1], fill="white", outline="")

            if plateau[x][y] == 0:  # case inexplorée
                w.create_rectangle(a[0], a[1], b[0], b[1], fill="grey", outline="")

            if plateau[x][y] == 'green':
                w.create_rectangle(a[0], a[1], b[0], b[1], fill="green", outline="")
                w.create_text(a[0] + 8, a[1] + 8, text=str(chr(9881)))

            if plateau[x][y] == 'bomb':
                w.create_rectangle(a[0], a[1], b[0], b[1], fill="purple", outline="")
                w.create_text(a[0] + 8, a[1] + 8, text=str(chr(9881)))
            if plateau[x][y] == 'gold':
                w.create_rectangle(a[0], a[1], b[0], b[1], fill="yellow", outline="")
                w.create_text(a[0] + 8, a[1] + 8, text=str(chr(9883)))
            if plateau[x][y] == 'fail':
                w.create_rectangle(a[0], a[1], b[0], b[1], fill="orange", outline="")
                w.create_text(a[0] + 8, a[1] + 8, text=str(chr(9874)))

            if plateau[x][y] == '?':
                w.create_rectangle(a[0], a[1], b[0], b[1], fill="grey", outline="")
                w.create_text(a[0] + 8, a[1] + 8, text='?')

            if plateau[x][y] == 'd':
                w.create_rectangle(a[0] + 1, a[1] + 1, b[0] - 1, b[1] - 1, fill="red", outline="")
                w.create_text(a[0] + 8, a[1] + 8, text=str(chr(9873)))
            for i in range(1, 8):
                if plateau[x][y] == str(i):
                    w.create_text(a[0] + 8, a[1] + 8, text=str(i))


# gui refreshers
def guimessage(color, context, reason):
    messageframe = LabelFrame(root, text=context, fg=color)
    messageframe.pack(fill="both", expand="no", side=BOTTOM)

    destroybutton = Button(messageframe, text="x", command=messageframe.destroy)
    destroybutton.pack(side=LEFT)

    left = Label(messageframe, text=reason, fg=color)
    left.pack()  # on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)


## init tkinter
# importation des bibliotheques pyhton
from tests import listes
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import askokcancel, askyesno, askquestion
from lib import web
#from lib import datasheets
import random
import time


global appVersion  # Variable contenant le numero de version du porgramme (écrit avec les données)

global palette

global posxmax

global thereIsADraw

global passedTime
passedTime = 800

appVersion = "1.1"

cacheData = {}

root = Tk()  # création de la fenêtre tkinter racine

root.wm_title('Super D-Mineur')  # definition du titre
# root.wm_iconbitmap('ressources/supano.ico')#definition de l'icone

##Barre de Menu supérieur
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)  # sous menu
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)  # sous menu
helpmenu.add_command(label="Version : {}".format(appVersion), command=web.help)
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_command(label="Rules", command=web.rules)

devmenu = Menu(menubar, tearoff=0)  # sous menu
menubar.add_cascade(label="Dev", menu=devmenu)

root.config(menu=menubar)

##Titre
header = Label(root, text="Super-D-mineur Version {} stable !".format(appVersion))
header.pack(fill="both", expand="no")

##Panneau latéral
aside = Frame(root)
aside.pack(side=LEFT)

##panneau  init
starter = LabelFrame(root, text="Configuration : init")
starter.pack(fill="both", expand="yes", side=TOP)

left = Label(starter, text="difficulty ")
left.pack()
p = Scale(starter, from_=1, to=10, )
p.pack()

left2 = Label(starter, text="Terrain size (x = y)")
left2.pack()  # on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

xLen = Spinbox(starter, from_=20, to=100, )
xLen.pack()  # on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

creatbutton = Button(starter, text="Play !", command=createNewDraw)
creatbutton.pack()

root.mainloop()
