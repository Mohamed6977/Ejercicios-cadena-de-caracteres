# Ejercicio 3
# Autor: mohamed mchachi hjiej
# Versión: 1.0

def intercambiar_mayus_minus():
    cadena = input("Introduce una cadena: ")
    resultado = ""
    
    for caracter in cadena:
        if caracter.islower():
            resultado += caracter.upper()
        elif caracter.isupper():
            resultado += caracter.lower()
        else:
            resultado += caracter
    
    print("Cadena transformada:", resultado)

if __name__ == "__main__":
    intercambiar_mayus_minus()
