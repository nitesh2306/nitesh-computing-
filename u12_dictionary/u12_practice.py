# # create dictionary containing your menu items, and the price
# menu= {"Pasta":15.5, "Burger":5.5, "Pizza":20, "Fries":3.5, "Nuggets":4}

# # print out to the customer the things you sell 
# for items in menu:
#     print(items)


# # Ask customer what do they want to buy
# order= input("what do you want to buy? ")

# # Check if order is in dictionary
# if order in menu:
#     # If exist, then say the price
#     print(f"{order} is available")
#     print(f"{order} cost ${menu[order]}")
# else:
#     print(f"i do not sell {order}")






# imagine you own a sports shop

# # create a dictionary containing the items you sell and the price
# products={"racket":100, "shuttle":30,"shoes":99}
# # show the customers the items that you sell - for loop
# for items in products:
#     print(items)

# # ask customer what do they want to buy
# purchase=input("what would you like to purchase? ")
# # check if you sell the item
# if purchase in products:
#     print(f"{purchase} is available")
#     print(f"{purchase} cose ${products[purchase]}")
# else:
#     print(f"i do not sell {purchase}")
# # say the price if you sell the item



# Task 3.1
# Edit the program so that it:
# • converts the input for country to lower case
# • searches the dictionary for the country input and outputs the capital city of that country.
# Save your program.    [3]

# Task 3.2
# Copy and paste your program from sub-task 3.1.
# Edit the program so that if the user enters the value ‘Y’ 
# for remove, the program:
# • allows the user to input a country they want to remove from the dictionary
# • converts the country input to lower case
# • removes the country from the dictionary that is input by the user.
# Save your program.   [3]

capital_cities = {
    'singapore':'Singapore',
    'japan':'Tokyo', 
    'australia':'Canberra',
    'england':'London',
    'france':'Paris',
    'germany':'Berlin'
}

country = input("Please enter the name of a country: ")
# add = input("Would you like to add a new entry? (Y or N): ")
if country  in capital_cities:
    print(f"the capital of {country} is {capital_cities[country]}")


remove = input("Would you like to remove any of the entries? (Y or N): ")

if remove == "Y":
    country = input("Please enter the name of a country: ").lower()
    del(capital_cities[country])

print(capital_cities)

### continue to remove
# if country in capital_cities:
#     print(f"the capital of {country} is {capital_cities[country]}")









# else say don't exist







# In-Class Exercise 1: Student Grades Analysis
# Scenario: A teacher needs to analyze student performance.
# Create a dictionary with student names as keys and grades as values.
students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}

# Task 1: Identify and print the name of the highest scoring student.



#------------------------------------------------------------
# Task 2: Calculate and display the number of students scoring above 80.



#------------------------------------------------------------
# Task 3: Update all grades by adding 5 points as a bonus.




#------------------------------------------------------------
# In-Class Exercise 2: Inventory Stock Management
# Scenario: A warehouse manager needs to manage product stock levels.
inventory = {"Apples": 50, "Bananas": 30, "Oranges": 20, "Grapes": 60}

# Task 1: Add a new product "Pineapples" with an initial stock of 40.




#------------------------------------------------------------
# Task 2: Find and print the total stock of all items combined.




#------------------------------------------------------------
# Task 3: Identify and remove any product with stock below 25.



#------------------------------------------------------------
# In-Class Exercise 3: Library Book Management
# Scenario: A librarian tracks the availability of books in a dictionary.
books = {
    "1984": {"status": "Available", "copies": 5},
    "Brave New World": {"status": "Checked Out", "copies": 0},
    "Fahrenheit 451": {"status": "Available", "copies": 2},
}

#------------------------------------------------------------
# Task 1: Add a new book "To Kill a Mockingbird" with 3 copies.



#------------------------------------------------------------
# Task 2: Update the status of "1984" to "Checked Out" if all copies are borrowed.




#------------------------------------------------------------
# Task 3: Print all books currently available along with their copy count.






#------------------------------------------------------------
# In-Class Exercise 4: Customer Orders Tracking
# Scenario: A store tracks orders with customers and the items they purchased.
orders = {
    "John": ["Apples", "Bananas"],
    "Mary": ["Oranges", "Grapes"],
    "Alice": ["Bananas", "Pineapples"],
}

# Task 1: Add a new order for "Mark" who purchased "Apples" and "Oranges".





#------------------------------------------------------------
# Task 2: Count and print the total number of unique items purchased by all customers.



#------------------------------------------------------------
# Task 3: Identify customers who purchased "Bananas".



#------------------------------------------------------------
