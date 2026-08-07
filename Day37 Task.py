

#1.Write a Python program to create a class Bank A
'''
account that stores the account balance and deposit amount. Create an object and display the updated balance.
Input:
5000
1500
Output: Balance-6500
'''
#
'''
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
        else:
            print("Invalid amount")
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        if balance >= 0:
            self.__balance=balance
    
ob=BankAccount(5000)
print("Initial balance:",ob.get_balance())
ob.deposit(1500)
print("After deposit:",ob.get_balance())

'''
#2.Write a Python program to create a class Product that stores the product price and quantity. Create an object and calculate the total cost.
'''
Input:
250
4
Output:
Total Cost: 1000
'''
#
'''
class Product:
    def __init__(self,price,quantity):
        self.__price=price
        self.quantity=quantity
    def total_cost(self):
        return self.__price*self.quantity
    def get_calculate(self):
        return self.total_cost()
p=Product(250,4)
print("Total Cost:",p.get_calculate())
'''
#3.Write a Python program to create a class Temperature that stores the temperature in Celsius. Create an object and convert it to Fahrenheit.
'''
Input:25
Output: 77.0
'''
#
'''
class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def Fahrenheit(self):
        return (self.celsius*1.8)+32
    def get_calculate(self):
        return self.Fahrenheit()
t=Temperature(25)
print("The Fahrenheit temperature is:",t.get_calculate())
'''
#4.Write a Python program to create a class Student with private attributes name and age. Use a method to display the student's details.
'''
Input:
John
21
Output:
Name: John
Age: 21
'''
#
'''
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print("Name:",self.__name)
        print("Age:",self.__age)
    def get_display(self):
        return self.display()
s=Student("John",21)
print("Student Details")
s.get_display()
'''
#5.Write a Python program to create a class Employee with private attributes name and salary. Display the employee details using a method.
'''
Input:
Rahul
50000
Output:
Employee Name: Rahul
Salary: 50000
'''
#
'''
class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    def details(self):
        print("Employee Name:",self.__name)
        print("Salary:",self.__salary)
    def get_details(self):
        return self.details()
emp=Employee("Rahul",20000)
print("Employee details")
emp.get_details()
'''      














