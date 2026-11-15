paraula = input("Introdueix una paraula (en minúscules): ")

comptador = 0
for lletra in paraula:
    if lletra == 'a':
        comptador += 1

print("La paraula conté", comptador, "lletra(es) 'a'.")