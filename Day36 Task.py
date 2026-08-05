#1. Write a Python program to create a class Student that stores the student's name and age. Create an object of the class and display the student's details.
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
        self.name=name
        self.age=age
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
s=Student("John",21)
s.display()
'''
#2.Write a Python program to create a class Rectangle that stores the length and breadth. Create an object and calculate the area of the rectangle.
'''
Input:
5
8
Output:
Area: 40
'''
#
'''
class Rechangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def display(self):
        print(self.length*self.bredth)
s=Rechangle(8,5)
s.display()
'''
#3.Write a Python program to create a class Calculator that stores two numbers. Create an object and find their sum.
'''
Input:
10
20
Output:
Sum: 30
'''
#
'''
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("Sum=",self.a+self.b)
s=Calculator(10,20)
s.display()
'''
#4.Write a Python program to create a class Employee that stores the employee's name and salary. Create an object and display the employee details.
'''
Input:
Rahul
45000
Output:
Employee Name: Rahul
Salary: 45000
'''
#
'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('Employee Name:',self.name)
        print('salary:',self.salary)
name=input("enter:")
salary=int(input("Enter:"))
s=Employee(name,salary)
s.display()
'''
#5.Write a Python program to filter all strings whose length is greater than 5 using the filter() function.
'''
Input:
apple mango cat elephant dog python
Output:
elephant python
'''
#
'''
def greater_length(word):
    return len(word)>5
string=input("Enter:")
word=string.split()
ob=filter(greater_length,word)
for i in ob:
    print(i)
'''
