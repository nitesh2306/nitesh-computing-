# create a list of 20 random numbers from 1 - 20
# import random
# numlist=[]
# for i in range(20):
#     num=random.randint(1,20)
#     numlist.append(num)
# print(numlist)
# for i in numlist:
#     print(i)
    
# string, integer, float, bool, list
# how to define a list
fruits = ["banana","orange","watermelon","durian","apple"]

# print out durian
print(fruits[3])
# change watermelon to starfruit
# fruits[2]="STARFRUIT"
# print(fruits)
# fruits.append("kiwi")
# print(fruits)

# # insert at index 0
# fruits.insert(0,"watermelon")
# print(fruits)

# # remove() ->>> remove orange
# fruits.remove("orange")
# print(fruits)

# # delete by the index delete the index 2
# del(fruits[2])
# print(fruits)

# # pop() removes the last item and assigns to a variable
# k= fruits.pop()
# print(fruits)
# print(f"i removed {k}")

# #### 
# # ask the user to enter a color and store it into a list
# # you need 5 colors in this list.

# # ask for colors input()
# colist = []
# # repeat 5 times with for loop
# for  i in range(5):
#     colour=input("enter a colour ")
#     colist.append(colour)
# print(colist)
# # add the color to li


# # Task 4: List Reverser

# # Ask the user to enter a list of 5 numbers (one by one)
# # Stores them in a list
# # Reverses the list manually (without using reverse() or slice)
# # Prints the reversed list

# numbers = []
# for i in range(5):
#     num=int(input(f"enter number {i+1}: "))
#     numbers.append(num)

# reversed_list = []
# for i in range(len(numbers) -1,-1,-1):
#     reversed_list.append(numbers[i])
# print("reversed_list", reversed_list )

# this is the slicing method way
# numbers = [4,6,8,9,10]
# reverse= numbers[::-1]
# print(reverse)

# ### this is the insert at the start way
# reverse_list=[]
# for num in numbers:
#     reverse_list.insert(0,num)

# print(reverse_list)
