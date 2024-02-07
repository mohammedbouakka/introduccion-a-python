# Obtenir la nota de l'usuari
nota = float(input("Introdueix la teva nota: "))

# Determinar el resultat segons l'escala
if 1 <= nota <= 4:
    resultat = "Insuficient"
elif nota == 5:
    resultat = "Suficient"
elif nota == 6:
    resultat = "Bé"
elif 7 <= nota <= 8:
    resultat = "Notable"
elif 9 <= nota <= 10:
    resultat = "Excel·lent"
else:
    resultat = "Nota no vàlida"

# Imprimir el resultat
print(f"Resultat: {resultat}")
