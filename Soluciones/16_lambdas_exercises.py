"""
1. Crea una lambda que sume dos números. 

2. Crea una lambda que calcule el cuadrado de un número. 

3. Crea una lambda que devuelva el mayor de dos números. 

4. Crea una lambda que sume 10 a un número dado. 

5. Crea una lambda que devuelva el último carácter de una 
    cadena. 

6. Crea una lambda que indique si una palabra tiene más de 
    6 letras. 

7. Crea una lambda que convierta una cadena a minúsculas. 

8. Crea una lambda que devuelva True si un número es 
    positivo. 

9. Crea una lambda que devuelva "Cadena vacía" si el string 
    está vacío. 

10. Crea una lambda que calcule el precio final con un 
    impuesto añadido del 21%. 
"""

# Uso de lambdas las cuales son funciones anonimas

sum_two_values = lambda num1, num2: num1 + num2
print(f"{sum_two_values(10, 20)}")

square_number = lambda num: num ** 2
print(f"\n{square_number(5)}")

greater_number = lambda num1, num2: num1 if num1 > num2 else num2
print(f"\n{greater_number(10, 20)}")

sum_ten = lambda num: num + 10
print(f"\n{sum_ten(5)}")

last_char = lambda string: string[-1]
print(f"\n{last_char('Python')}")

more_than_six = lambda word: len(word) > 6
print(f"\n{more_than_six('Python')}")

converto_to_lower_case = lambda string: string.lower()
print(f"\n{converto_to_lower_case('PYTHON')}")

is_positive = lambda num: num > 0
print(f"\n{is_positive(-1)}")

is_empty_string = lambda string: "Cadena vacía" if not string else string
print(f"\n{is_empty_string('')}")

final_price = lambda price: price * 1.21
print(f"\n{final_price(100)}")