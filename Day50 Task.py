#1.Create two decorators: • add_prefix → adds "Message: " before the result. • uppercase → converts the result to uppercase. Apply both to a function that returns a message.
'''
Input hello python
Output Message: HELLO PYTHON
'''
#
'''
def add_prefix(func):
    def wrapper():
        result = func()
        return "Message: " + result
    return wrapper

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper
@add_prefix
@uppercase
def message():
    return "hello python"
print(message())
'''
#2.Create these decorators: remove_special_characters remove_spaces uppercase add_prefix Apply all four decorators to a function that accepts a sentence.
'''
Input Hello @ Python World!
Output TEXT: HELLOPYTHONWORLD
'''
#
'''
def remove_special_characters(func):
    def inner():
        result = func()
        result = ''.join(ch for ch in result if ch.isalnum() or ch.isspace())
        return result
    return inner
def remove_spaces(func):
    def inner():
        result = func()
        return result.replace(" ", "")
    return inner
def uppercase(fun):
    def inner():
        res=fun()
        return res.upper()
    return inner
def add_prefix(fun):
    def inner():
        res=fun()
        return "TEXT:"+res
    return inner
@remove_special_characters
@remove_spaces
@uppercase
@add_prefix 
def message():
    return "Hello @ Python World!"
print(message())
'''
#3.Given a list of numbers, use map() with a lambda function to create a new list containing their squares.
'''
Input [1, 2, 3, 4, 5]
Output [1, 4, 9, 16, 25]
'''
#
'''
nums = [1, 2, 3, 4, 5]
res = list(map(lambda x: x ** 2, nums))
print(res)
'''
#4.Use map() with lambda to convert every string in a list to uppercase.
'''
Input ["python", "java", "javascript"]
Output ["PYTHON", "JAVA", "JAVASCRIPT"]
'''
#
'''
language = ["python", "java", "javascript"]
res = list(map(lambda x: x.upper(), language))
print(res)
'''
#5.Use filter() and lambda to extract all even numbers from a list.
'''
Input [10, 15, 20, 25, 30, 35]
Output [10, 20, 30]
'''
#
'''
nums = [10, 15, 20, 25, 30, 35]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
'''
#6.Create a lambda function that accepts two numbers and returns the larger number.
'''
Input 25 40
Output 40
'''
#
'''
larger = lambda a, b: a if a > b else b
print(larger(25, 40))
'''
'''
Create a button with the text "Click Me". When the user clicks the button, display: Button Clicked!
Create a paragraph: Hello World and a button "Change Text". When the button is clicked, change the paragraph to: Welcome to JavaScript
Create a button called "Change Color". When the button is clicked, change the background color of the webpage.
Create a button called "Double Click Me". When the user double-clicks it, display: Double clicked
'''
