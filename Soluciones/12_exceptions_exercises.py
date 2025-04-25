"""
1. Crea una función que intente dividir dos números 
    proporcionados por el usuario. Usa try-except para 
    capturar cualquier error de división (por ejemplo, 
    división por cero). 

2. Crea una función que tome una cadena e intente 
    convertirla en un número entero. Usa try-except para 
    capturar cualquier error en la conversión. 

3. Crea una función que abra un archivo, lea su contenido y 
    maneje posibles errores (por ejemplo, archivo no 
    encontrado). Usa try-except para gestionar las 
    operaciones de archivos de forma segura. 

4. Crea una función que realice múltiples operaciones 
    (suma, resta, división, multiplicación) con dos números. 
    Usa try-except-else-finally para manejar errores y 
    asegurar que se imprima un mensaje final, 
    independientemente de los errores. 

5. Crea una función que le pida al usuario su edad y lance 
    un ValueError si la entrada no es un número entero 
    positivo. Usa el manejo de excepciones para gestionar la 
    entrada y lanzar excepciones personalizadas cuando sea 
    necesario. 

6. Crea una función que intente acceder a un elemento de 
    una lista por índice. Usa try-except para manejar el 
    caso donde el índice esté fuera de rango. 

7. Crea una función que use try-except para manejar 
    múltiples excepciones: ZeroDivisionError, ValueError y 
    TypeError. 

8. Crea una función que simule una transacción. Lanza una 
    excepción personalizada llamada InsufficientFundsError 
    si el saldo es menor que la cantidad a retirar. 

9. Crea una función que intente convertir una lista de 
    cadenas en enteros. Maneja cualquier error que surja 
    cuando una cadena no pueda convertirse. 

10. Crea una función que calcule la raíz cuadrada de un 
    número. Lanza un ValueError si el número es negativo.
"""

def division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("La division entre 0 no esta permitida.")

def convert_to_int(text):
    try:
        return int(text)
    except ValueError:
        print("No se puede convertir a entero.")

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Archivo no encontrado.")

def operations(num1, num2):
    try:
        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"Multiplicacion: {num1 * num2}")
        print(f"Division: {num1 / num2}")
    except ZeroDivisionError:
        print("La division entre 0 no esta permitida.")
    else:
        print("Todas las operaciones se realizaron correctamente.")
    finally:
        print("Se termino de operar.")

def get_age():
    try:
        age = int(input("Ingrese su edad: "))
        if age <= 0:
            raise ValueError("La edad no debe ser un numero negativo.")
        return age
    except ValueError as e:
        print(f"Error: {e}")

def get_element_list(list, index):
    try:
        return list[index]
    except IndexError:
        print("El indice esta fuera de rango.")

def division_with_more_exceptions(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

def InsufficientFundsError(Exception):
    pass

def convert_list_to_int(string_list):
    number_list = []
    for string in string_list:
        try:
            number_list.append(int(string))
        except ValueError:
            print(f"Error: '{string}' no se puede transformar en un entero.")
    return number_list

def square_root(number):
    try:
        if number < 0:
            raise ValueError("No se puede obtener la raiz cuadrada de un numero negativo.")
        return number ** 0.5
    except ValueError as e:
        print(f"Error: {e}")
print(square_root(-2))