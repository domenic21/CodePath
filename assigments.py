# def lst_test (lst):
#    for i in lst:
#       print(lst)
# my_list = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(my_list['a'])
   
# my_list = {'a','b','c','d'}
# print(my_list[1:3])

# def lst_test (lst):
#    output = [] #create an empty list
#    for i in lst: #for each item in the list
#         output.append(i) #append each item to the output list
#    print(output) #print the output list
# my_dict={'a':[1,2], 'b':[3,4], 'c':[5,6]} #create a dictionary

# # Call the function with a list
# lst_test(my_dict)

# def get_top_player(dict):
#     highest_score = 0
#     top_player = ''
#     for name, score in dict.items():
#         if score > highest_score:
#             highest_score = score
#             top_player = name
#     print(top_player)
# dict = {"Audrey": 90, "Char":60, "Mario": 95}
# get_top_player(dict)

# def contains_duplicate(nums):
#     # Write your code here
#     counter = {}
#     for value in nums:
#         if value in counter:
#             return True
#         counter[value] = 1
#         return False
          

# nums = [1, 2, 4, 3]
# print(contains_duplicate(nums))  # Output: True


def frequency_greater_than_n(nums, n):
    frequency = {} #create an empty dictionary
    for num in nums: #for each number in the list
        if num in frequency: #if the number is in the dictionary
            frequency[num] += 1 #increment the value by 1
        else: #if the number is not in the dictionary
            frequency[num] = 1  #add the number to the dictionary
    return {key: value for key, value in frequency.items() if value > n}
#return the dictionary with the key and value if the value is greater than n

nums = [1, 2, 4, 3, 2, 4, 4, 3, 3, 3]
n = 3
print(frequency_greater_than_n(nums, n))  # Output: {3: 4, 4: 3}
