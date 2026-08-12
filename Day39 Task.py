#1.Create a Vehicle class with a method start() that prints "Vehicle started". Create a Car class that inherits from Vehicle and add a method drive() that prints "Car is driving".
'''
Expected Output:

Vehicle started
Car is driving
'''
#
'''
class Vehicle:
    def start(self):
        print("Vehicle is started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
c=Car()
c.start()
c.drive()
'''
#2.Create the following inheritance structure:
'''
Grandparent
     ↓
   Parent
     ↓
   Child

Each class should contain one method. Create a Child object and access all three methods.

Expected Output:

Grandparent method
Parent method
Child method
'''
#
'''
class Grandparent:
    def grand(self):
        print("Grandparent method")
class Parent(Grandparent):
    def parent(self):
        print("Parent method")
class Child(Parent):
    def child(self):
        print("Child method")
c=Child()
c.grand()
c.parent()
c.child()
'''
#3.Create:
'''
BankAccount
      ↓
SavingsAccount
      ↓
PremiumSavingsAccount

BankAccount should contain account number and balance.

SavingsAccount should contain interest rate.

PremiumSavingsAccount should contain cashback percentage.

Create an object of PremiumSavingsAccount and display all details.
'''
#
'''
class BankAccount:
    def __init__(self, accnum, balance):
        self.accnum = accnum
        self.balance = balance

    def display(self):
        print("Account number:", self.accnum)
        print("Account balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, accnum, balance, interest_rate):
        super().__init__(accnum, balance)
        self.interest_rate = interest_rate

    def display_interest(self):
        print("Interest rate:", self.interest_rate)


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, accnum, balance, interest_rate, cashback_percentage):
        super().__init__(accnum, balance, interest_rate)
        self.cashback_percentage = cashback_percentage

    def display_cashback(self):
        print("Cashback percentage:", self.cashback_percentage)


ob = PremiumSavingsAccount(12364478, 20000, 20, 10)

ob.display()
ob.display_interest()
ob.display_cashback()
'''
#4.Create a parent class:
'''
        Vehicle
       /       \
     Car       Bike

Vehicle should contain a method start().

Car should contain drive().

Bike should contain ride().

Create objects for both Car and Bike and access the appropriate methods.
'''
#
'''
class Vehicle:
    def start(self):
        print("Vehicle is started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")
c=Car()
c.start()
c.drive()
print('='*5)
b=Bike()
b.start()
b.ride()
'''  
#5.Design the following inheritance structure:
'''
             Person
            /      \
       Student    Employee
            \      /
             Intern

Implement this using Python classes.

Create an Intern object and access the required properties from the parent classes.

Also check the MRO using:

ClassName.mro()
'''
class Person:
    def person(self):
        print("IAm a person")
class Student(Person):
    def student(self):
        print("And IAm Student")
class Employee(Person):
    def emp(self):
        print("And IAm employee")
class Intern(Student,Employee):
    def intern(self):
        print("And IAm intern")

i=Intern()
i.person()
i.student()
i.emp()
i.intern()
print(Intern.mro())




























