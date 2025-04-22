"""
1. Crea una clase llamada "Animal" que tenga una propiedad 
    "species" y un método "make_sound" que imprima un sonido 
    genérico. 

2. Modifica la clase "Animal" para que reciba la especie al 
    crear un objeto y almacénala en una propiedad pública. 
    Añade el método "make_sound" que imprima un sonido 
    dependiendo de la especie. 

3. Crea una clase llamada "Car" con las propiedades públicas 
    "brand" y "model". Además, debe tener una propiedad 
    privada "_speed" que inicialmente será 0. 

4. Añade a la clase "Car" un método llamado "accelerate" que 
    aumente la velocidad en 10 unidades. Añade también un 
    método "brake" que reduzca la velocidad en 10 unidades. 
    Asegúrate de que la velocidad no sea negativa. 

5. Crea una clase "Book" que tenga propiedades como "title" 
    (público) y "author" (privado). Añade un método para 
    obtener el autor y otro para cambiar el título del libro. 

6. Crea una clase "Estudiante" que tenga como propiedades su 
    nombre, apellido y una lista de notas. Añade un método 
    para calcular y devolver la nota media del estudiante. 

7. Crea una clase "BankAccount" con propiedades como "owner" 
    y "balance". Añade métodos para depositar y retirar 
    dinero, asegurándote de que no se pueda retirar más de lo 
    que hay en la cuenta. 

8. Crea una clase "Point" que represente un punto en el 
    espacio 2D con coordenadas "x" e "y". Añade un método que 
    calcule la distancia entre dos puntos. 

9. Crea una clase "Employee" que tenga propiedades como 
    "name", "hourly_wage" (pago por hora) y "hours_worked". 
    Añade un método que calcule el pago total basado en las 
    horas trabajadas y el salario por hora. 

10. Crea una clase "Store" que tenga una propiedad 
    "inventory" (una lista de productos). Añade un método para 
    agregar un producto al inventario y otro para mostrar 
    todos los productos disponibles. 
"""

class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        if self.species == "Perro":
            print(f"guau")
        elif self.species == "Gato":
            print(f"miau")
        elif self.species == "Cerdo":
            print(f"oink")
        else:
            print(f"El {self.species} esta haciendo ruido.")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._speed = 0
    
    def accelerate(self):
        self._speed += 10
    
    def brake(self):
        if self._speed < 10:
            self._speed = 0
        else:
            self._speed -= 10

class Book:
    def __init__(self, title, author):
        self.title = title
        self._author = author
    
    def get_author(self):
        return self._author
    
    def change_title(self, new_title):
        self.title = new_title

class Student:
    def __init__(self, first_name, last_name, *notes):
        self.first_name = first_name
        self.last_name = last_name
        self.notes = notes
    
    def calculate_average(self):
        return sum(self.notes) / len(self.notes)

