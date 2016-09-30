
# coding: utf-8

# In[1]:

## list-2.1 count_evens
'''
Return the number of even ints in the given array.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
'''

def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0: count += 1
    return count

count_evens([2, 1, 2, 3, 4])


# In[2]:

## list-2.2 big_diff
'''
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
'''

def big_diff(nums):
    nums.sort()
    return abs(nums[-1] - nums[0])

big_diff([10, 3, 5, 6])


# In[3]:

## list-2.3 centered_average
'''
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
Use int division to produce the final average.
You may assume that the array is length 3 or more.
'''

def centered_average(nums):
    nums.sort()
    new_nums = nums[1:-1]
    return sum(new_nums)/(len(nums)-2)

centered_average([1, 2, 3, 4, 100])


# In[4]:

## list-2.4 sum13
'''
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
'''

def sum13(nums):
    while 13 in nums:
        if nums.index(13) < len(nums)-1:
            nums.pop(nums.index(13)+1)
        nums.pop(nums.index(13))
    return sum(nums)

sum13([1, 2, 2, 1, 13])


# In[5]:

## list-2.5 sum67
'''
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
'''

def sum67(nums):
    count = 0
    blocked = False
    
    for num in nums:
        if num == 6:
            blocked = True
            continue
    
        if num == 7 and blocked:
            blocked = False
            continue
        if not blocked:  
            count += num
    return count
  
sum67([1, 2, 2, 6, 99, 99, 7]) 


# In[6]:

## list-2.6 has22
'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
'''

def has22(nums):
    result = False
    for i in range(0,len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            result = True
    return result

has22([1, 2, 1, 2]) 


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



