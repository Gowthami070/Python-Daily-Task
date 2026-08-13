#1.Create a class Person with the attribute name. Create a child class Employee with the attribute salary. Create another child class Manager that inherits from Employee and has the attribute department. Display all the details.
'''
Input
Ravi
50000
HR
Output
Name: Ravi
Salary: 50000
Department: HR
'''
#
'''
class Person:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print("Name:",self.name)
        
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
    def display_salary(self):
        print("Salary:",self.salary)
        
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display_dept(self):
        print("Department:",self.department)
        
m=Manager("Ravi",50000,"HR")
m.display_name()
m.display_salary()
m.display_dept()
'''

#2.Create a class Vehicle with the attribute brand. Create a child class Car with the attribute model. Create another child class ElectricCar with the attribute battery_capacity. Display all the details.
'''
Input
Tesla
Model 3
75
Output
Brand: Tesla
Model: Model 3
Battery Capacity: 75 kWh
'''
#
'''
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    def display_brand(self):
        print("Brand:",self.brand)
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def display_model(self):
        print("Model:",self.model)
class ElectricCar(Car):
    def __init__(self,brand,model,battery_capasity):
        super().__init__(brand,model)
        self.battery_capasity=battery_capasity
    def display_battery(self):
        print("Battery Capasity:",self.battery_capasity)
e=ElectricCar("Tesla","Model 3","75 kWh")
e.display_brand()
e.display_model()
e.display_battery()

'''
#3.Create a class Product with the attribute product_name. Create another class Price with the attribute price. Create a child class Bill that inherits from both classes. Read the GST percentage and display the final bill amount.
'''
Input
Laptop
50000
18
Output
Product: Laptop
Price: 50000
Final Bill: 59000.0
'''
class Product:
    def __init__(self, name):
        self.__name = name

    def display(self):
        print("Product:", self.__name)


class Price:
    def __init__(self, price):
        self.price = price

    def display_price(self):
        print("Price:", self.price)


class Bill(Product, Price):
    def __init__(self, name, price):
        Product.__init__(self, name)
        Price.__init__(self, price)

    def gst(self, gst):
        gst_amount = self.price * (gst / 100)
        final_bill = self.price + gst_amount
        print("Final Bill:", final_bill)


b = Bill("Laptop", 50000)

b.display()
b.display_price()
b.gst(18)
#4.Create a class Player with the attribute player_name. Create another class Sport with the attribute sport_name. Create a child class Athlete that inherits from both classes. Display the player details.
'''
Input
Virat Kohli
Cricket
Output
Player: Virat Kohli
Sport: Cricket
'''
#
'''
class Player:
    def __init__(self,name):
        self.__name=name
    def display_name(self):
        print("Player:",self.__name)
class Sport:
    def __init__(self,names):
        self.__names=names
    def display_names(self):
        print("Sport:",self.__names)
class Athlete(Player,Sport):
    def __init__(self, name, names):
        Player.__init__(self, name)
        Sport.__init__(self, names)
ob=Athlete("Virat Kohli","Cricket")
ob.display_name()
ob.display_names()
'''
