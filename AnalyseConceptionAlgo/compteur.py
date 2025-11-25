def procedure(n):
    cpt = 0
    i = 1
    while i < n:
        j = i+1
        while j <= n :
            cpt = cpt+1
            j = j+1
        i = i*2
    return cpt

print(procedure(16))