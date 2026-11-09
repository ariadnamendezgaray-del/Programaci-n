
def calcular_tiquet(factura, taxa=1.02):
    factura = factura["total"] * taxa
    return factura 

comanda_real = {"id" : 894, "client": "Marta", "total": 100.0}
calcular_tiquet(comanda_real)
calcular_tiquet(comanda_real)

print("Preu base:" ,comanda_real["total"])
print("Tiquet calculat:" , calcular_tiquet(comanda_real))