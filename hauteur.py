def hauteur(a):
    if a[0] == '' and a[1] == '':
        return 1
    elif a[0] == '':
        return 1+hauteur(a[1])
    elif a[1] == '':
        return 1+hauteur(a[0])
    else:
        return 1+max(hauteur(a[1]), hauteur(a[0]))
    
    
