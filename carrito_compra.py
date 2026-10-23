suma_total = 0 
preu_productes = 0

carret = [
        {"producte": "Cafè d'Especialitat", "preu_unitari": 8.50, "quantitat": 2},
        {"producte": "Llet de Civada Barista", "preu_unitari": 1.95, "quantitat":3},
        {"producte": "Xocolata 85% cacau" , "preu_unitari":2.75, "quantitat": 2 },
        ]

for preu_total in carret :
    preu_productes = preu_total["quantitat"] * preu_total["preu_unitari"]
    suma_total = preu_productes +  preu_productes
    

print ("El total de la compra es de:"suma_total)





