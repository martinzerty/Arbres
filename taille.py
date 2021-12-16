def taille(a):
    if a[0] == '' and a[1] == '':
        return 1
    elif a[0] == '':
        return 1+ taille(a[1])
    elif a[1] == '':
        return 1+taille(a[0])
    else:
        return 1+taille(a[0])+taille(a[1])
