# Obtenir un número de l'usuari
numero = float(input("Introdueix un número: "))

# Comparar si el número és major, menor o igual a 100
if numero > 100:
    print(f"El número {numero} és major que 100.")
elif numero < 100:
    print(f"El número {numero} és menor que 100.")
else:
    print("El número és igual a 100.")
