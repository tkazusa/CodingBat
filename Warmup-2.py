
# coding: utf-8

# In[1]:

import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print ('elapsed time: %f ms' % self.msecs)


# In[2]:

## Wormup-2.1 string_times
'''
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
'''

def mystring_times(str, n):
    return str*n
  
def string_times(str, n):
    result = ""
    for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
        result = result + str  # could use += here
    return result

with Timer(verbose=True) as t:
    mystring_times('code', 2)
    
with Timer(verbose=True) as t:
     string_times('code', 2)


# In[3]:

## Wormup-2.2 front_times
'''
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
'''

def myfront_times(str, n):
    if len(str) < 3:
        return n*str
    else: return n*str[:3]

def front_times(str, n):
    front_len = 3
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]
    
    result = ""
    for i in range(n):
        result = result + front
    return result

with Timer(verbose=True) as t:
    myfront_times('Chocolate', 3)
    
with Timer(verbose=True) as t:
     front_times('Chocolate', 3)


# In[4]:

## Wormup-2.3 string_bits
'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
'''

def mystring_bits(str):
    new_str = ""
    for i in range(len(str)):
        if  i % 2 == 0:
            new_str += str[i]
        else:new_str= new_str 
    return new_str

def string_bits(str):
    result = ""
    # Many ways to do this. This uses the standard loop of i on every char,
    # and inside the loop skips the odd index values.
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


with Timer(verbose=True) as t:
    mystring_bits('Chocolate')
    
with Timer(verbose=True) as t:
     string_bits('Chocolate')


# In[5]:

## Wormup-2.4 string_splosion
'''
Given a non-empty string like "Code" return a string like "CCoCodCode".
'''

def string_splosion(str):
    new_str = ""
    for i in range(len(str)+1):
        new_str += str[:i]
    return new_str
  
def string_splosion(str):
    result = ""
    # On each iteration, add the substring of the chars 0..i
    for i in range(len(str)):
        result = result + str[:i+1]
    return result

with Timer(verbose=True) as t:
    string_splosion('Chocolate')
    
with Timer(verbose=True) as t:
     string_splosion('Chocolate')


# In[6]:

## Wormup-2.4 string_splosion
'''
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
'''

'''
def last2(str):
   no-idea
'''    

 
def last2(str):
    # Screen out too-short string case.
    if len(str) < 2:
        return 0
  
    # last 2 chars, can be written as str[-2:]
    last2 = str[len(str)-2:]
    count = 0
  
    #Check each substring length 2 starting at i
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == last2:
            count = count + 1
            
    return count

with Timer(verbose=True) as t:
     last2('xaxxaxaxx')


# In[7]:

## Wormup-2.5 array_count9
'''
Given an array of ints, return the number of 9's in the array.
'''

def myarray_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

 
def array_count9(nums):
    count = 0
    # Standard loop to look at each value
    for num in nums:
        if num == 9:
            count = count + 1

    return count

with Timer(verbose=True) as t:
     myarray_count9([1, 9, 9, 3, 9])

with Timer(verbose=True) as t:
    array_count9([1, 9, 9, 3, 9])


# In[8]:

## Wormup-2.6 array_count9
'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4.
'''

def myarray_front9(nums):
    result = False
    if len(nums) < 4:
        for i in range(len(nums)):
            if nums[i] == 9: result = True
    
    for j in range(4):
        if nums[j] == 9: result = True
    return result
      
    
def array_front9(nums):
    # First figure the end for the loop
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):  # loop over index [0, 1, 2, 3]
        if nums[i] == 9:return True
    
    return False
    
with Timer(verbose=True) as t:
    myarray_front9([1, 9, 9, 3, 9])

with Timer(verbose=True) as t:
    myarray_front9([1, 9, 9, 3, 9])


# In[9]:

## Wormup-2.7 array123
'''
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.
'''

def myarray_front9(nums):
    result = False
    if len(nums) < 4:
        for i in range(len(nums)):
            if nums[i] == 9: result = True
    
    for j in range(4):
        if nums[j] == 9: result = True
    return result
      
    
def array_front9(nums):
    # First figure the end for the loop
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):  # loop over index [0, 1, 2, 3]
        if nums[i] == 9:return True
    
    return False
    
with Timer(verbose=True) as t:
    myarray_front9([1, 9, 9, 3, 9])

with Timer(verbose=True) as t:
    myarray_front9([1, 9, 9, 3, 9])


# In[10]:

## Wormup-2.8 array123
'''
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.
'''

def myarray123(nums):
    count1 = False
    count2 = False
    count3 = False
    for i in range(len(nums)):
        if nums[i] == 1: count1 = True
        if nums[i] == 2: count2 = True
        if nums[i] == 3: count3 = True
  
    if count1 == True and count2 == True and count3 == True:
        return True
    return False
      
    
def array123(nums):
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

    
with Timer(verbose=True) as t:
    myarray123([1, 1, 2, 1, 2, 3])

with Timer(verbose=True) as t:
    array123([1, 1, 2, 1, 2, 3])


# In[11]:

## Wormup-2.9 string_match
'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
'''

def mystring_match(a, b):
    count = 0
    shorter = min(len(a), len(b))
    for i in range(0,shorter-1):
        if a[i:i+2] ==b[i:i+2]: count +=1
    return count
  
def string_match(a, b):
    # Figure which string is shorter.
    shorter = min(len(a), len(b))
    count = 0
  
    # Loop i over every substring starting spot.
    # Use length-1 here, so can use char str[i+1] in the loop
    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count = count + 1
    return count

    
with Timer(verbose=True) as t:
    mystring_match('iaxxai', 'aaxxaaxx')

with Timer(verbose=True) as t:
    string_match('iaxxai', 'aaxxaaxx')


# In[ ]:




# In[ ]:




# In[ ]:



