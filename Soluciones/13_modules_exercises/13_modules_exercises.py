"""
1. Crea un módulo llamado "calculator" que contenga funciones 
    para sumar, restar, multiplicar y dividir dos números. 
    Importa este módulo en otro archivo y usa sus funciones. 

2. Crea un módulo llamado "converter" que tenga funciones 
    para convertir temperaturas entre Celsius y Fahrenheit. 
    Escribe un programa que importe este módulo y realice 
    conversiones. 

3. Crea un módulo que contenga una lista de nombres de 
    estudiantes y una función que imprima todos los nombres. 
    Importa este módulo en otro archivo y usa la función para 
    mostrar la lista. 

4. Crea un módulo llamado "geometry" que tenga una función 
    para calcular el área de un círculo y un cuadrado. Usa 
    este módulo en otro archivo para calcular áreas. 

5. Escribe un módulo que contenga una función que acepte 
    cualquier número de argumentos y devuelva su suma. Importa 
    y usa la función en otro archivo. 

6. Crea un módulo que defina una clase llamada "Car" con 
    propiedades como marca, modelo y año. Importa este módulo 
    en otro archivo y crea una instancia de la clase "Car". 

7. Escribe un módulo que contenga funciones para leer y 
    escribir en archivos de texto. Crea un programa que use 
    estas funciones para escribir y leer datos. 

8. Crea un módulo llamado "statistics" que tenga funciones 
    para calcular la media y la mediana de una lista de 
    números. Usa este módulo para calcular estos valores en 
    una lista dada. 

9. Crea un módulo que contenga una función para contar 
    cuántas veces aparece una palabra en un texto. Escribe un 
    programa que importe el módulo y lo use para contar 
    palabras en una cadena. 

10. Crea un módulo llamado "dates" que contenga funciones 
    para obtener la fecha actual y calcular la diferencia 
    entre dos fechas. Usa este módulo en un programa para 
    mostrar la fecha actual y la diferencia entre dos fechas 
    específicas.
"""

from calculator import addition, subtraction, multiplication, division
print(addition(4, 2))
print(subtraction(4, 2))
print(multiplication(4, 2))
print(division(4, 2))

from converter import convert_to_celsius, convert_to_fahrenheit
print(f"\n{convert_to_celsius(60)}")
print(convert_to_fahrenheit(32))

from list_names import print_names
print()
print_names()

from geometry import area_circle, area_square
print(f"\n{area_square(4)}")
print(area_circle(5))

from sum_list_number import sum_list
print(f"\n{sum_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")

from car_module import Car
my_car = Car("Chevrolet", "Malibu", 2004)
print(f"\n{my_car.information()}")

