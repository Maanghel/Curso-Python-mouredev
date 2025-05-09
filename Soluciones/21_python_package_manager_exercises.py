"""
1. Importa el módulo math y muestra el valor de pi. 

2. Crea un array de números usando numpy y multiplícalo por 
    3. 

3. Muestra la versión instalada de numpy. 

4. Realiza una petición HTTP con requests a una API pública 
    y muestra el código de estado. 

5. Importa una función llamada sum_two_values desde un 
    paquete personalizado mypackage.arithmetics y utilízala. 

6. Usa pandas para crear un DataFrame con nombres en 
    español. 

7. Ejecuta el comando para instalar el paquete requests 
    desde la terminal. 

8. Usa requests para obtener datos de una API y extrae solo 
    los nombres de los primeros Pokémon. 

9. Muestra todos los paquetes instalados con pip desde la 
    terminal. 

10. Escribe una línea de código que muestre la ayuda 
    sobre el paquete numpy desde Python.
"""

import math
print(math.pi)

import numpy
array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"\n{array * 3}")

print(f"\n{numpy.version.version}")

import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/squirtle")
print(f"\n{response.status_code}")

from my_package_manager import arithmetics
print(f"\n{arithmetics.sum_two_values(2, 2)}")

import pandas
data = {"Nombre": ["Manuel", "Ana", "Jose", "Maria"]}
df = pandas.DataFrame(data)
print(f"\n{df}")

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5")
data = response.json()
names = [p["name"] for p in data["results"]]
print(f"\n{names}")

# pip list

# help(numpy)