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

def is_subsequence(lst, sequence):
    seq_index = 0
    for i in range(len(lst)):
        if seq_index == len(sequence): #if the index is equal to the length of the sequence
            return True
        if lst[i] == sequence[seq_index]: #if the value at the index of the list is equal to the value at the index of the sequence
            seq_index += 1 #increment the index of the sequence
    return seq_index == len(sequence) #return the index of the sequence is equal to the length of the sequence

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))  