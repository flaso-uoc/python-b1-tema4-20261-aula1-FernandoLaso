"""
Enunciado:
Realizando la entrada por consola de los datos, implementa la función 'sum'
que solicite la entrada de dos números con 'input' y devuelva la suma de los
números.

Parámetro:
No recibe ningún parámetro debido a que dentro de la función se solicita la
entrada de los números.

Ejemplo:
    Entrada:
        "Insert the first number: " 8
        "Insert the second number: " 3

    Salida:
        "Result: " 11
"""

def sum():
    n_1 = int(input("Insert the first number: "))
    n_2 = int(input("Insert the second number: "))
    result = n_1 + n_2
    print("Result: ", result)
    return result

# sum()