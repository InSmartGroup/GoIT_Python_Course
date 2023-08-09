# Given a list of numbers, return a fixed list so that the values increment by 1 for each index
# from the minimum value up to the maximum value (both included)
# E.g.: Input: 1,3,5,6,7,8
# Output: 1,2,3,4,5,6,7,8

def pipe_fix(nums):
    num_min, num_max = min(nums), max(nums)
    nums_new = []

    for i in range(num_min, num_max + 1):
        nums_new.append(i)

    return nums_new


print(pipe_fix([1, 3, 5, 6, 7, 8]))
