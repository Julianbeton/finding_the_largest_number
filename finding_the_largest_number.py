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

    first_number_difference_to_second_number = first_number - second_number
    first_number_difference_to_third_number = first_number - third_number

    second_number_difference_to_first_number = second_number - first_number
    second_number_difference_to_third_number = second_number - third_number

    third_number_difference_to_first_number = third_number - first_number
    third_number_difference_to_second_number = third_number - second_number

#find the largest number among the 3 numbers
    if first_number >= second_number and first_number >= third_number:
        largest_number = first_number
        result = f"\nThe Largest Number is the First Number:  {largest_number}.\n\n Solution:\nThe Difference of First Number to Second Number is:\n{first_number} - {second_number} = {first_number_difference_to_second_number}\nThe Difference of First Number to Third Number is:\n{first_number} - {third_number} = {first_number_difference_to_third_number}\nTherefore {first_number} is Greater Than {second_number} and {third_number}."
        

    elif second_number >= first_number and second_number >= third_number:
        largest_number = second_number
        result = f"\nThe Largest Number is the Second Number:  {largest_number}.\n\n Solution:\nThe Difference of Second Number to First Number is:\n{second_number} - {first_number} = {second_number_difference_to_first_number}\nThe Difference of Second Number to Third Number is:\n{second_number} - {third_number} = {second_number_difference_to_third_number}\nTherefore {second_number} is Greater Than {first_number} and {third_number}."

    else: 
        largest_number = third_number
        result = f"\nThe Largest Number is the Third Number:  {largest_number}.\n\n Solution:\nThe Difference of Third Number to First Number is:\n{third_number} - {first_number} = {third_number_difference_to_first_number}\nThe Difference of Third Number to Second Number is:\n{third_number} - {second_number} = {third_number_difference_to_second_number}\nTherefore {third_number} is Greater Than {first_number} and {second_number}."
    

    output_window = tk.Toplevel()
    output_window.title("The Largest Number")
    output_window.geometry("800x330")
    output_window.configure(bg="#000000")


    result_label = tk.Label(output_window, text=result, fg="#00FFFF", bg="#000000", font=("System", "20"))
    result_label.pack()


window = tk.Tk()
window.title("Largest Number Finder Program🔍🕵🔎")
window.configure(bg="#000000")
window.geometry("510x340")

label = tk.Label(window, text = " Largest Number Finder", font=("Times", "28"), bg="#000000", fg="#00FFFF").grid(row=0, column=0, pady = 20, sticky=tk.W)
label = tk.Label(window, text = "🔍🕵🔎", font=("Times", "28"), bg="#000000", fg="#00FFFF").grid(row=0, column=1, pady = 20, sticky=tk.W)

tk.Label(window, text = "      Enter First Number:", font=("System", "20"), bg="#000000", fg="#00FFFF").grid(row=1, column=0, sticky=tk.W)
first_number_entry = tk.Entry(window, width=7, font=("System", "20"),bg="#00FFFF",fg="#000000")
first_number_entry.grid(row = 1, column = 1, pady = 5)

tk.Label(window, text = "      Enter Second Number:", font=("System", "20"), bg="#000000", fg="#00FFFF").grid(row=2, column=0, sticky=tk.W)
second_number_entry = tk.Entry(window, width=7, font=("System", "20"),bg="#00FFFF",fg="#000000")
second_number_entry.grid(row = 2, column = 1, pady = 5) 

tk.Label(window, text = "      Enter Third Number:", font=("System", "20"), bg="#000000", fg="#00FFFF").grid(row=3, column=0, sticky=tk.W)
third_number_entry = tk.Entry(window, width=7, font=("System", "20"),bg="#00FFFF",fg="#000000")
third_number_entry.grid(row = 3, column = 1, pady = 5)

finding_the_largest_number_button = tk.Button(window, text="Find the Largest Number👆", command=finding_the_largest_number, width=20, height=1, font=("Times", "18","bold italic"), bg="#00FFFF", fg="#000000", padx=15, pady=5)
finding_the_largest_number_button.grid(row=4, column=0, columnspan=2, pady=20)


window.mainloop()