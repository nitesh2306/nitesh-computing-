# Part 1: Learning Exercises

# Exercise 1: Importing Modules
# Write a program to use the math module for calculations.
# Example: Calculate the square root of 16 and the power of 2^3.

import math  # Importing the math module
# sqrt_value = math.sqrt(16)
# power_value = math.pow(2, 3)
# print("Square root of 16 is:", sqrt_value)
# print("2 to the power of 3 is:", power_value)


#------------------------------------------------------------
# Exercise 2: Modulus and Floor Division
# Write a program to calculate the modulus and floor division
# of two numbers. Example: 17 divided by 5.
# num1 = 17
# num2 = 5
# modulus = num1 % num2  # modulus is the remainder after a division
# floor_div = num1 // num2 # return 3 if 17 dividide by 5
# print("17 % 5 is:", modulus)
# print("17 // 5 is:", floor_div)

# # asked to calculate how many hours and minutes is 195 minutes

# total = 195
# hours = total // 60 # return you the hour portion
# minutes = total % 60
# print(f"{total} minutes is equal to {hours} hour and {minutes} minute")

#------------------------------------------------------------
# Exercise 3: Using Rounding Methods
# Write a program to round a number using round(), math.ceil(),
# and math.floor(). Example: number = 5.67.
# number = 5.6782372380209238
# rounded = round(number,5)
# ceiled = math.ceil(number)
# floored = math.floor(number)
# print("Rounded:", rounded, "Ceiled:", ceiled, "Floored:", floored)


# #------------------------------------------------------------
# # Exercise 4: Floor Division for Time Conversion
# # Write a program to convert total seconds into minutes and 
# # seconds using floor division and modulus. Example: 125 seconds
# # = 2 minutes and 5 seconds.
# total_seconds = 125
# minutes = total_seconds // 60
# seconds = total_seconds % 60
# print("Minutes:", minutes, "Seconds:", seconds)


# #------------------------------------------------------------
# # Exercise 5: Rounding for Pricing
# # Write a program to calculate the total price of an item after 
# # rounding up to the nearest dollar. Example: If the price is 
# # 19.75, the total is 20.
# price = 19.75
# rounded_price = math.ceil(price)
# print("Rounded total price is:", rounded_price)



# #------------------------------------------------------------
# # Exercise 6: Generating Random Integers
# # Write a program to generate a random number between 1 and 10.
# # Example: The output could be any number from 1 to 10.
# import random
# random_number = random.randint(1, 10)
# print("Random number between 1 and 10:", random_number)



# Exercise 7: Simulating Two Dice Rolls
# Write a program to simulate the roll of a 6-sided die two times
# and display the results. Example: Output = 4, 6.
# import random 

# d1 = random.randint(1,6)
# d2 = random.randint(1,6)
# print(f"Dice 1 : {d1}")
# print(f"Dice 2 : {d2}")


#------------------------------------------------------------
# Exercise 8: Floor Division for Groups
# Write a program to calculate how many full groups can be formed 
# and how many items are leftover. Example: 25 students divided 
# into groups of 4 = 6 groups and 1 leftover.

# numstudents = 15
# groupsize = 4

# numgroups = numstudents // groupsize
# leftover = numstudents % groupsize

# print(f"{numstudents} students divided into groups of {groupsize}")
# print(f"number of groups formed = {numgroups}")
# print(f"number students without a group = {leftover}")




##### Exercise 1
# Write a program to convert total minutes into hours and minutes.
# Your program must ask the user to input the number of minutes

# Example:
# Input = 185 minutes
# Output = 3 hours and 5 minutes.

# totalminutes= int(input("the number of minutes: "))
# hours= totalminutes // 60
# minutes= totalminutes % 60 
# print(f"{totalminutes} is {hours} hour and {minutes} minutes")


# Exercise 2
# Write a program to calculate how many notes of a specific
# denomination are needed to give change and how much remains.
 
# # Example:
# Amount = $275
# Denomination = $50 
# Notes = 5
# Remaining = $25
totalamount= int(input("enter the cost "))
denomination = 50
nubofnotes= totalamount // denomination
remainder= totalamount % denomination
print(f"{totalamount} , denomination: {denomination}, Number of notes: {nubofnotes}, Remainder: {remainder}")