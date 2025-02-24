# Ejercicio 4
# Autor: mohamed mchachi hjiej
# Versión: 1.0

def contiene_subcadena():
    cadena = input("Introduce la cadena principal: ")
    subcadena = input("Introduce la subcadena a buscar: ")
    
    if subcadena in cadena:
        print("La subcadena está contenida en la cadena principal.")
    else:
        print("La subcadena NO está contenida en la cadena principal.")

if __name__ == "__main__":
    contiene_subcadena()
