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
def max_difference(lst):
    
    min_value = min(lst)
    max_value = max(lst)
    max_diff = max_value - min_value
    return max_diff
    
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
