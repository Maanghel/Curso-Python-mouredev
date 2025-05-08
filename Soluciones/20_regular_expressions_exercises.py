"""
1. Busca si una cadena empieza por "Hola". 

2. Busca la palabra "Python" en una cadena aunque esté en 
    minúsculas. 

3. Encuentra todas las apariciones de la palabra "curso" en 
    una cadena. 

4. Reemplaza todas las apariciones de "lección" por 
    "LECCIÓN". 

5. Divide un texto en partes separadas por comas. 

6. Busca la primera palabra que comience con "A" o "a". 

7. Encuentra todas las palabras en una cadena que terminen 
    en "ción". 

8. Verifica si una cadena contiene solo números. 

9. Reemplaza todos los números de una cadena por el texto 
    "[número]". 

10. Encuentra todas las palabras de 4 letras exactas en 
    una cadena.
"""

import re

text1 = "Hola a todos, esto es python!"
text2 = "Me gusta la programacion"
match1 = re.match("Hola", text1) # re.match busca si la cadena comienza con "Hola"
match2 = re.match("programacion", text2)
print(match1)
print(match2)

search1 = re.search("Python", text1, re.I) # re.I permite buscar sin importar mayúsculas o minúsculas
search2 = re.search("Python", text2, re.I)
print(f"\n{search1}")
print(search2)

text = "Este curso es sobre Python. Con este curso aprenderas mucho"
findall = re.findall("curso", text) # re.findall devuelve todas las ocurrencias de "curso"
print(f"\n{findall}")

text = "Esta leccion es buena, la leccion pasada tambien, y la leccion futura igual."
new_text = re.sub("leccion", "LECCION", text) # re.sub reemplaza todas las apariciones de "leccion"
print(f"\n{new_text}")

other_text = re.split(",", text) # re.split divide el texto por comas
print(f"\n{other_text}")

text = "En esta leccion aprenderas"
other_match = re.search(r"\b[aA]\w+", text) # Busca la primera palabra que comience con 'A' o 'a'
print(f"\n{other_match}")

other_findall = re.findall(r"\w+cion", text) # Busca todas las palabras que terminan en "cion"
print(f"\n{other_findall}")

number_Text = "1982472985"
result = re.fullmatch("\d+", number_Text) # re.fullmatch verifica que toda la cadena contenga solo dígitos
print(f"\n{result}")

new_number_text = re.sub("\d+", "[numero]", number_Text) # Reemplaza todos los números por "[numero]"
print(f"\n{new_number_text}")

last_text = "Esta leccion esta muy bien"
results = re.findall(r"\b\w{4}\b", last_text)  # re.findall busca palabras de exactamente 4 letras
print(f"\n{results}")