#1.Write a generator that yields each unique character and its frequency in the given string.
'''
Input: banana
Output:
b 1
a 3
n 2
'''
def frequency_generator(text):
    visited = []
    for ch in text:
        if ch not in visited:
            count = 0

            for i in text:
                if ch == i:
                    count += 1
            visited.append(ch)
            yield ch, count
text = input("Enter: ")
for char, frequency in frequency_generator(text):
    print(char, frequency)
#2.write a generator that yields all leap years between two given years
"""
input:2000
2020
output: 2000 2004 2008 2012 2016 2020
"""
#
'''
def leap_year(start,end):
    for i in range(start,end+1):
        if (i%4==0 and i%100!=0) or i%400==0:
            yield i
            
start=int(input("Enter:"))
end=int(input("Enter:"))
for year in leap_year(start, end):
    print(year, end=" ")
'''
#3.Create a class Temperature with a private attribute __temp. Display whether the temperature is valid (greater than or equal to -273).
'''
Input:
25
Output:
Valid Temperature
'''
#
'''
class Temperature:
    def __init__(self,temp):
        self.__temp=temp
    def display(self): 
        if self.__temp >=-273:
            print("Valid Temperature")
        else:
            print("Not a Valid Temperature")


temp=int(input("Enter temp:"))
t=Temperature(temp)
t.display()
'''
#4.Create a class Wallet with a private attribute __balance. Deduct the purchase amount if sufficient balance exists.
'''
Input
3000
1200
Output
Payment Successful
Remaining Balance: 1800
'''
#
'''
class Wallet:
    def __init__(self,balance,purchase_amt):
        self.__balance=balance
        self.purchase_amt=purchase_amt
    def display(self):
        if self.__balance>purchase_amt:
            self.__balance-=purchase_amt
            print("Payment Successful")
            print("Remaining Balance:",self.__balance)
        else:
            print("Insufficient balance")

balance=int(input("Enter balance:"))
purchase_amt=int(input("Enter amount:"))
w=Wallet(balance,purchase_amt)
w.display()
'''
#5.Create a class Student with instance attributes name and marks. Use an instance method to display whether the student has passed (marks ≥ 35).
'''
Input
Rahul
78
Output
Rahul Passed
'''
#
'''
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        if self.marks>=35:
            print(self.name,"Passed")
        else:
            print(self.name,"Fail")
name=input("Enter name:")
marks=int(input("Enter name:"))
s=Student(name,marks)
s.display()
'''










