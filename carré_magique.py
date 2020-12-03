carre_mag = [[4, 14, 15, 1],[9, 7, 6, 12],[5, 11, 10, 8],[16, 2, 3, 13]]
print (carre_mag)

carre_pas_magique = carre_mag
carre_pas_magique[3][2] = 7 
print(carre_pas_magique)

def afficheCarre(carre):
    a = 0
    for i in range(carre):
        


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    somme = sum(carre_mag[0])
    for i in carre():
        if somme != sum(l):
                return -1
    return somme


def sommeColonne (carre, 1):
    somme = 0
    for i in carre:
        somme += l[i]
    return somme 
    
        
print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))