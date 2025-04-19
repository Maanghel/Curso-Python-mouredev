"""
1. Crea un diccionario con las claves name, age, y country, 
    asignando valores a cada una. Imprime el diccionario. 

2. Accede al valor de la clave name en el diccionario. 

3. Añade una nueva clave job con el valor "Programador" al 
    diccionario del punto anterior. Imprime el diccionario 
    actualizado. 

4. Modifica el valor de la clave age en el diccionario para 
    que sea 38. Imprime el diccionario actualizado. 

5. Elimina la clave country del diccionario e imprime el 
    diccionario resultante. 

6. Crea un diccionario donde las claves sean números del 1 
    al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 
    4, ...). 

7. Verifica si la clave age está presente en el diccionario 
    {"name": "Brais", "age": 37, "country": "Galicia"}. 

8. Imprime solo las claves del diccionario. 

9. Convierte las claves del diccionario en una lista e 
    imprime la lista resultante. 

10. Crea un nuevo diccionario a partir de una lista de 
    claves ["name", "age", "job"] usando fromkeys(), 
    asignando a todas las claves el valor "Desconocido".
"""

my_dict = {"name": "Manuel", "age": 29, "country": "Mexico"} # Crea un diccionario
print(my_dict)

print(f"\n{my_dict["name"]}") # Imprime el value de la key indicada

my_dict["job"] = "Programador" # Agrega una nueva key:value al diccionario
print(f"\n{my_dict}")

my_dict["age"] = 38 # Modifica el value de la key indicada
print(f"\n{my_dict}")

del my_dict["country"] # Elimina una key:value
print(f"\n{my_dict}")

my_other_dict = {x: x ** 2 for x in range(1, 6)}
print(f"\n{my_other_dict}")

my_new_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
print(f"\n{"age" in my_new_dict }") # Verifica si una key se encuentra en el diccionario

print(f"\n{my_dict.keys()}") # Imprime solo las keys del diccionario

my_keys_list = my_dict.keys() # Crea una lista con solo las keys
print(f"\n{my_keys_list}")

my_last_dict = dict.fromkeys(my_keys_list, "Desconocido") # Crea un diccionario con una lista de valores y les asigna un valor a value
print(f"\n{my_last_dict}")