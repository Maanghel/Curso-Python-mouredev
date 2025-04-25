"""
1. Usa un bucle while para imprimir los números del 1 al 
    10. 

2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 
    50] e imprime cada número. 

3. Escribe un programa que use un bucle while para sumar 
    los números del 1 al 100 e imprime el resultado. 

4. Escribe un bucle for que imprima cada carácter de la 
    cadena “Python”. 

5. Usa un bucle while para encontrar el primer número 
    divisible por 7 entre 1 y 50. 

6. Usa un bucle for para recorrer el diccionario {“name”: 
    “Brais”, “age”: 37, “country”: “Galicia”} e imprime las 
    claves. 

7. Escribe un programa que use un bucle while para imprimir 
    los números pares entre 1 y 20. 

8. Usa un bucle for con la función range() para imprimir 
    los números del 1 al 10 en orden inverso. 

9. Escribe un programa que use un bucle for para contar 
    cuántas veces aparece el número 30 en la lista[30, 10, 
    30, 20, 30, 40]. 

10. Usa un bucle for para recorrer una lista de nombres 
    y detener el bucle cuando se encuentre el nombre 
    “Brais”. 
"""

count = 1
while count <= 10:
    print(count)
    count += 1

my_list = [10, 20, 30, 40, 50]
print()
for element in my_list:
    print(element)

count = 1
total = 0
while count <= 100:
    total += count
    count += 1
print(f"\n{total}")

string = "Python"
print()
for element in string:
    print(element)

count = 1
while count <= 50:
    if count % 7 == 0:
        print(f"\n{count}")
        break
    count += 1

my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
print()
for key in my_dict:
    print(key)

count = 1
print()
while count <= 20:
    if count % 2 == 0:
        print(count)
    count += 1

print()
for x in range(10, 0, -1):
    print(x)

my_list = [30, 10, 30, 20, 30, 40]
count = 0
for element in my_list:
    if element == 30:
        count += 1
print(f"\n{count}")

my_list_names = ["Angel", "Juan", "Pablo", "Roberto", "Brais", "Moure", "Elena"]
print()
for name in my_list_names:
    if name == "Brais":
        print("Se encontro el nombre Brais")
        break
    print(name)