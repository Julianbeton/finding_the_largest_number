#Assignment 4

#Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

#pseudocode

#import customtkinter
import tkinter as tk
from tkinter import messagebox

#function
def finding_the_largest_number():
#ask user to input number 1
    first_number = float(first_number_entry.get())
#ask user to input number 2
    second_number = float(second_number_entry.get())
#ask user to input number 3
    third_number = float(third_number_entry.get())
#find the largest number among the 3 numbers
    if first_number >= second_number and first_number >= third_number:
        largest_number = first_number
        result = f"The Largest Number is the First Number: {largest_number}. \n The First Number: {first_number} is Greater Than {second_number} and {third_number}."
        
    elif second_number >= first_number and second_number >= third_number:
        largest_number = second_number
        result = f"The Largest Number is the Second Number: {largest_number}. \n The Second Number: {second_number} is Greater Than {first_number} and {third_number}."

    else: 
        largest_number = third_number
        result = f"The Largest Number is the Third Number: {largest_number}. \n The Third Number: {third_number} is Greater Than {first_number} and {second_number}."
    
    messagebox.showinfo("The Largest Number", result)


window = tk.Tk()
window.title("Largest Number Finder Program🔍🕵🔎")
window.configure(bg="#000000")
window.geometry("510x340")

label = tk.Label(window, text = " Largest Number Finder", font=("Times", "28","bold italic"), bg="#000000", fg="#00FFFF").grid(row=0, column=0, pady = 20, sticky=tk.W)
label = tk.Label(window, text = "🔍🕵🔎", font=("Times", "28","bold italic"), bg="#000000", fg="#00FFFF").grid(row=0, column=1, pady = 20, sticky=tk.W)

tk.Label(window, text = "      Enter First Number:", font=("System", "20", "bold italic"), bg="#000000", fg="#00FFFF").grid(row=1, column=0, sticky=tk.W)
first_number_entry = tk.Entry(window, width=7, font=("System", "20", "bold italic"),bg="#00FFFF",fg="#000000")
first_number_entry.grid(row = 1, column = 1, pady = 5)

tk.Label(window, text = "      Enter Second Number:", font=("System", "20", "bold italic"), bg="#000000", fg="#00FFFF").grid(row=2, column=0, sticky=tk.W)
second_number_entry = tk.Entry(window, width=7, font=("System", "20", "bold italic"),bg="#00FFFF",fg="#000000")
second_number_entry.grid(row = 2, column = 1, pady = 5) 

tk.Label(window, text = "      Enter Third Number:", font=("System", "20", "bold italic"), bg="#000000", fg="#00FFFF").grid(row=3, column=0, sticky=tk.W)
third_number_entry = tk.Entry(window, width=7, font=("System", "20", "bold italic"),bg="#00FFFF",fg="#000000")
third_number_entry.grid(row = 3, column = 1, pady = 5)

finding_the_largest_number_button = tk.Button(window, text="Find the Largest Number👆", command=finding_the_largest_number, width=20, height=1, font=("Times", "18","bold italic"), bg="#00FFFF", fg="#000000", padx=15, pady=5)
finding_the_largest_number_button.grid(row=4, column=0, columnspan=2, pady=20)


window.mainloop()