# name = input("What is your name? ")
# msg = input("What would you like to say? ")

# print(name + " says " + msg )

############################################################
# Part 1: Learning Exercises 
# input() and and .format()

# Exercise 1: Using input() for Text
# Write a program to ask the user for their favorite color and display it.
# Example: If the user enters "blue", the program should display
# "Your favorite color is blue."
# color = input("What is your favorite color? ")
# print("Your favorite color is " + color + ".")




#------------------------------------------------------------
# Exercise 2: Understanding input() Behavior
# Write a program to ask the user for their age and display it.
# Example: If the user enters "15", display "Your age is 15."
# Note: Treat the input as a string for now.
# age = input("Enter your age: ")
# print("Your age is " + age + ".")


#------------------------------------------------------------
# Exercise 3: Comparing String Formatting Methods
# Write a program to ask the user for their name and age and display it
# in three different ways. Example: Input name = "John", age = 15
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# # Using + concatenation
# print(name + " is " + age + " years old.")


# # Using .format()
# print("{} is {} years old.".format(name, age))

# # Using f-strings
# print(f"{name} is {age} years old.")


#### VARIABLE TYPE ######
name = "Nitesh"
age = 15

# string variable string concatenation (join)
var1 = "BOB" # whenever you see a quotation mark, this is a string variable/ value
var2 = "DYLAN"
var3 = var1 + var2 # + on 2 strings, will join them together
# print(var3)

# integer variable
var4 = 100 # integer variable
var5 = 300
var6 = var4 + var5 # + on 2 numbers will add them together
# print(var6)

# type conversion
# change it from a string to an integer --->>> use int()

# 1. asking user to input the first number
# num1=int(input("what is the first number ?"))

# # 2. asking user to input the second number
# num2=int(input("what is the second number ?"))

# # 3. calculating the addition of num1 and num2
# answer= num1 + num2

# # 4. print out the answer
# print(f" {num1} + {num2} = {answer}")



'''
Challenge 1: Arithmetic with Variables
Write a program to calculate the perimeter of a rectangle.
Example: Assign 12 to length and 8 to width.
 
Calculate the perimeter using the formula: 2 * (length + width).
'''
# type your code here
# length= 12
# width= 8 
# primeter = 2*(length + width)

# print("the perimeter is " + str(primeter))
#print(f"the perimeter is {primeter}") # automatically convert for you

# integer
# string

# the perimeter is 40

''''
Challenge 2: String Combination
Use variables to create a descriptive sentence.
 
Example: Assign "Alice" to name and "reading" to hobby.
Combine them to display: "Alice loves reading in her free time."
# You must have 2 variables to complete this exercise
'''

'''
Challenge 3: Creative Repetition
Combine repetition and a meaningful statement.
Example: Print "Let's go! " three times, followed by "We can do it!"
 
Example Output: Let's go! Let's go! Let's go! We can do it!
 
You have to use the string * x method to duplicate the words to complete this exercise.
'''



# Exercise 6: Greeting with .format()
# Write a program to ask the user for their name and print a greeting
# using .format(). Example:
# Input: name = "Alice"
# Output: "Hello, Alice! Have a great day!"
# name= input("enter your name ")
# print(f"hello {name}! have a great day!")


#------------------------------------------------------------
# Exercise 8: Area of a Circle with .format()
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using .format(). Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."
# radius= float(input("enter the radius: "))
# area= 3.14 * radius**2 #math.pow(radius,2)
# print(f"the area of the circle is {area}")



# Exercise 12: Temperature Conversion with .format()
# Write a program to ask the user for a temperature in Celsius, convert it
# to Fahrenheit, and display the result using .format().
 # Use the formula: Fahrenheit = (Celsius * 9/5) + 32.
 
# Example:
# Input: Celsius = 25
# Output: "25C is equal to 77F."
celsius= int(input("enter the celsius "))
frh= (celsius * 9/5) + 32
print(f"{celsius} is equal to {frh}")