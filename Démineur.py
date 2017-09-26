import random


def initialisation(largeur, Longueur, difficulté): #initialise le dessous de grille
    global tableau
    tableau=[]
    for i in range(Longueur): #positionnement des mines
        lignes=[" " for i in range(largeur)]
        for i in range(len(lignes)):
            mine=random.randint(0,35)
            if mine<=difficulté:
                lignes[i]="o"
        tableau.append(lignes)

    for i in range(Longueur):
        for j in range(largeur): #compteur pour les numéros
            if tableau[i][j]!="o":
                nb=0
                try:
                    if tableau[i-1][j-1]=="o":
                        nb+=1

                    if tableau[i-1][j]=="o":
                        nb+=1
                        
                    if tableau[i-1][j+1]=="o":
                        nb+=1

                    if tableau[i][j-1]=="o":
                        nb+=1
                        
                    if tableau[i][j+1]=="o":
                        nb+=1

                    if tableau[i+1][j-1]=="o":
                        nb+=1
                        
                    if tableau[i+1][j]=="o":
                        nb+=1

                    if tableau[i+1][j+1]=="o":
                        nb+=1

                except:
                    pass
                        
                if nb!=0:
                    tableau[i][j]=str(nb)


def init_plateau():   #crée la liste "affichée" à l'utilisateur
    global plateau
    plateau=[ [] for i in range(len(tableau))]
    for i in range(len(plateau)):
                   plateau[i]=[0 for j in range(len(tableau[i]))]
                   # un tableau qui contient des zéros pour l'instant, signifiant "case non découverte"


def positionnement(x,y,action):
               
    if action=="rightclick" :#on place le drapeau (d) ou le point d'interrgoation (?)
        if plateau[x][y]==0:
            plateau[x][y]="d"
                   
        elif plateau[x][y]=="d":
            plateau[x][y]="?"
                   
        elif plateau[x][y]=="?":
            plateau[x][y]=0

    elif action=="leftclick":
        if tableau[x][y]=="o":
            
            print("boom")
            findujeu()
        
        if tableau[x][y]!="o":
            plateau[x][y]=tableau[x][y]

def findujeu(): #défaite
    print("game over")
    #voir sur tk pour l'affichage de la fin

def victoire (): # dans le mainloop : vérifie les conditions de victoire
    toutes_mines_trouvées=True
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
                       
            if tableau[i][j]=="o":
                toutes_mines_trouvées= toutes_mines_trouvées and plateau[i][j]=="d"

    if toutes_mines_trouvées==True :
        print("Bravo !")
        #actions de fin de partie
        #rejouer ?
                       
                       
    
    
    
    
                    
                    

initialisation(10,10,7)
init_plateau()
    



