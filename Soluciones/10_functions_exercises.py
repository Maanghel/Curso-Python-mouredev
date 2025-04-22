"""
1. Crea una función llamada "personalized_greeting" que 
    reciba un nombre como argumento e imprima "Hola, 
    <nombre>". Si no se proporciona ningún nombre, debe 
    saludar diciendo "Hola, desconocido". 

2. Escribe una función llamada "multiply" que reciba dos 
    números como argumentos y retorne el resultado de 
    multiplicarlos. 

3. Crea una función llamada "is_even" que reciba un número 
    entero como argumento y retorne True si es par y False 
    si es impar. 

4. Escribe una función llamada "convert_to_uppercase" que 
    reciba una cadena de texto y la retorne en mayúsculas. 

5. Crea una función llamada "arbitrary_sum" que reciba un 
    número arbitrario de números como argumentos y retorne 
    la suma de todos ellos. 

6. Escribe una función llamada "generate_full_greeting" que 
    reciba dos argumentos: nombre y apellido, y retorne el 
    saludo completo "Hola, <nombre> <apellido>". Los 
    argumentos deben ser pasados por clave. 

7. Crea una función llamada "power" que reciba dos números: 
    base y exponente, y retorne el resultado de elevar la 
    base al exponente. 

8. Escribe una función llamada "calculate_average" que 
    reciba tres números y retorne su promedio. 

9. Crea una función llamada "count_characters" que reciba 
    una cadena de texto y retorne el número de caracteres 
    que contiene. 

10. Escribe una función llamada "display_messages" que 
    reciba un número indefinido de cadenas y las imprima en 
    mayúsculas, una por una, tal como se hizo en el archivo 
    proporcionado.
"""

def personalized_greeting(name):
    print(f"Hola, {name}!")
personalized_greeting("Manuel")

def multiply(value1, value2):
    return value1 * value2
print(f"\n{multiply(2, 2)}")

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(f"\n{is_even(2)}")

def convert_to_uppercase(text):
    return text.upper()
print(f"\n{convert_to_uppercase("Hola Python")}")

def arbitrary_sum(*numbers):
    return sum(numbers)
print(f"\n{arbitrary_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")

def generate_full_greeting(first_name, last_name):
    print(f"\nHola {first_name} {last_name}!")
generate_full_greeting(first_name= "Manuel", last_name= "Gamez")

def power(base, exponent):
    return base ** exponent
print(f"\n{power(2, 3)}")

def calculate_average(value1, value2, value3):
    return (value1 + value2 + value3) / 3
print(f"\n{calculate_average(2, 5, 2)}")

def count_characters(text):
    return len(text)
print(f"\n{count_characters("Hola, Python")}")

def display_messages(*texts):
    print()
    for text in texts:
        print(text.upper())
display_messages("hola", "manuel", "gamez")