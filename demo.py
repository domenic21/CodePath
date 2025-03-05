#demo 
#Problem #1 


#Define the function 
#the function takes a list of items 
#create and empty list = result 
# for each item in the list we multiply by 2 
#append each item to the result list 
# return the list result 
#print function 

# def flip_sign(lst):
#     result=[]
#     for i in lst:
#        n = i * -1
#        result.append(n)
#     return result

# lst = [1,-2,-3,4]
# flipped_lst = flip_sign(lst)
# print(flipped_lst)


# Problem 5 Max difference 
#max_difference function
#takes a list of integers 
#returns the difference between the smallest and largest value in the list
#find min and max the subtract 

# def max_difference(lst):

    # min_value = min(lst)
    # max_value = max(lst)
    # max_diff = max_value - min_value
    # return max_diff

# lst = [5,22,8,10,2]
# max_diff = max_difference(lst)
# print(max_diff)


#Unit 2 
#lst and sequence  
# return true / false 
# subsequence: set of numbers not adjencent but in the same order 
# def is_subsequence(lst, sequence):
#     seq_index = 0
#     for num in lst:
#         if seq_index == len(sequence):
#             break
#         if sequence[seq_index] == num:
#             seq_index += 1
#     return seq_index == len(sequence)

# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence)) 

# def is_subsequence(lst, sequence):
#     seq_index = 0
#     for i in range(len(lst)):
#         if seq_index == len(sequence): #if the index is equal to the length of the sequence
#             return True
#         if lst[i] == sequence[seq_index]: #if the value at the index of the list is equal to the value at the index of the sequence
#             seq_index += 1 #increment the index of the sequence
#     return seq_index == len(sequence) #return the index of the sequence is equal to the length of the sequence

# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))  

# Problem 2: Create a Dictionary
# create a dictionary from a list of keys and a list of values
# create a for loop  for i in range i = 0 and the len of keys for each value, for each key we would assing value
#
# def create_dictionary(keys, values):
#      dictionary ={}
#      for i in range(0, len(keys)):
#         dictionary[keys[i] ]= values[i]
#         print(dictionary)
# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# create_dictionary(keys, values)
     
     #Session 2 Unit 2
     #Define function cast_vote, the function accepts a dictionary 
     #maps throught the candidates and assignes number of votes and a string + candidate
     #If candidate doesnt exist add them to the dictionary 
     # Find candidate 
     #increase number +1 of votes 
     #if not candidate not in the dictionary, create an entry and update dictionary
     
# def cast_vote(votes, candidate):
    
#     if candidate in votes:
#         votes[candidate] += 1 # it would add 1 if candidate exists
#     else:
#         votes[candidate] = 1  #it would add a new candidate with 1 vote
    
# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)

#Problem 2: Keys in Common 
#Function takes 2 dictionaries and compares each other
#Returns common keys 

# def common_keys(dict1, dict2):
#     lst = []
#     for name in dict1.keys():
#         for name2 in dict2.keys():
#             if name == name2:
#                 lst.append(name)
#     return lst
        
    
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)

#Problem 3: Highest Priority Task
#Given a dictionary check which task has the highest priority and return
# if priority has the same number 1-10  return the first in the alphabet

# def get_highest_priority_task(tasks):
#     highest_priority = -1
#     highest_priority_task = ""
#     for task, priority in tasks.items():
#         if priority > highest_priority or (priority == highest_priority and task < highest_priority_task):
#             highest_priority = priority
#             highest_priority_task = task
#     return highest_priority_task

# tasks = {"task1": 8, "task2": 1, "task3": 9, "task4": 10, "task5": 7}
# perform_task = get_highest_priority_task(tasks)
# print(perform_task)

# def count_mississippi(limit):
#     for num in range(1, limit):
# 	    print( f"{num} mississippi")
     
# count_mississippi(6)

#Problem 5: First Unique
#Find the non-repeating char in the string
# if it doesnt exist return -1

def first_unique_char(my_str):
    my_char = {}
    for i in my_str:
        if i in my_char:
            my_char[i] += 1 
        else:
            my_char[i] = 1
    for i , value in my_char.items():
        if value == 1:
            return i 
    return -1
my_str = "l"
print(first_unique_char(my_str))
