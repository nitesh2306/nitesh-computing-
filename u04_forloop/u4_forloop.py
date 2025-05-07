######
# for loop allows you to loop through things...
# things here mean range(), 'string', list, dictionary

# three ways of using range()
# range(stop) # stop value
# # range(5) ---->>>>>> # 0, 1, 2, 3, 4
# # for i in range(5):
# #     print(i)

# range(start, stop) # from the start, up to stop
# range(7,12)   # 7, 8, 9, 10, 11

# range(start, stop, step) # from start, to stop, in increment of step
# range(8, 25, 2) #8, 10, 12, 14, 16, 18, 20, 22, 24

# range(10, 0, -1) # 10, 9 , 8, 7, 6, 5, 4, 3, ,2 , 1 


# ###################################################
# # Part 1: Learning Exercises
# # Exercise 1: Simple Loop with range(stop)
# # Write a program to print "Welcome to Python!" 5 times.
# # Use range(stop) to repeat the message.
# for _ in range(5):  # Loop runs 5 times
#     print("Welcome to Python!")

# repeat things again and again
# for i in range(5)
# 



# #------------------------------------------------------------
# # Exercise 2: Printing Numbers with range(stop)
# # Write a program to print numbers from 0 to 4 using range(stop).
# # Example: Output = 0, 1, 2, 3, 4.
# for i in range(5):  # Loop from 0 to 4
#     print("Number: {}".format(i))
# for i in range (43,37,-1):
#     print(i)              

# #------------------------------------------------------------
# # Exercise 3: Counting with range(start, stop)
# # Write a program to print numbers from 10 to 15.
# # Use range(start, stop) to set the range.
# # Example: Output = 10, 11, 12, 13, 14, 15.
# for i in range(10, 16):  # Loop from 10 to 15
#     print("Counting: {}".format(i))


# #------------------------------------------------------------
# # Exercise 4: Using range(start, stop, step)
# # Write a program to print even numbers from 2 to 10.
# # Use range with a step value.
# # Example: Output = 2, 4, 6, 8, 10.
# for i in range(2, 11, 2):  # Step value is 2
#     print("Even number: {}".format(i))
# for i in range (4,49,4):
#     print(i)

# #------------------------------------------------------------
# # Exercise 5: Printing Numbers in Reverse
# # Write a program to print numbers from 10 to 1.
# # Use range(start, stop, step) with a negative step value.
# # Example: Output = 10, 9, 8, ..., 1.
# for i in range(10, 0, -1):  # Loop backwards
#     print("Countdown: {}".format(i))


# #------------------------------------------------------------
# # Exercise 6: Summing Numbers in a Range
# # Write a program to calculate the sum of numbers from 1 to 10.
# # Use range(start, stop) and a loop to add the numbers.
# # Example: Output = 55.
# total = 0
# for i in range(1, 11):  # Loop from 1 to 10
#     total += i
# print("The total sum is: {}".format(total))
# name= "NITESH"

# #------------------------------------------------------------
# # Exercise 7: Printing a Simple Pattern
# # Write a program to print the following pattern:
# # *
# # **
# # ***
# # ****
# # *****
# for i in range(1, 6):  # Loop for rows
#     print("*" * i)





###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Printing Odd Numbers
# Write a program to print all odd numbers from 1 to 15.
# Use range(start, stop, step) to skip even numbers.
# Example: Output = 1, 3, 5, ..., 15.
# for i in range(1,16,2):
#     print(i)


#------------------------------------------------------------
# Exercise 9: Multiplying Numbers
# Write a program to print the first 5 multiples of 7.
# Use range(start, stop, step).
# Example: Output = 7, 14, 21, 28, 35.
# for i in range(7,36,7):
#     print(i)

#------------------------------------------------------------
# Exercise 10: Repeating a Phrase
# Write a program to print "I love Python!" 3 times.
# Use range(stop) to repeat the phrase.
# for i in range(3):
#     print("i love phyton")


#------------------------------------------------------------
# Exercise 11: Custom Counting Pattern
# Write a program to print the following pattern:
# 1
# 22
# 333
# 4444
# 55555

# print("1" * 1)
# print("2" * 2)
# print("3" * 3)
# print("4" * 4)
# print("5" * 5)
# for i in range(1,6):
#      print(str(i) * i)


# 5
# 44
# 333
# 2222
# 11111
# multiply = 1
# for i in range(5,0,-1):
#     print(str(i) * multiply)
#     multiply = multiply + 1





#------------------------------------------------------------
# Exercise 12: Generating a Multiplication Table
# Write a program to print the multiplication table of 6.
# Example: 6 x 1 = 6, ..., 6 x 10 = 60.
# 6 x 1 = 6
# 6 x 2 = 12

# ask for a number 
# num = int(input("enter a number: "))
# for i in range(1,13):
#     print(f"{num} x {i} = {num * i }")



#------------------------------------------------------------
# Exercise 13: Printing a Custom Star Pattern
# Write a program to print the following pattern:
# *
# ***
# *****
# *******
# *********
# "*""
# for i in range(1,10,2):
#     print("*" * i)
# for i in range(15):
#     print(i)
# # print out the numbers 0 - 14







# loop through the word "INDONESIA"
# print all the letters in the word INDONESIA
word = "INDONESIA"
# for i in word:
#     print(i)


# print out numbers from 0-6
# for i in range(7):
#     print(i)

# print out numbers from 6 - 18
# for i in range(6,19):
#     print(i)

# # print out multiples of 8 from 8 to 96
# for i in range(8,97,8):
#     print(i)

# # print out  numbers from 15 to 4 decreasing by 1
# for i in range(15,3,-1):
#     print(i)