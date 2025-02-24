# Ejercicio 2
# Autor: mohamed mchachi hjiej
# Versión: 1.0

def sustituir_caracter():
    cadena = input("Introduce una cadena: ")
    
    caracter1 = input("Introduce el primer caracter: ")
    while len(caracter1) != 1:
        caracter1 = input("Error. Debes introducir un único caracter. Vuelve a intentarlo: ")
    
    caracter2 = input("Introduce el segundo caracter: ")
    while len(caracter2) != 1:
        caracter2 = input("Error. Debes introducir un único caracter. Vuelve a intentarlo: ")
    
    nueva_cadena = cadena.replace(caracter1, caracter2)
    print("Cadena resultante:", nueva_cadena)

if __name__ == "__main__":
    sustituir_caracter()
