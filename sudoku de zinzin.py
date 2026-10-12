grille = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

def presenteLigne(grille, ligne, chiffre):
    for colonne in range(9):
        if grille[ligne][colonne] == chiffre:
            return True
    return False

def presenteColonne(grille, colonne, chiffre):
    for ligne in range(9):
        if grille[ligne][colonne] == chiffre:
            return True
    return False


def presenteZone(grille, ligne, colonne, chiffre):
    departLigne = (ligne // 3) * 3
    departColonne = (colonne // 3) * 3
    for i in range(3):
        for j in range(3):
            if grille[departLigne + i][departColonne + j] == chiffre:
                return True
    return False


def estValide(grille, ligne, colonne, chiffre):
    if presenteLigne(grille, ligne, chiffre) or presenteColonne(grille, colonne, chiffre) or presenteZone(grille, ligne, colonne, chiffre):  # noqa: SIM103
        return False
    return True

def resoudre(grille, position):
    if position >= 81:
        return True
    ligne = position // 9
    colonne = position % 9 
    if grille[ligne][colonne] != 0:
        return resoudre(grille, position + 1)
    for chiffre in range(1, 10):
        if estValide(grille, ligne, colonne, chiffre):
            grille[ligne][colonne] = chiffre
            if resoudre(grille, position +1):
                return True
            grille[ligne][colonne] = 0
    return False

resoudre(grille, 0)
print ("Solution:")
for ligne in grille:
    print(ligne)