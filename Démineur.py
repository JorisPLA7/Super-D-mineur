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
            if j!="o":
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


def init_plateau():   #crée la liste affichée à l'utilisateur
    global plateau
    plateau=[[]for i in range(len(tableau))]
    
                    
                    

initialisation(10,10,7)

    



