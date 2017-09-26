import random


def initialisation(largeur, Longueur, difficulté):
    global tableau
    tableau=[]
    for i in range(Longueur):
        lignes=[0 for i in range(largeur)]
        for i in len(lignes):
            mine=random.randint(0,35)
            if mine<=difficulté:
                lignes[i]=1
        tableau.append(lignes)
        
