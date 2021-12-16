def prefixe(a):
    print(a.valeur)
    if a.enfant_gauche:
        prefixe(a.enfant_gauche)
    if a.enfant_droit:
        prefixe(a.enfant_droit)
