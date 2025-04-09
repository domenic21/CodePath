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



# class Node:
#     def __init__(self, value, next=None):
#         # Initialize a node with a value and a pointer to the next node
#         self.value = value
#         self.next = next

# def is_palindrome(head):
#     # Step 1: Use slow and fast pointers to find the middle of the linked list
#     slow, fast = head, head  # Both start at the head of the list
#     while fast and fast.next:  # Move until fast reaches the end of the list
#         slow = slow.next  # Slow moves one step
#         fast = fast.next.next  # Fast moves two steps

#     # At this point, slow is at the middle of the list because fast has reached the end
#     # If the list has an odd number of elements, slow will be at the middle element
#     # If the list has an even number of elements, slow will be at the first element of the second half
    

#     # Step 2: Reverse the second half of the list starting from the slow pointer
#     prev = None  # Initialize a variable to store the previous node
#     while slow:  # Traverse the second half of the list
#         temp = slow.next  # Temporarily store the next node
#         slow.next = prev  # Reverse the current node's pointer
#         prev = slow  # Move prev to the current node
#         slow = temp  # Move slow to the next node

#     # Now, prev points to the head of the reversed second half

#     # Step 3: Compare the values of the first half and the reversed second half
#     left, right = head, prev  # Initialize pointers for comparison
#     while right:  # Only need to traverse the reversed half
#         if left.value != right.value:  # If values don't match, it's not a palindrome
#             return False
#         left = left.next  # Move left pointer forward
#         right = right.next  # Move right pointer forward

#     return True  # If all values match, it's a palindrome
# head = Node(1, Node(2, Node(1 )))
# print(is_palindrome(head))  # Output: True




# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(head):
	
#         if not head:
#             return False
        
#         slow = head  # Starts at the head
#         fast = head  # Also starts at the head

#         while fast and fast.next:
#             slow = slow.next          # Move slow pointer by one
#             fast = fast.next.next     # Move fast pointer by two

#             if slow == fast:          # If they meet, there's a cycle
#                break
        
#         if not fast or not fast.next: # If fast reaches the end, no cycle
#             return None

#         # Reset slow to head to find the start of the cycle
#         slow = head
#         while slow != fast:
#             slow = slow.next
#             fast = fast.next

#         # Find the tail of the cycle
#         tail = slow
#         while tail.next != slow:
#             tail = tail.next

#         return tail.value  # Return the value of the tail node


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)


# # Creates a cycle starting from node1 to node3
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2  # Creates a cycle by linking node4 to node2


# print(is_circular(node1)) 

# class Node:
#     def __init__(self, value, next_node = None, prev_node = None):
#         self.value = value
#         self.next_node = next_node
#         self.prev_node = prev_node

# def mystery_function(head):
#     if head is head:
#         return None
#     output_node = head.next_node
#     if output_node is not None:
#         output_node.prev_node = None
#     head.next_node = None
#     return output_node
    
# head = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# head.next_node = node2
# node2.prev_node = head
# node2.next_node = node3
# node3.prev_node = node2
# head = mystery_function(head)




# # Define a Node class to represent elements in a linked list
# class Node:
#     def __init__(self, value, next_node=None):
#         # Initialize the value of the node
#         self.value = value
#         # Initialize the reference to the next node in the list
#         self.next_node = next_node

# # Function to process a linked list and return specific values
# def mystery_function(head):
#     # Start at the head of the linked list
#     current = head
#     # Initialize an empty list to store the output
#     output = []
    
#     # Traverse the linked list
#     while current:
#         # If the value of the current node is even, add it to the output list
#         if current.value % 2 == 0:
#             output.append(current.value)
#         # Move to the next node in the linked list
#         current = current.next_node
    
#     # Return the list of even values
#     return output

# # Create a linked list: 1 -> 2 -> 3 -> 4
# head = Node(1, Node(2, Node(3, Node(4))))

