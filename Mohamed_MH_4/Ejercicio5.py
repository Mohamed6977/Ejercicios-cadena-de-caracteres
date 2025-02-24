# Ejercicio 5
# Autor: mohamed mchachi hjiej
# Versión: 1.0

def es_palindromo():
    cadena = input("Introduce una cadena: ")
    if cadena == cadena[::-1]:
        print("La cadena es un palíndromo.")
    else:
        print("La cadena NO es un palíndromo.")

if __name__ == "__main__":
    es_palindromo()
