"""
Enunciado:
Implementa la función 'squared_sum_ram(numbers_list)' que recibe una lista de números
enteros y calcule la suma de sus valores al cuadrado. Se debe usar un bucle 'for'
para ilustrar el uso de la RAM.

La función 'squared_sum_heap(numbers_list)' ya está implementada y debe almacenar la
suma de los valores al cuadrado en el Heap. Sin embargo, existe un error en este cálculo identifícalo y corrígelo.

Parámetros:
    - numbers_list: Lista de números enteros.

Ejemplo:
    Entrada:
    squared_sum_ram([6, 4, 7])
    squared_sum_heap([6, 4, 7])

    Salida:
    101
    101

"""


def squared_sum_ram(numbers_list):
    cuadrado = []
    for n in numbers_list:
        cuadrado.append(n**2)
    sumados = 0
    for n in cuadrado:
        sumados += n
    return sumados


def squared_sum_heap(numbers_list):
    # Store the list in Heap
    # You should correct and overwrite something in the following line.
    squared_sum_list = [num**2 for num in numbers_list]
    heap_sum = sum(squared_sum_list)
    return heap_sum



numbers_list = [6, 4, 7]
print(squared_sum_ram(numbers_list))
print(squared_sum_heap(numbers_list))
