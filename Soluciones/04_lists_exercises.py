"""
1. Crea una lista con los números del 1 al 5 e imprímela. 

2. Accede e imprime el tercer elemento de la lista [10, 20, 
    30, 40, 50]. 

3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] 
    e imprímela. 

4. Inserta el número 15 en la posición 2 de la lista [10, 
    20, 30, 40, 50]. 

5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 
    40, 50]. 

6. Usa la función pop() para eliminar el último elemento de 
    la lista [1, 2, 3, 4, 5] y almacénalo en una variable. 
    Imprime la variable y la lista. 

7. Invierte la lista [100, 200, 300, 400, 500] e imprímela. 

8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e 
    imprímela. 

9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el 
    resultado en una nueva lista. Imprime la lista 
    resultante. 

10. Crea una sublista con los elementos de la lista 
    [10, 20, 30, 40, 50] que van desde la posición 1 hasta 
    la 3 (sin incluir la posición 3).
"""

my_list = [1, 2, 3, 4, 5]
print(my_list)

print(f"\n{my_list[2]}")

my_list.append(6) # Inserta un valor en el ultimo index de la lista
print(f"\n{my_list}")

my_other_list = [10, 20, 30, 40, 50]
my_other_list.insert(2, 15) # Inserta un valor en el index indicado
print(f"\n{my_other_list}")

my_other_list.remove(30) # Elimina el primer elemento encontrado del valor indicado
print(f"\n{my_other_list}")

number_remove = my_list.pop() # Elimina el ultimo valor de la lista
print(f"\n{number_remove}")
print(f"{my_list}")

my_other_other_list = [100, 200, 300, 400, 500]
my_other_other_list.reverse() # Voltea el orden de la lista
print(f"\n{my_other_other_list}")

my_new_list = [3, 1, 4, 2, 5]
my_new_list.sort() # Ordena la lista de menor a mayor
print(f"\n{my_new_list}")

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_concatenated_list = my_first_list + my_second_list # Concatena dos listas
print(f"\n{my_concatenated_list}")

my_last_list = [10, 20, 30, 40, 50]
my_slice_list = my_last_list[1: 3] # Se usa el slicing para conseguir ciertos elementos de la lista segun su index
print(f"\n{my_slice_list}")