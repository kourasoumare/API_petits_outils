def factorielle(n):
    if not isinstance(n,int) or  n < 0:
         raise ValueError("n doit être un entier positif ou nul")
    resultat = 1
    for i in range(2, n + 1):
        resultat = resultat * i
    return resultat
    