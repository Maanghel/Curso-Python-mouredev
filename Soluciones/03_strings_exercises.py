"""
1. Declara una variable text con la frase “Aprendiendo 
    Python” y luego imprime la longitud de la cadena usando 
    len(). 

2. Concatena dos cadenas: “Hola” y “Python”, y muestra el 
    resultado en una sola línea. 

3. Crea una cadena que incluya un salto de línea, y luego 
    imprímela para ver el resultado. 

4. Usa el formateo de cadenas con f-strings para imprimir 
    tu nombre, apellido y edad en una cadena de texto. 

5. Desempaqueta los caracteres de la palabra “Python” en 
    variables separadas y luego imprímelos uno por uno. 

6. Extrae un “slice” de la palabra “Programación” para 
    obtener los caracteres desde la posición 3 hasta la 7. 

7. Invierte la cadena “Python” usando slicing y muestra el 
    resultado. 

8. Convierte la cadena “aprendiendo python” en mayúsculas 
    usando el método adecuado e imprímela. 

9. Cuenta cuántas veces aparece la letra “n” en la cadena 
    “Programación en Python”. 

10. Verifica si la cadena “12345” es numérica usando el 
    método adecuado e imprime el resultado.
"""

text = "Aprendiendo Python"
print(len(text)) # Nos indica cuantos caracteres tiene la variable

print("\nHola " + "Python") # Concatena dos strings

new_text = "\nLinea\nde\nSalto" # Hace uso de la secuencia de escape \n la cual crea una nueva linea
print(new_text)

first_name = "Manuel"
last_name = "Gamez"
age = 29
print(f"\nFirst name = {first_name}\nLast name = {last_name}\nAge = {age}")

a, b, c, d, e, f = "Python" # Empaqueta todo el string en una serie de variables
print(f"\n{a}")
print(b)
print(c)
print(d)
print(e)
print(f)

other_text = "Programacion"
print(f"\nObteniendo los caracteres desde la posicion 3 hasta la 7 de la palabra 'Programacion':\n{other_text[3:8]}") # Se usa el slicing para obtener ciertos valores del texto

reverse_text = "Python"
print(f"\n{reverse_text[::-1]}") # Invierte el string

upper_text = "aprendiendo python"
print(f"\n{upper_text.upper()}") # Convierte en mayusculas un string

count_text = "Programacion en Python"
print(f"\n{upper_text.count("n")}") # Cuenta la cantidad de ocasiones que se encuentra un valor

numeric_text = "12345"
print(f"\n{numeric_text.isnumeric()}") # Verifica si la variable es numerica