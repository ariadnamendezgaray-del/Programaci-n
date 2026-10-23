
def calcular_quota_bizum ( total_despesa, num_persones = 3, concepte="Despeses"):
    total_despeses= round (total_despesa / num_persones, 2) 
    
    return ("L'import corresponent per cada persona es de ", total_despeses)




