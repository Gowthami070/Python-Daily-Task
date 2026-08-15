#1.Method Overriding
'''
Create a parent class Operation with a method calculate().
Create two child classes:

Addition → returns the sum of two numbers.
Multiplication → returns the product of two numbers.

Call calculate() using objects of both child classes.

Sample Input:10 5
Sample Output:
15
50
'''
#
'''
class Operation:
    def calculate(self):
        print("Performing addition and multi[plication")
class Addition(Operation):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate(self):
        return self.a+self.b
class Multiplication(Operation):
    super().__init__(a,b)
    def calculate(self):
        return self.a*self.b
a=Addition(10,5)
m=Multiplication(10,5)
print("Addition:",a.calculate())
print("Multiplication:",m.calculate())
'''
#
'''
class Operation:
    def calculate(self,a,b):
        pass
class Addition(Operation):
    def calculate(self,a,b):
        return a+b
class Multiplication(Operation):
    def calculate(self,a,b):
        return a*b
a=Addition()
m=Multiplication()
print(a.calculate(10,5))
print(m.calculate(10,5))
 '''   

#2.Number Pattern
'''
Create a parent class Number that accepts N.
Create a child class Pattern that inherits N and prints:
Sample Input:4
Sample Output:
1
1 2
1 2 3
1 2 3 4
'''


#3.Encapsulation – Hidden PIN Digit Sum
'''
Create a class SecurePin with a private variable __pin.
Create methods to:
Store a PIN number.
Return the sum of all digits in the PIN without directly accessing the private variable outside the class.
Sample Input:4826
Sample Output:20
'''
#
'''
class SecurePin:
    def __init__(self, pin):
        self.__pin = pin
    def digit_sum(self):
        total = 0
        for i in str(self.__pin):
            total = total + int(i)
        return total
pin = int(input("Enter Pin:"))
obj = SecurePin(pin)
print("Sum:",obj.digit_sum())
'''

#4.Inheritance – Digit Difference
'''
Create a parent class Number that stores a number.
Create a child class DigitDifference that inherits the number and finds the difference between the largest digit and smallest digit.
Sample Input:58321
Sample Output:7
'''
class Number:

n=int(input("Enter:"))
print(Number(n))
'''
5.Inheritance – Reverse Triangle Pattern
Create a parent class PatternInput that stores N.
Create a child class ReversePattern that inherits N and prints:

Sample Input:4
Sample Output:
4 4 4 4
3 3 3
2 2
1
'''
