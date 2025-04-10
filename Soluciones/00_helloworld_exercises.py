"""
1. Imprime "¡Hola Mundo!" por consola. 

2. Escribe un comentario de una sola línea explicando qué 
    hace el código del Ejercicio 1. 

3. Imprime tu nombre y edad en la misma línea utilizando la 
    función print. 

4. Usa la función type() para imprimir el tipo de dato de 
    una cadena de texto, un número entero y un número 
    decimal. 

5. Escribe un comentario en varias líneas explicando qué 
    son los tipos de datos en Python. 

6. Imprime el resultado de concatenar dos cadenas de texto, 
    por ejemplo: "Hola" y "Mundo". 

7. Crea una variable para almacenar tu nombre, otra para tu 
    edad, e imprime ambas en la misma línea. 

8. Escribe un programa que solicite al usuario su nombre y 
    lo imprima junto con un saludo. 

9. Usa print() para mostrar el resultado de la suma de dos 
    números enteros y el tipo de dato resultante. 

10. Comenta el código del Ejercicio 9, y explica qué 
    hace cada línea usando comentarios de una sola línea.
"""

print("¡Hola Mundo!")
# Imprimimos ¡Hola Mundo! en la terminal por medio de la función print

print("\nMi nombre es Manuel y tengo 29 años")

print("\n",type("Python"))
print(type(7))
print(type(3.0))

"""
Son categorias que nos permiten definir cómo se almacenan o 
manipulan los datos, dentro los mas comunes tenemos:
- str: Para cadenas de texto
- int: Para valores enteros
- float: Para valores decimales
- bool: Para valores booleanos (True/False)
"""

print("\nHola" + " " + "Mundo")

nombre = "Manuel"
edad = 29
print(f"\nMi nombre es {nombre} y tengo {edad} años")

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

suma = 2 + 2 # Creamos una variable que tiene como valor el resultado de una suma
print(f"El resultado de la suma es: {suma}") # Imprimimos el resultado de la suma
print(f"El tipo de dato del resultado es: {type(suma)}") # Imprimimos el tipo de dato mediante la funcion type