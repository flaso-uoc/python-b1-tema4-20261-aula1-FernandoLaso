"""
Implementa una función 'read_and_write', no recibe ningún parámetro debido a
que, dentro de la misma se debe solicitar la entrada de 2 datos mediante
teclado.

En el momento de solicitar el ingreso de los datos se debe considerar el
siguiente texto.
'Insert your name: ' El valor introducido debe ser de tipo str.
'Insert your age: ' El valor introducido debe ser de tipo int.

Se debe crear un archivo de texto 'file.txt' donde La información entrada
por consola debe ser guardada en dicho archivo y se debe imprimir por consola
desde el archivo de texto.

Parámetro:
No recibe ningún parámetro.

Ejemplo:
    Entrada:
        'Insert your name: ' Julio 
        'Insert your age: ' 30
    Salida:
        Julio
        30
"""

def read_and_write():
    name = input("Insert your name: ")
    age = int(input("Insert your age: "))
    with open("file.txt", "w+") as f:
        f.write(name+"\n")
        f.write(str(age))

    with open("file.txt", "r") as rf:
        file = rf.readlines()      
        for line in file:
            print(line, end="")

# read_and_write()
