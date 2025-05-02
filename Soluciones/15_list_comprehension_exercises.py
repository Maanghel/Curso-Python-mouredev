"""
1. Genera una lista utilizando comprensión con los números
    del 0 al 10.

2. Crea una lista utilizando comprensión con los cuadrados
    de los números del 1 al 10.

3. Genera una lista utilizando comprensión con los números
    pares del 0 al 20.

4. Convierte una lista de temperaturas en Celsius a
    Fahrenheit utilizando comprensión.

5. Crea una lista utilizando comprensión con los caracteres
    de una cadena.

6. Filtra una lista de palabras y deja solo las que tienen
    más de 4 letras utilizando comprensión.

7. Aumenta en 5 cada número de una lista con comprensión
    usando una función externa.

8. Crea una lista de booleanos que indique si cada número
    es mayor que 10 utilizando comprensión.

9. Multiplica solo los números impares por 3 en una lista
    utilizando comprensión.

10. Usa comprensión de listas anidada para generar una
    matriz 3x3 con números del 1 al 9.
"""

new_list = [i for i in range(11)] # Genera una lista utilizando comprensión con los números del 0 al 10.
print(new_list)

list_squared = [i ** 2 for i in range(1, 11)] # Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.
print(f"\n{list_squared}")

list_pairs = [i for i in range(0, 21) if i % 2 == 0] # Genera una lista utilizando comprensión con los números pares del 0 al 20.
print(f"\n{list_pairs}")

list_celsius = [0, 10, 20, 30, 40]
list_fahrenheit = [(temp * 9/5) + 32 for temp in list_celsius] # Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.
print(f"\n{list_fahrenheit}")

text = "Hola, Python!"
list_chars = [char for char in text] # Crea una lista utilizando comprensión con los caracteres de una cadena.
print(f"\n{list_chars}")

list_words = ["Python", "es", "genial", "y", "divertido"]
list_long_words = [word for word in list_words if len(word) > 4] # Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.
print(f"\n{list_long_words}")

def add_five(num):
    return num + 5
list_numbers = [add_five(i) for i in range(1, 11)] # Aumenta en 5 cada número de una lista con comprensión usando una función externa.
print(f"\n{list_numbers}")

list_numbers = [1, 5, 10, 15, 20]
list_greater_than_10 = [num > 10 for num in list_numbers] # Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.
print(f"\n{list_greater_than_10}")

other_list = [i * 3 for i in range(1, 11) if i % 2 != 0] # Multiplica solo los números impares por 3 en una lista utilizando comprensión.
print(f"\n{other_list}")

list_matrix = matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)] # Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.
print(f"\n{list_matrix}")