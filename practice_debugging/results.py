name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 # should be 0 not 

flag = True
while flag == True: # needs to be true 
    name = input("Enter student's name:") # should be ""
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: # should be and 
            break 
        else:
            print('Invalid mark!')
    mark_list += [mark] # wrong indentation
    count += 1
    if mark >= 75: # should be >=
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name] # wrong bracat
    more = (input('Would you like to enter another score, Y or N?: ')) # input cannot be integer 
    if more == 'N':
        flag = False

average = round(sum(mark_list)/len(mark_list), 2) # should be sum 
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.")  # change to string 
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))