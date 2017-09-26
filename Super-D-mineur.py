##PROGRAMME SOUS LICENSE G.P.L (see README.md) ........ Joris Placette ........ 2017










def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    print ("clicked at", event.x//20, event.y//20)
    




'''à changer'''
def rbfcbutton():  #fonction appelée pour ouvrir un fichier existant
   global cacheData
   cacheData = datasheets.pickread()
   global MyDraw
   MyDraw = listes.Draw(cacheData['xLen'],cacheData['yLen'],cacheData['p'])
   MyDraw.applyDraw(cacheData['draw'])
   checkbutton.pack()

   print("nouvelles données en ram: {}".format(cacheData))

'''à changer'''

def wbfcbutton(): #fonction appelée pour écrire les valeurs dans un fichier
   datasheets.pickwrite(cacheData) # se référer à datasheets.py

def createNewDraw():
    pulldata()
    w = Canvas(aside, width=(cacheData['xLen']*20), height=(cacheData['yLen']*20), background='white')
    w.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
    w.bind("<Key>", key)
    w.bind("<Button-1>", callback)
    w.pack()
    global MyDraw
    MyDraw = listes.Draw(cacheData['xLen'],cacheData['yLen'],cacheData['p'])
    refreshcanvas()
    checkbutton.pack()
    starter.destroy()

'''à changer'''
#réccupération des données de l'utilisateur
def pulldata():
    #récupération des données
   cacheData["p"] = int(p.get())
   cacheData["xLen"] = int(xLen.get())
   cacheData["yLen"] = int(yLen.get())

def refreshcanvas():
   w.delete("all")
   cacheData["draw"] = MyDraw.getCurrentDraw()

   for x in range(0,len(cacheData['draw']-1)):
       for y in range(0,len(cacheData['draw'][x]-1)):
   
       #print('x = {} y = {}  b = {}'.format(x,y,cacheData['draw'][x][y]))
           a = (x*20+1, y*20+1)
           b = ((a[0]+18), a[1]+18)
           #if cacheData['draw'][x][y] == 0 : w.create_rectangle(a[0], a[1], b[0], b[1], fill="white")
           if cacheData['draw'][x][y] == 1 :
               w.create_rectangle(a[0], a[1], b[0], b[1], fill="white", outline="")
           if cacheData['draw'][x][y] == 0: # case inexplorée
               w.create_rectangle(a[0], a[1], b[0], b[1], fill="black", outline="")
           for i in range(1,8):
               if cacheData['draw'][x][y] == str(i) :
                   w.create_text(a[0], a[1], text=str(i))
                   
def donothing(): #ne fait rien, comme son nom l'indique
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
   print("Fenêtre qui ne fait rien ouverte")

'''à changer'''
def forcesave():
   print("tentative de sauvegarde forcée")
   pulldata()
   wbfcbutton()

'''à changer'''
#gui refreshers
def guimessage(color, context, reason):
   messageframe = LabelFrame(root, text=context, fg=color )
   messageframe.pack(fill="both", expand="no", side=BOTTOM)

   destroybutton= Button(messageframe, text="x", command=messageframe.destroy)
   destroybutton.pack(side=LEFT)

   left = Label(messageframe, text=reason, fg=color)
   left.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

## init tkinter
#importation des bibliotheques pyhton
try:
    from tests import listes
    print("bibliothèque importée avec succès :  listes")
except:
    print("Impossible d'importer la bibliothèque :  listes")

try: #schéma classique verbeux, afin que l'utilisateur sache quels fichiers sont manquants
    from tkinter import *
    print("bibliothèque importée avec succès :  tkinter")
except:
    print("Impossible d'importer la bibliothèque :  tkinter")
try:
    from tkinter.filedialog import *
    print("bibliothèque importée avec succès :  tkinter")
except:
    print("Impossible d'importer la bibliothèque :  tkinter")
try:
    from tkinter.messagebox import askokcancel, askyesno,askquestion
    print("bibliothèque importée avec succès :  tkinter")
except:
    print("Impossible d'importer la bibliothèque :  tkinter")
try:
    import pickle
    print("bibliothèque importée avec succès :  pickle")
except:
    print("Impossible d'importer la bibliothèque :  pickle")
try:
    from lib import web
    print("bibliothèque importée avec succès :  lib\web")
except:
    print("Impossible d'importer la bibliothèque :  lib\web")
try:
    from lib import datasheets
    print("bibliothèque importée avec succès :  lib\datasheets")
except:
    print("Impossible d'importer la bibliothèque :  lib\datasheets")
try:
    import random
    print("bibliothèque importée avec succès :  random")
except:
    print("Impossible d'importer la bibliothèque :  random")
try:
    import time
    print("bibliothèque importée avec succès :  time")
except:
    print("Impossible d'importer la bibliothèque :  time")


global appVersion #Variable contenant le numero de version du porgramme (écrit avec les données)

global palette

global posxmax

global thereIsADraw

global passedTime
passedTime = 800
#MyDraw = listes.Draw(200,200,0.3)

appVersion = "0.0"
'''helpPage = "https://github.com/JorisPLA7/Super-Conway/blob/master/README.md" #lien pages d'aide à consulter
githubPage = "https://github.com/JorisPLA7/Super-Conway/blob/master/"
'''
cacheData = {}


root=Tk() #création de la fenêtre tkinter racine

root.wm_title('Super D-Mineur')#definition du titre
root.wm_iconbitmap('ressources\supano.ico')#definition de l'icone



##Barre de Menu suppérieur
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0) #sous menu

filemenu.add_command(label="Ouvrir une sauvegarde", command=rbfcbutton)
filemenu.add_command(label="Sauvegarder sans validation", command=forcesave)
filemenu.add_separator()

filemenu.add_command(label="Quitter", command=root.destroy)
menubar.add_cascade(label="Fichier", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0) #sous menu
helpmenu.add_command(label="Version de l'application : {}".format(appVersion), command=web.help)
helpmenu.add_command(label="Ouvrir une aide sur le web", command=web.help)
menubar.add_cascade(label="Aide", menu=helpmenu)

devmenu = Menu(menubar, tearoff=0) #sous menu
menubar.add_cascade(label="Developpement", menu=devmenu)

root.config(menu=menubar)

##Titre
header = Label(root, text="Super-Demineur. Version {}".format(appVersion))
header.pack(fill="both", expand="no")

##Panneau lateral
aside = Frame(root)
aside.pack(side=LEFT)



##panneau  init
starter = LabelFrame(root, text="Configuration : initiale")
starter.pack(fill="both", expand="yes", side=TOP)

left = Label(starter, text="difficulté (croissante)")
left.pack()
p = Scale(starter,from_=1, to=10,)
p.pack()

left2 = Label(starter, text="Taille de la grille (x,y)")
left2.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

xLen = Spinbox(starter, from_=20, to=1000,)
xLen.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
yLen = Spinbox(starter, from_=20, to=1000,)
yLen.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

creatbutton= Button(starter, text="Jouer !", command=createNewDraw)
creatbutton.pack()



root.mainloop()