# # Call the mystery_function and store the result
# output = mystery_function(head)

# # Print the resulting list of even values
# print(output)  # Output: [2, 4]


# ####################
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def shuffle_linked_list(head):
#     if not head or not head.next:  # If the list has 0 or 1 node, no changes are needed
#         return head

#     # Initialize pointers
#     current = head

#     # Traverse the list and swap adjacent nodes
#     while current and current.next:
#         # Swap the values of the current node and the next node
#         current.value, current.next.value = current.next.value, current.value
#         # Move to the next pair of nodes
#         current = current.next.next

#     return head

# # Helper function to print the linked list
# def print_linked_list(head):
#     current = head
#     result = []
#     while current:
#         result.append(current.value)
#         current = current.next
#     print(" -> ".join(map(str, result)))

# # Example usage
# head = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # Linked list: 1 -> 2 -> 3 -> 4 -> 5
# print("Original list:")
# print_linked_list(head)

# shuffled_head = shuffle_linked_list(head)
# print("Shuffled list:")
# print_linked_list(shuffled_head)  # Output: 2 -> 1 -> 4 -> 3 -> 5

######

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

#         if not headA or not headB:
#             return None
#         pA, pB = headA, headB
#         while pA != pB:
#             pA= headB if pA is None else pA.next
#             pB = headA if pB is None else pB.next
#         return pA

#unit 7 : recussion
# def repeat_hello(n):
# 	if n > 0:
# 		print("Hello")
# 		repeat_hello(n - 1)
		
# repeat_hello(5)

# def repeat_hello_iterative():
#     for i in range(5):
#         print("Hello")
# repeat_hello_iterative()

# # factorial cases 
# def factorial(n):
#     if n == 0:
#         return 1 
#     else:
#         return n * factorial(n-1 )
# print(factorial(5))

# recusrive sum

# def sum_list(lst):
#     if not lst:
#         return 0
#     return lst[0] + sum_list(lst[1:])
# lst = [1, 2, 3, 4, 5]
# print(sum_list(lst))

# def binary_search(lst, target):
# 	# Initialize a left pointer to the 0th index in the list
# 	# Initialize a right pointer to the last index in the list
        
# 	    left = 0 
#         rigth = 0
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1
# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0] + sum_list(lst[1:])
# lst =[1, 2, 3, 4, 5]
# print(sum_list(lst))

# Problem 4

#understand: 
# function return true if the input is a power of 2 and false otherwise 

#plan

# def is_power_of_two(n):
#     #Base case

#     if n % 2  != 0:
#         return False
#     if n == 2:
#         return True
#     else: #work#break#engine
# Binary search I
# def binary_search(lst, target):
#     left=0
#     right = len(lst)
#     while left<=right:
#         middle = (right + left) // 2
       
#         if lst[middle] == target:
#             return middle
#         elif lst[middle] < target:
#             left = middle + 1
#         else:
#             right = middle - 1
#     return -1

# lst = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 11
# print(binary_search(lst, target))


#week 8

#problem 2 Node Sum 

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def check_tree(root):
#     return root.val == (root.left.val + root.right.val) if root else True

# ex = TreeNode(10, TreeNode(4), TreeNode(6))
# print(check_tree(ex))  # Output: True
#TIME COMPLEXITY O(1)  SPACE COMPLEXITY O(1)

#Porblem 3: Node sum II
#Given the root of a binary tree that has at most 3 nodes: the root, 
# #its left child, and its right child, return True if the value of the root is equal to the sum of the values 
# #of its two children. Return False otherwise.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if not root or (not root.left and not root.rigth):
        return False
    # Check if both left and right children are present
    if not root.left:
        return root.rigth.val == root.val
    if not root.right:
        return root.left.val == root.val
    return root.val ==(root.left.val + root.right.val)

    
ex = TreeNode(10, TreeNode(4))
print(check_tree(ex))  