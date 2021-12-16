def prefixe(a):
    if a[0] != '':
        prefixe(a[0])
    print(a)
    if a[1] != '':
        prefix(a[1])
