#1. Student Marks Analysis (Dictionary of Lists)
'''
Each student has marks in five subjects.
students = {
    "Rahul": [78, 85, 90, 88, 92],
    "Priya": [95, 89, 91, 90, 94],
    "Arun": [70, 72, 68, 75, 80]}

Write a function student_analysis(data) to print:
Student with the highest total marks
Student with the highest average
Students who scored above 80 in at least 3 subjects
'''
#
def student_analysis(students):
    highest_total = 0
    highest_average = 0
    student_highest_total = ""
    student_highest_average = ""
    students_above_80 = []

    for student, marks in students.items():
        total_marks = sum(marks)
        average_marks = total_marks / len(marks)

        if total_marks > highest_total:
            highest_total = total_marks
            student_highest_total = student

        if average_marks > highest_average:
            highest_average = average_marks
            student_highest_average = student

        if sum(1 for mark in marks if mark > 80) >= 3:
            students_above_80.append(student)

    print("Student with the highest total marks:", student_highest_total)
    print("Student with the highest average:", student_highest_average)
    print("Students who scored above 80 in at least 3 subjects:", students_above_80)
students = {
    "Rahul": [78, 85, 90, 88, 92],
    "Priya": [95, 89, 91, 90, 94],
    "Arun": [70, 72, 68, 75, 80]}
student_analysis(students)
#2.Library Management (Dictionary of Tuples)
'''
library = {
    "Python":("John",5),
    "Java":("James",2),
    "SQL":("David",0)}

Write a function library_report(data) to print:
Available books
Out-of-stock books
Book with maximum copies
'''
#
'''
def library_report(library):
    available_books = []
    out_of_stock_books = []
    max_copies_book = None
    max_copies = 0

    for book, (author, copies) in library.items():
        if copies > 0:
            available_books.append(book)
        else:
            out_of_stock_books.append(book)

        if copies > max_copies:
            max_copies = copies
            max_copies_book = book

    print("Available books:", available_books)
    print("Out-of-stock books:", out_of_stock_books)
    print("Book with maximum copies:", max_copies_book, "with", max_copies, "copies")
library = {
    "Python":("John",5),
    "Java":("James",2),
    "SQL":("David",0)}
library_report(library)
'''
#3.Write a Python program to find the key whose list has the maximum sum in a dictionary of lists.
'''
Sample Input:

data = {
    "A": [10, 20, 30],
    "B": [15, 25, 35],
    "C": [40, 10]}

Sample Output:
Key : B
Sum : 75
'''
#
'''
data = {
    "A": [10, 20, 30],
    "B": [15, 25, 35],
    "C": [40, 10]
}

maximum_key = ""
maximum_sum = 0

for key in data:
    total = sum(data[key])

    if total > maximum_sum:
        maximum_sum = total
        maximum_key = key

print("Key :", maximum_key)
print("Sum :", maximum_sum)
'''
#4.Write a Python program to find the frequency of every element in a nested list.
'''
Sample Input:
data = [
    [1,2,3],
    [2,3,4],
    [1,2]
]

Sample Output:
1 : 2
2 : 3
3 : 2
4 : 1
'''
#
'''
data = [
    [1, 2, 3],
    [2, 3, 4],
    [1, 2]
]

frequency = {}

for sublist in data:
    for element in sublist:

        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

for key in frequency:
    print(key, ":", frequency[key])
'''
#5.Write a Python program to count the total number of vowels present in all strings of a nested list?
'''
Sample Input:

data = [
    ["apple","banana"],
    ["orange"],
    ["kiwi","grapes"]
]

Sample Output:

Total Vowels : 13
'''
#
'''
data = [
    ["apple","banana"],
    ["orange"],
    ["kiwi","grapes"]
]
count=0
for sub in data:
    for s in sub:
        for char in s:
            if char in "aeiouAEIOU":
                count+=1
print("Total Vowels :", count)
'''