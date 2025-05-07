# num1 = 10
# num2 = 10

# print(num1 > num2) # more than
# print(num1 < num2) # less than
# print(num1 >= num2) # more than or equal to
# print(num1 <= num2) # less than or equal to
# print(num1 == num2) # equal to
# print(num1 != num2) # not equal to

# if num1 > num2:
#     print("num1 is bigger")
# else:
#     print("num1 is smaller")

# pw="nitesh"
# inputpw=input("enter the password ")
# if pw==inputpw:
#     print("access granted")
# else:
#     print("access denied")


# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # Exercise 8: Pass/Fail Checker
# # Write a program to check if a student's score is a pass or 
# # fail. Passing marks are 50 and above. Example: Input = 65.
# # Output: "Pass."
# marks=input("enter your marks ")
# if int(marks) > 49:
#     print("student has passed")
# else:
#     print("student has failed")


# Exercise 4: Multi-Way Selection with If-Elif-Else
# Write a program to check if a number is positive, zero, or 
# negative. Example: Input = 0. Output = "The number is zero."

# num = int(input("Enter a number: "))

# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")

# Exercise 11: Age-Based Group Assignment
# Write a program to categorize a person into groups based 
# on age: Child (0-12), Teen (13-19), Adult (20-64), Senior(>=65) 
# Example: Input = 15. Output = "Teen."
# numpple = int(input("How many persons? "))

# for i in range(numpple):

#     age=input("enter your age ")
#     if int(age) < 13:
#         print("child")
#     elif int(age)< 20:
#         print("teen")
#     elif int(age)< 65:
#         print("adult")
#     else:
#         print("senior citizen")

# getting remainder after a division >>>> modulus %
num=int(input("enter a number "))
if num % 2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")