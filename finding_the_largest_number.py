#Assignment 4
#Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

#pseudocode
#import tkinter
import tkinter as tk
from tkinter import messagebox

#function
def finding_the_largest_number():
#ask user to input number 1
    first_number = float(input("Input the first number: "))
#ask user to input number 2
    second_number = float(input("Input the second number: "))
#ask user to input number 3
    third_number = float(input("Input the third number: "))
#find the largest number among the 3 numbers
    if first_number >= second_number and first_number >= third_number:
        largest_number = first_number
        first_number_is_the_largest = f"The Largest Number is the First Number:{largest_number}. The First Number:{first_number} is Greater Than {second_number} and {third_number}."
        print(first_number_is_the_largest)
        
    elif second_number >= first_number and second_number >= third_number:
        largest_number = second_number
        second_number_is_the_largest = f"The Largest Number is the Second Number:{largest_number}. The Second Number:{second_number} is Greater Than {first_number} and {third_number}."
        print(second_number_is_the_largest)

    else: 
        largest_number = third_number
        third_number_is_the_largest = f"The Largest Number is the Third Number:{largest_number}. The Third Number:{third_number} is Greater Than {first_number} and {second_number}"
        print(third_number_is_the_largest)


finding_the_largest_number()