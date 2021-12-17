def hauteur(a):
    if not a.enfant_gauche and not a.enfant_droit:
        return 1
    elif not a.enfant_gauche:
        return 1+hauteur(a.enfant_droit)
    elif not a.enfant_droit:
        return 1+hauteur(a.enfant_gauche)
    else:
        return 1+max(hauteur(a.enfant_droit), hauteur(a.enfant_gauche))
    
    
