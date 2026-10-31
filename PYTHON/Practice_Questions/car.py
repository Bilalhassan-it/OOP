class Car:
    def __init__(self, Brand, Model, Year):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year

    def display(self):
        print("Brand:" , self.Brand)
        print("Model:" , self.Model)
        print("Year:" , self.Year)


c1 = Car("Toyota", "Camry", 2020)
c2 = Car("Honda", "Civic", 2019)

c1.display()
c2.display()

