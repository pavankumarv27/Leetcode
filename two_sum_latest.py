# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# [25, 1, 10, 4, 35, 6, 7, 16]
# target = 41

# scenarios
# 1. sum of two integers is equal to target (one time)
# 2. sum of two integers is equal to target (2 times)
# 3. sum of any 2 integers is not equal to target
# 4. empty list passed
# 5. single element list passed
# 6. list of only negative integers passed
# 7. list of combination of negative and positive integers passed
# 8. list with duplicates passed
# 9. 

def two_sum(array, target):
    for i in range(len(array)):
        possible_ele = target - array[i]
        if possible_ele in array[i+1:]:
            return [i, array[i+1:].index(possible_ele)+(i+1)]
    return -1
