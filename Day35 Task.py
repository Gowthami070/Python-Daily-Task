'''
1.Instructions
Write the program using user-defined functions only. 
Do not use external libraries. 
Take the input as a single string from the user. 
Display all the following details. 
Write a Python program using functions to analyze the given text and perform the following operations.
Input
  Python Programming 2026 is Awesome!! Python is Easy. 123  
Output
Original String:
Python Programming 2026 is Awesome!! Python is Easy. 123
After Removing Extra Spaces:Python Programming 2026 is Awesome!! Python is Easy. 123
Total Characters: 52
Total Words: 8
Uppercase String:PYTHON PROGRAMMING 2026 IS AWESOME!! PYTHON IS EASY. 123
Lowercase String:
python programming 2026 is awesome!! python is easy. 123
Title Case:Python Programming 2026 Is Awesome!! Python Is Easy. 123
Swap Case: pYTHON pROGRAMMING 2026 IS aWESOME!! pYTHON IS eASY. 123
Number of Vowels: 16
Number of Digits: 7
Number of Alphabets: 39
Number of Special Characters: 5   
Frequency of Each Word:
Python : 2
Programming : 1
2026 : 1
is : 2
Awesome!! : 1
Easy. : 1
123 : 1
Longest Word: Programming
Shortest Word: is
Starts with 'Python': True
Ends with '123': True
Index of 'Awesome': 27
Replace 'Python' with 'Java':
Java Programming 2026 is Awesome!! Java is Easy. 123
Reverse String: 321 .ysaE si nohtyP !!emosewA si 6202 gnimmargorP nohtyP
Palindrome:False
'''
def remove_extra_space(text):
    x=text.split()
    return " ".join(x)
def total_characters(text):
    cleaned=remove_extra_space(text)
    return len(cleaned)
def total_words(text):
    cleaned=remove_extra_space(text)
    return len(cleaned)
def main():
    text="  Python Programming 2026 is Awesome!! Python is Easy. 123"
    result=remove_extra_space(text)
    print(result)
    print("No.of characters=",total_characters(result))
    print("No.of words=",total_words(result))

main()
