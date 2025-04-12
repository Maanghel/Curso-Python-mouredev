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
print(len(text))

print("\nHola " + "Python")

new_text = "\nLinea\nde\nSalto"
print(new_text)

first_name = "Manuel"
last_name = "Gamez"
age = 29
print(f"\nFirst name = {first_name}\nLast name = {last_name}\nAge = {age}")

a, b, c, d, e, f = "Python"
print(f"\n{a}")
print(b)
print(c)
print(d)
print(e)
print(f)

other_text = "Programacion"
print(f"\nObteniendo los caracteres desde la posicion 3 hasta la 7 de la palabra 'Programacion':\n{other_text[3:8]}")

reverse_text = "Python"
print(f"\n{reverse_text[::-1]}")

upper_text = "aprendiendo python"
print(f"\n{upper_text.upper()}")

count_text = "Programacion en Python"
print(f"\n{upper_text.count("n")}")

numeric_text = "12345"
print(f"\n{numeric_text.isnumeric()}")