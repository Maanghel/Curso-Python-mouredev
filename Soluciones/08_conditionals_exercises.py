"""
1. Escribe un programa que verifique si un número es 
    positivo, negativo o cero. 

2. Solicita al usuario que ingrese su edad y muestra un 
    mensaje indicando si es mayor de edad(18 años o más) o 
    menor de edad. 

3. Escribe un programa que verifique si una cadena de texto 
    está vacía y muestre un mensaje en consecuencia. 

4. Crea un programa que solicite dos números al usuario y 
    compare cuál es mayor. Si son iguales, muestra un 
    mensaje indicando la igualdad. 

5. Escribe un programa que verifique si un número es 
    divisible por 3 y por 5 al mismo tiempo. 

6. Solicita al usuario que ingrese un número y verifica si 
    es par o impar. 

7. Escribe un programa que determine si una persona puede 
    votar en función de su edad(mayor o igual a 18). Si 
    tiene 16 o 17 años, indica que puede votar con permiso 
    especial. 

8. Crea un programa que solicite una contraseña al usuario 
    y verifique si coincide con una contraseña predefinida. 
    Si no coincide, muestra un mensaje de error. 

9. Escribe un programa que determine si un número está 
    entre 10 y 20 (ambos incluidos). 

10. Escribe un programa que simule un semáforo: 
    solicita al usuario que ingrese un color(rojo, amarillo, 
    verde) y muestra un mensaje indicando si debe detenerse, 
    estar alerta o avanzar. 
"""

number = 0
if number > 0:
    print(f"El numero {number} es positivo.")
elif number < 0:
    print(f"El numero {number} es negativo.")
else:
    print(f"Es numero es 0")

age = int(input(f"\nIngrese su edad: "))
if age >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

my_string = ""
if not my_string:
    print("\nLa cadena de texto esta vacia.")
else:
    print("\nLa cadena de texto no esta vacia.")

number1 = int(input("\nIngrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
if number1 > number2:
    print(f"El numero {number1} es mayor que {number2}.")
elif number2 > number1:
    print(f"El numero {number2} es mayor que {number1}.")
else:
    print(f"El numero {number1} es igual al numero {number2}.")

my_number = int(input("\nIngrese un numero: "))
if my_number % 3 == 0 and my_number % 5 == 0:
    print(f"El numero {my_number} es divisible entre 3 y 5.")
else:
    print(f"El numero {my_number} no es divisible entre 3 y 5 al mismo tiempo.")

other_number = int(input("\nIngrese un numero: "))
if other_number % 2 == 0:
    print(f"El numero {other_number} es par.")
else:
    print(f"El numero {other_number} no es par.")

new_age = int(input("\nIngrese su edad: "))
if new_age >= 18:
    print("El ciudadano puede votar.")
elif new_age == 17 or new_age == 16:
    print("El ciudadano puede votar con un permiso especial.")
else:
    print("El ciudadano no puede votar.")

password = "12345"
user_password = input("\nIngrese la contraseña: ")
if user_password == password:
    print("Contraseña correcta. Iniciando sesion.")
else:
    print("Contraseña incorrecta. Intente nuevamente.")

other_other_number = int(input("\nIngrese un numero: "))
if other_other_number > 10 and other_other_number < 20:
    print(f"El numero {other_other_number} se encuentra entre el 10 y el 20.")
else:
    print(f"El numero {other_other_number} no se encuentra entre el 10 y el 20.")

color = input("\nIngrese un color de semaforo (rojo/verde/amarillo): ").lower()
if color == "verde":
    print(f"El semaforo esta en {color}. Puede avanzar.")
elif color == "amarillo":
    print(f"El semaforo esta en {color}. Este alerta.")
elif color == "rojo":
    print(f"El semaforo esta en {color}. Detengase.")
else:
    print(f"Color no valido.")