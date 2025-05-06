"""
1. Crea un archivo de texto y escribe en él la frase "Hola 
    desde Python". 

2. Abre un archivo y lee todo su contenido. 

3. Añade una nueva línea al final del archivo con el texto 
    "Línea añadida". 

4. Lee solo los primeros 10 caracteres del archivo. 

5. Usa seek para volver al inicio del archivo y leer desde 
    ahí. 

6. Lee e imprime el contenido línea por línea usando 
    readline. 

7. Lee todas las líneas del archivo en una lista y 
    recórrelas con un bucle. 

8. Crea un archivo nuevo que sobrescriba si ya existe, y 
    escribe varias líneas. 

9. Usa una función para abrir un archivo, escribir texto y 
    cerrarlo automáticamente con with. 

10. Lee un archivo línea por línea y muestra solo las 
    que contienen la palabra "Python".
"""

with open("file.txt", "w") as file: # Crea o escribe en un archivo una linea de texto
    file.write("Hola desde Python")

with open("file.txt", "r") as file: # Lee un archivo
    print(file.read())

with open("file.txt", "a") as file: # Agrega una nueva linea de texto al archivo
    file.write("\nLínea añadida.")

with open("file.txt", "r") as file: # Lee los 10 primeros caracteres del archivo
    print(file.read(10))

with open("file.txt", "r") as file: # Regresa a la primera linea del archivo y lee desde ahi
    file.seek(0)
    print(file.read())

with open("file.txt", "r") as file: # Lee linea a linea el archivo
    print(file.readline())
    print(file.readline())

with open("file.txt", "r") as file: # Lee el archivo linea a linea desde una lista
    content = file.readlines()
    for line in content:
        print(line)

with open("file.txt", "w") as file: # Reescribe el archivo
    file.writelines(["Estoy\n", "Aprendiendo\n", "Python\n"])

with open("file.txt", "r") as file: # Muestra las lineas que contengan python
    content = file.readlines()
    for line in content:
        if "python" in line.lower():
            print(line)