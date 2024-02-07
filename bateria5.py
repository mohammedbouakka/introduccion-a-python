# Obtenir la quantitat d'anys com a programador de l'usuari
anys_treballats = int(input("Quants anys portes treballant com a programador? "))

# Determinar el nivell (junior o senior)
if anys_treballats < 5:
    nivell = "Junior"
else:
    nivell = "Senior"

# Imprimir el resultat
print(f"Ets {nivell} com a programador.")
