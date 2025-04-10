"""
1. Declara y asigna valores a las siguientes variables: 
    name: una cadena que contenga tu nombre. 
    age: un número entero que represente tu edad. 
    height: un número flotante que represente tu altura. 
    Imprime cada variable en una línea separada. 

2. Convierte la variable edad de entero a cadena y 
    concatenala con un texto que diga cuántos años tienes. 

3. Declara una variable booleana is_student que indique si 
    eres estudiante o no. Usa True o False según corresponda 
    e imprímela. 

4. Usa la función len() para calcular cuántos caracteres 
    tiene tu nombre completo, almacenado en una variable. 

5. Declara tres variables en una sola línea que representen 
    tu nombre, apellido y ciudad de origen. Luego, imprime 
    estos valores. 

6. Usa la función input() para solicitar al usuario su 
    color favorito y almacénalo en una variable color. 
    Luego, imprime el valor ingresado. 

7. Declara una variable fruit e inicialízala con un valor. 
    Luego, cambia el valor de la fruta a otro diferente y 
    vuelve a imprimirla. 

8. Convierte un número decimal, almacenado en la variable 
    price, a un número entero y luego imprímelo. 

9. Declara una variable llamada address_len y almacena en 
    ella la cantidad de caracteres de una dirección usando 
    la función len(). Imprime el resultado. 

10. Usa un tipo de dato forzado para declarar una 
    variable phone, asegurándote de que siempre será un 
    número. Luego, cambia su valor a un número diferente y 
    verifica el tipo de la variable con type().
"""

name = "Manuel"
age = 29
height = 1.81
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")

print("\nTengo " + str(age) + " años")

is_student = True
print(f"\n¿Eres estudiante? {is_student}")

my_name = "Manuel Gamez"
print(f"\nMi nombre completo tiene {len(my_name)} caracteres")

first_name, last_name, city = "Manuel", "Gamez", "Mexico"
print(f"\nFirst Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"City: {city}")

color = input("\n¿Cual es su color favorito? ")
print(f"Color favorito: {color}")

fruit = "Manzana"
print(f"\nFruta: {fruit}")
fruit = "Pera"
print(f"Fruta: {fruit}")

price = 25.3
print(f"\n{int(price)}")

address_len = "AV DE LA PATRIA Nº 952, CENTRO CIVICO"
print(f"\nTiene {len(address_len)} caracteres")

phone: int = 6645124875
print(f"\n{type(phone)}")
phone = 6631425186
print(type(phone))