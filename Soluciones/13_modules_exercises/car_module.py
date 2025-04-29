class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def information(self):
        return f"{self.brand} {self.model}, {self.year}"