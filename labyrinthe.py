def ajouterLien(graphe, a, b):
    graphe[a][b] = 1
    graphe[b][a] = 1

def parcourir(graphe, courant, arrivee, visites, chemin):
    visites[courant] = True
    chemin.append(courant)
    if courant == arrivee:
        return True
    for v in range(10):
        if graphe[courant][v] == 1 and not visites[v]:  # noqa: SIM102
            if parcourir(graphe, v, arrivee, visites, chemin):
                return True
    chemin.pop()
    return False

def trouverChemin(graphe, depart, arrivee):
    visites = [False] * 10
    chemin = []
    if parcourir(graphe, depart, arrivee, visites, chemin):
        return chemin
    return []

A, B, C, D, E, F, G, H, I, J = range(10)
graphe = [[0] * 10 for _ in range(10)]
for a, b in [(A, B), (B, C), (B, E), (C, D), (C, F), (F, G), (G, H), (G, I), (I, J)]:
    ajouterLien(graphe, a, b)

noms = "ABCDEFGHIJ"
chemin = trouverChemin(graphe, A, J)
print([noms[i] for i in chemin])