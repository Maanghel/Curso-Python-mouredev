"""
1. Genera un SyntaxError al imprimir una cadena sin 
    paréntesis. 

2. Genera un NameError intentando usar una variable no 
    definida. 

3. Genera un IndexError accediendo a un índice inexistente 
    de una lista. 

4. Genera un ModuleNotFoundError al importar un módulo 
    inexistente. 

5. Genera un AttributeError accediendo a un atributo que no 
    existe. 

6. Genera un KeyError al acceder a una clave inexistente de 
    un diccionario. 

7. Genera un TypeError usando tipos incorrectos (índice 
    string en lista). 

8. Genera un ImportError al importar una función que no 
    existe desde un módulo. 

9. Genera un ValueError intentando convertir un string no 
    numérico a entero. 

10. Intenta detectar si un error ocurre usando try
    except con un KeyError. 
"""

# print(Hola, Python!) Genera un SyntaxError
print("Hola, Python!")

# print(num) Genera un NameError
num = 7
print(f"\n{num}")

num_list = [1, 2, 3, 4, 5]
# print(num_list[5]) Genera un IndexError
print(f"\n{num_list[0]}")

# import mathh Genera un ModuleNotFoundError
import math

# print(math.PI) Genera un AttributeError
print(f"\n{math.pi}")

age_dict = {"Manuel": 29, "Juan": 25, "Ana": 26}
# print({age_dict["Pedro"]}) Genera un KeyError
print(f"\n{age_dict["Manuel"]}")

text = "Hola"
# print(text + 4) Genera un TypeError
print(f"\n{text + " Python"}")

# from math import PI Genera un ImportError
from math import pi

# print(int("Hola")) Genera un ValueError
print(f"\n{int("0")}")

try:
    print(age_dict["Pedro"])
except KeyError:
    print(f"\nOcurrio un error.")