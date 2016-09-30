
# coding: utf-8

# In[1]:

## list-1.1 first_last6
'''
Given an array of ints, return True if 6 appears as either the first or last element in the array. 
The array will be length 1 or more.
'''

def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

first_last6([13, 6, 1, 2, 3])


# In[2]:

## list-1.2 same_first_last
'''
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
'''

def same_first_last(nums):
    if len(nums) == 0: return  False
    return nums[0] == nums[-1]

same_first_last([1, 2, 3, 4, 5, 13])


# In[3]:

## list-1.3 make_pi
'''
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
'''

def make_pi():
    return [3,1,4]

make_pi()


# In[4]:

## list-1.4 common_end
'''
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
'''

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

common_end([1, 2, 3], [1, 3])


# In[5]:

## list-1.5 sum3
'''
Given an array of ints length 3, return the sum of all the elements.
'''

def sum3(nums):
    return sum(nums)

sum3([2, 7, 2])


# In[6]:

## list-1.6 rotate_left3
'''
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
'''

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

rotate_left3([1, 2, 1])


# In[7]:

## list-1.7 reverse3
'''
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
'''

def reverse3(nums):
    return nums[::-1]

reverse3([2, 11, 3])


# In[8]:

## list-1.8 max_end
'''
Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. 
Return the changed array.
'''

def max_end3(nums):
    larger = nums[0]
    if nums[0] < nums[2]: larger = nums[2]
    return [larger] * 3

max_end3([3, 11, 11])


# In[9]:

## list-1.9 sum2
'''
Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. 
Return the changed array.
'''

def sum2(nums):
    if len(nums) > 1: return nums[0] + nums[1]
    elif len(nums) == 1: return nums[0]
    else: return 0
    
sum2([1,2,3])


# In[10]:

## list-1.10 middle_way
'''
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
'''

def middle_way(a, b):
    return [a[1],b[1]]

middle_way([1, 2, 3], [4, 5, 6])


# In[11]:

## list-1.12 has23
'''
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
'''

def has23(nums):
    result = False
    for i in range(2):
        if nums[i] == 2 or nums[i] == 3: result = True
    return result

has23([3, 9])


# In[ ]:




# In[ ]:




# In[ ]:



