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


# def frequency_greater_than_n(nums, n):
#     frequency = {} #create an empty dictionary
#     for num in nums: #for each number in the list
#         if num in frequency: #if the number is in the dictionary
#             frequency[num] += 1 #increment the value by 1
#         else: #if the number is not in the dictionary
#             frequency[num] = 1  #add the number to the dictionary
#     return {key: value for key, value in frequency.items() if value > n}
# #return the dictionary with the key and value if the value is greater than n

# nums = [1, 2, 4, 3, 2, 4, 4, 3, 3, 3]
# n = 3
# print(frequency_greater_than_n(nums, n))  # Output: {3: 4, 4: 3}


#WEEK 4

# def move_zeros(nums):
#     left = 0 
#     for right in range (len(nums)):
#         if nums[right] != 0:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#     return nums

# nums = [0, 1, 0, 3, 12]
# print(move_zeros(nums))

# def find_middle(lst):
#     slow = 0
#     fast = 1 #starts at 1 not at 0 
#     while fast < len(lst) and fast + 1 < len(lst):
#         slow += 1
#         fast += 2
#     return lst[slow]
# lst = [1, 2, 3, 4, 5]
# print(find_middle(lst)) # Output: 3

# def reverse_string(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         temp = s[left]
#         s[left] = s[right]
#         left += 1
#         right -= 1
#     return temp
# s = list("hello")
# print(reverse_string(s)) # Output: "olleh"

# def find_pair_sum(s, target):
#  # two pointers solution
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         current_sum = s[left] + s[right]
#         if current_sum == target:
#            return True

#assigment week 7

# def find_val(names, val):
#    if val in names:
#       for i in range(len(names)):
#          if names[i] == val:
#              return i
#    else:
#       return -1

# names = ["ana", 'beric','juan']
# val = 'juan'
# print(find_val(names,val ))

# #given two integers x and n , n>= 0 write a function 
# #that recursively computes and returns x^n

# def power(x, n):
#    if n == 0:  # Base case: any number to the power of 0 is 1
#       return 1
#    else:  # Recursive case
#       return x * power(x, n - 1)

# x = 2
# n = 3
# print(power(x, n))  # Output: 8

# given a list of integers sorted in non-decreasing order starting and 
#ending position of a given target value. return the result as a list in the form
#of a [start position, end_position]
#if target is not found in the list return [-1,-1 ]
#solution must be 0log(n)

# def search_range(nums, target):
#    def find_bound(is_first, left, right):
#       if left > right:
#          return -1
#       mid = (left + right) // 2
#       if nums[mid] == target:
#          if is_first:
#             if mid == left or nums[mid - 1] != target:
#                return mid
#             return find_bound(is_first, left, mid - 1)
#          else:
#             if mid == right or nums[mid + 1] != target:
#                return mid
#             return find_bound(is_first, mid + 1, right)
#       elif nums[mid] < target:
#          return find_bound(is_first, mid + 1, right)
#       else:
#          return find_bound(is_first, left, mid - 1)

#    start = find_bound(True, 0, len(nums) - 1)
#    if start == -1:
#       return [-1, -1]
#    end = find_bound(False, 0, len(nums) - 1)
#    return [start, end]

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# print(search_range(nums, target))  # Output: [3, 4]

