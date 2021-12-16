def prefixe(a):
    print(a.valeur)
    if a.enfant_gauche:
        prefixe(a.enfant_gauche)
    if a.enfant_droit:
        prefixe(a.enfant_droit)

def infixe(a):
    if a.enfant_gauche:
        infixe(a.enfant_gauche)
    print(a.valeur)
    if a.enfant_droit:
        infixe(a.enfant_droit)

def sufixe(a):
    if a.enfant_gauche:
        sufixe(a.enfant_gauche)
    if a.enfant_droit:
        sufixe(a.enfant_droit)
    print(a.valeur)
