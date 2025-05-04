"""
1. Crea una función que reciba una función y un número, y 
    devuelva el resultado de aplicar la función al número. 

2. Crea una función que reciba dos números y una función, y 
    devuelva el resultado de sumar los dos números y aplicar 
    la función. 

3. Crea una función que devuelva otra función que sume un 
    número fijo. 

4. Usa map() con lambda para multiplicar cada número de una 
    lista por 10. 

5. Usa filter() con lambda para quedarte solo con los 
    números pares. 

6. Usa reduce() con lambda para obtener la suma total de 
    una lista. 

7. Escribe una función que devuelva una función que reciba 
    un nombre y devuelva "Hola, ". 

8. Crea una función que reciba una lista y una función, y 
    cuente cuántos elementos cumplen con la función. 

9. Crea una función que reciba dos funciones y un número, y 
    las aplique en orden. 

10. Crea una función que reciba una lista y una 
    función, y aplique esa función a cada elemento usando un 
    bucle (sin map). 
"""

from functools import reduce

def apply_fun(value, fun): # Funcion que retorna el resultado de aplicar la funcion al numero ingresado
    return fun(value)
print(apply_fun(7, lambda x: x - 2))

def sum_two_values(value1, value2, fun): # Funcion que retorna el resultado de aplicar una funcion a dos numeros
    return fun(value1 + value2)
print(f"\n{sum_two_values(2, 3, lambda num: num ** 2)}")

def sum_five(value): # Funcion que devuelve una funcion que suma un valor fijo
    return lambda x: x + value
print(f"\n{sum_five(5)(5)}")

list_numbers = [1, 2, 3, 4, 5]
print(f"\n{list(map(lambda num: num * 10, list_numbers))}") # Uso de map con un lambda para multiplicar los numeros de una lista

print(f"\n{list(filter(lambda num: num % 2 == 0, list_numbers))}") # Uso de filter con un lambda para solo quedarse con los numeros pares

print(f"\n{reduce(lambda num1, num2: num1 + num2, list_numbers)}") # Uso de reduce con un lambda para sumar los numeros de una lista

def greeting(): # Funcion que retorna otra funcion que retorna un saludo
    return lambda name: "Hola, " + name
print(f"\n{greeting()("Manuel")}")

def count_pairs(list_number, fun): # Funcion que retorna una funcion que suma en uno el total cada que un elemento cumple la condicion lambda
    return sum(1 for num in list_number if fun(num))
print(f"\n{count_pairs(list_numbers, lambda x: x % 2 == 0)}")

def apply_two_function(num, fun1, fun2): # Funcion que recibe dos funciones y las aplica en orden
    return fun2(fun1(num))
print(f"\n{apply_two_function(5, lambda x: x + 5, lambda y: y + 5)}")

def apply_fun_list(lst, fun): # Funcion que aplica una funcion de tipo map manualmente a una lista
    result = []
    for element in lst:
        result.append(fun(element))
    return result
print(f"\n{apply_fun_list(list_numbers, lambda num: num ** 2)}")