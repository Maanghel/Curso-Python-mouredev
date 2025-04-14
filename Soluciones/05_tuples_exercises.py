"""
1. Crea una tupla con los valores (10, 20, 30, 40, 50) e 
    imprímela. 

2. Accede al segundo elemento de la tupla (100, 200, 300, 
    400, 500) y muéstralo. 

3. Intenta modificar el primer elemento de la tupla (1, 2, 
    3) a 10 y observa el resultado. 

4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 
    2, 3, 3, 4, 5, 3). 

5. Encuentra el índice de la primera aparición de la cadena 
    "Python" en la tupla ("Java", "Python", "JavaScript", 
    "Python"). 

6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la 
    tupla resultante. 

7. Crea una subtupla con los elementos desde la posición 2 
    hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 
    40, 50). 

8. Convierte la tupla ("rojo", "verde", "azul") en una 
    lista, cambia el segundo elemento a "amarillo" y vuelve 
    a convertirla en una tupla. Imprime la tupla resultante. 

9. Elimina una tupla llamada my_tuple usando del y luego 
    intenta imprimirla para ver el resultado. 

10. Crea una tupla con un solo elemento (el número 100) 
    e imprímela. Asegúrate de usar la sintaxis correcta para 
    crear una tupla con un solo elemento.
"""

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

my_second_tuple = (100, 200, 300, 400, 500)
print(f"\n{my_tuple[1]}")

my_third_tuple = (1, 2, 3)
# my_third_tuple[0] = 10 TypeError
print(f"\n{my_third_tuple}")

my_other_tuple = (1, 2, 3, 3, 4, 5, 3)
print(f"\n{my_other_tuple.count(3)}") # Devuelva la cantidad de ocasiones que aparece un valor

my_string_tuple = ("Java", "Python", "JavaScript", "Python")
print(f"\n{my_string_tuple.index("Python")}") # Devuelve el indice de la primera incidencia

other_tuple = (1, 2, 3)
other_other_tuple = (4, 5, 6)
print()
print(other_tuple + other_other_tuple) # Concatena dos tuplas

sub_tuple = my_tuple[2:4] # Crea una sub tupla con slicing
print(f"\n{sub_tuple}")

color_tuple = ("rojo", "verde", "azul")
my_list = list(color_tuple)
my_list[1] = "amarillo"
color_tuple = tuple(my_list)
print(f"\n{color_tuple}")

del my_tuple # Elimina una tupla
# print(my_tuple) NameError

only_one_element = (100, ) # Sintaxis para crear una tupla de un solo elemento
print(f"\n{only_one_element}")