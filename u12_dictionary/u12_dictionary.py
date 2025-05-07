###################################################
# Part 1: Learning Exercises

# Practice Exercise 1: Creating a Dictionary
# Create a dictionary to store student names and their grades.
students= {"Mark":60, "Alice":77, "Bob":95}

# #------------------------------------------------------------
# # Practice Exercise 2: Accessing Dictionary Values
# # Access Bob's grade from the dictionary.
students= {"Mark":60, "Alice":77, "Bob":95}
bobgrades= students["Bob"]
print(bobgrades)

#------------------------------------------------------------
# Practice Exercise 3: Adding New Key-Value Pairs
# Add a new student, Diana, with a grade of 92 to the dictionary.
students= {"Mark":60, "Alice":77, "Bob":95}
students["Diana"]=92
print(students)
students["Bob"]=80
print(students)

#------------------------------------------------------------
# Practice Exercise 4: Updating Existing Values
# Update Charlie's grade to 80 in the dictionary.


#------------------------------------------------------------
# Practice Exercise 5: Deleting Key-Value Pairs
# Remove Alice's entry from the dictionary.
students= {"Mark":60, "Alice":77, "Bob":95}
del(students["Alice"])
print(students)

#------------------------------------------------------------
# Practice Exercise 6: Checking for Existence of a Key
# Check if 'Diana' is in the student dictionary.
students= {"Mark":60, "Alice":77, "Bob":95}
name= input("enter students name")
if name in students:
    print(f"{name} is in this class")
else:
    print(f"{name} is not in this class")

#------------------------------------------------------------
# Practice Exercise 7: Iterating Through a Dictionary
# Print all student names and their grades.
students= {"Mark":60, "Alice":77, "Bob":95}
for name in students:

   print(f"{name} scored {students[name]}")



#-----------