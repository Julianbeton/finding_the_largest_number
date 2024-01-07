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
    elif second_number >= first_number and second_number >= third_number:
        largest_number = second_number
    else: 
        largest_number = third_number

#Display the largest number
    print("The Largest Number is:", largest_number)

finding_the_largest_number()