#CorreTapa Pro 
#L'equip de disseny de CorreTapa App necessita un motor de diagòstiic per valorar automàticament els bars de la ruta gastronòmica.

def evaluar_estat_bar (nom_bar: str, te_tapa: bool, preu_cervesa: float, nota_clients: float, es_artesana: bool = False)

    if te_tapa == True and preu_cervesa <= 2.50 and nota_cients >= 4.5:
      estat =" DESTACAT_TOP"

    elif te_tapa == True and nota_clients >= 4.0:
       estat = " Molt Recomanable"
       
    elif te_tapa == False or es_artesana == True and preu_cervesa <= 3.00:
       estat ="Craft bon preu"

    else :
        estat = " ESTANDARD"

    return "Diagnostic" + nom_bar + "Estat" + str(estat)

#Proves 

test_1 = evaluar_estat_bar('El Racó de la Tapa:', True, 2.20, 4.8)
test_2 = evaluar_estat_bar('Taverna Central:' True, 2.8, 4.2)
test_3 = evaluar_estat_bar('BreDog Poblenou:' False, 2.9, 4.4, True)
    
