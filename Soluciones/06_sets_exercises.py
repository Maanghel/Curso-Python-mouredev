"""
1. Crea un set con los números del 1 al 5 e imprímelo. 

2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo. 

3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} 
    nuevamente. ¿Qué sucede? 

4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e 
    imprime el resultado. 

5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el 
    set resultante. 

6. Usa el método clear() para vaciar un set y luego imprime 
    su longitud. 

7. Convierte el set {"manzana", "naranja", "plátano"} en 
    una lista e imprime el primer elemento de la lista. 

8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e 
    imprime el set resultante. 

9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 
    4, 5, 6} e imprime el resultado. 

10. Elimina un set llamado my_set usando del y luego 
    intenta imprimirlo para ver el resultado.
"""

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6) # Agrega un valor al set
print(f"\n{my_set}")

my_set.add(5) # Los sets no permiten valores repetidos
print(f"\n{my_set}")

print(f"\n{3 in my_set}") # Verifica si un valor se encuentra en el set

my_set.remove(4) # Elimina un valor del set
print(f"\n{my_set}")

my_set.clear()
print(f"\n{len(my_set)}")

my_fruits_set = {"manzana", "naranja", "platano"}
my_list = list(my_fruits_set)
print(f"\n{my_list[0]}")

my_first_set = {1, 2, 3}
my_second_set = {4, 5, 6}
my_concatenated_set = my_first_set.union(my_second_set) # Concatena dos sets
print(f"\n{my_concatenated_set}")

my_third_set = {1, 2, 3, 4}
my_fourth_set = {3, 4, 5, 6}
print(f"\n{my_third_set.difference(my_fourth_set)}") # Retorna la diferencia entre dos sets

del my_set # Elimina un set
# print(f"\n{my_set}") NameError