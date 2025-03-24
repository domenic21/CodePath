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

# def first_unique_char(my_str):
#     my_char = {}
#     for i in my_str:
#         if i in my_char:
#             my_char[i] += 1 
#         else:
#             my_char[i] = 1
#     for i , value in my_char.items():
#         if value == 1:
#             return i 
#     return -1
# my_str = "l"
# print(first_unique_char(my_str))

# s = "Python"
# reversed_s = s[::-1]
# result = reversed_s + "rocks"
# print(result)

#date dd/mm/yyyy check if month is valid between 1-12
# date = "12/13/2023"
# # month = date[3:5]
# # is_valid = int(month) >= 1 and int(month) <= 12
# # print(is_valid)
# is_valid= 1<= int(date[3:5]) <= 12
# print(is_valid)

#Func that takes a string an returns a dict with each character
#as keys and frequency as values
# def char_count(string):
#     frequency = {}
#     for char in string:
#         char = char.lower()
#         # Ignore spaces
#         if char == ' ':
#             continue
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     return frequency
        

# string = 'Hello World'
# result = char_count(string)
# print(result)

#Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING message
#  2. STRING magazine

# def ransrom_note (message, magazine):
#     mag_count = {} # create an empty dictionary
#     for char in magazine: # for each character in the magazine
#         if char in mag_count: # if the character is in the dictionary mag_count
#             # increment the value by 1
#             mag_count[char] += 1
#         else: # if the character is not in the dictionary mag_count = 1 because 
#             mag_count[char] = 1 # add the character to the dictionary with a value of 1
#     # for each character in the message 
#     # check if the character is in the dictionary mag_count
#     # if the character is in the dictionary mag_count
#     # decrement the value by 1
#     # if the character is not in the dictionary mag_count return false
#     # if the value is less than 0 return false
#     # if the character is not in the dictionary mag_count return false

#     for char in message:
#         if char in mag_count and mag_count[char] > 0:
#             mag_count[char] -= 1
#         else:
#             return False
#     return True
    
# message = "bca"
# magazine = "abc"
# print(ransrom_note(message, magazine)) # Output: False

#Week 4 Pointers 


# class Dog:
#     def __init__(self, name, breed, owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner

#     def bark(self):
#         print('Woof!')
        
# dog1 = Dog('Buddy', 'Golden Retriever', 'Alice')
# dog2 = Dog('Max', 'Bulldog', 'Bob')

# dog1.bark()  # Output: Woof!
# dog2.bark()  # Output: Woof!




# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def get_last(head):
#     if not head:
#         return None
#     current = head
#     while current.next:
#         current = current.next
#     return current.value

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node1.next = node2
# node2.next = node3

# print(get_last(node1))  # Output: 3



# class Person:
#   def __init__(self, first, last):
#     self.last_name = last
#     self.first_name = first
#     self.children = []

#   def add_child(self, child):
#     self.children.append(child)
    
#   # Write your code here
#   def get_grandchildren(self):
#     grandchildren = []
#     for child in self.children:
#       grandchildren.extend(child.children)
#     return grandchildren









