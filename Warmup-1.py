
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

## Wormup-1.1 sleep_in
'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
'''


def mysleep_in(weekday, vacation):
  if vacation != True or weekday != True:
    return True
  else: return False
    
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

with Timer(verbose=True) as t:
    mysleep_in(True,False)
    
with Timer(verbose=True) as t:
     sleep_in(True,False)


# In[3]:

## Wormup-1.2 monkey_trouble
'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
We are in trouble if they are both smiling or if neither of them is smiling.
Return True if we are in trouble.
'''

def mymonkey_trouble(a_smile, b_smile):
    if a_smile == b_smile: return True
    else: return False

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

with Timer(verbose=True) as t:
    mymonkey_trouble(True,False)
    
with Timer(verbose=True) as t:
    monkey_trouble(True,False)


# In[4]:

## Wormup-1.3 sum_double
'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
'''

def mysum_double(a, b):
  if a==b: return 2 * (a + b)
  else: return a + b
    
def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum

with Timer(verbose=True) as t:
    mysum_double(3,6)
    
with Timer(verbose=True) as t:
    sum_double(3,6)


# In[5]:

## Wormup-1.4 diff21
'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
'''

def mydiff21(n):
  if n > 21:
    return (abs(21 - n))* 2
  else: return abs(21 - n)
    
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2


with Timer(verbose=True) as t:
    mydiff21(16)
    
with Timer(verbose=True) as t:
    diff21(16)


# In[6]:

## Wormup-1.5 parrot_trouble
'''
We have a loud talking parrot. 
The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
Return True if we are in trouble.
'''

def myparrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
    
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

with Timer(verbose=True) as t:
    myparrot_trouble(True, 7)
    
with Timer(verbose=True) as t:
    parrot_trouble(True, 7)


# In[7]:

## Wormup-1.6 makes10
'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
'''

def mymakes10(a, b):
  if (a == 10 or b == 10): return True
  elif a + b == 10: return True
  else: return False
    
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)

with Timer(verbose=True) as t:
    mymakes10(9, 9)
    
with Timer(verbose=True) as t:
    makes10(9, 9)


# In[8]:

## Wormup-1.7 near_hundred
'''
Given an int n, return True if it is within 10 of 100 or 200. 
Note:abs(num) computes the absolute value of a number.
'''

def mynear_hundred(n):
  return ((abs(n-100) <= 10 ) or (abs(n-200) <= 10))
    
def near_hundred(n):
  return ((abs(n-100) <= 10 ) or (abs(n-200) <= 10))

with Timer(verbose=True) as t:
    mynear_hundred(180)
    
with Timer(verbose=True) as t:
    near_hundred(180)


# In[9]:

## Wormup-1.8 near_hundred
'''
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.
'''

def mypos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

with Timer(verbose=True) as t:
    mypos_neg(-1,3,True)
    
with Timer(verbose=True) as t:
    pos_neg(-1,3,True)


# In[10]:

## Wormup-1.9 not_string
'''
Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged. 
'''

'''
def mynot_string(str):
  no idea
'''

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

with Timer(verbose=True) as t:
    not_string("bad")


# In[11]:

## Wormup-1.10 missing_char
'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
'''

def mymissing_char(str, n):
  return str[:n] + str[n+1:]

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

with Timer(verbose=True) as t:
    missing_char('code', 2)
    
with Timer(verbose=True) as t:
    mymissing_char('code', 2)


# In[30]:

## Wormup-1.11 front_back
'''
Given a string, return a new string where the first and last chars have been exchanged.
'''

def myfront_back(str):
  n = len(str)
  if n <=1:return  str
  return str[n-1] + str[1:n-1]+ str[0]



def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]



with Timer(verbose=True) as t:
    myfront_back('Chocolate')
    
with Timer(verbose=True) as t:
    front_back('Chocolate')


# In[31]:

## Wormup-1.13 front3
'''
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.
'''

def myfront3(str):
  if len(str) < 3:
    return 3*str
  else: return 3*str[:3]
    
def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 


with Timer(verbose=True) as t:
    myfront3('Chocolate')
    
with Timer(verbose=True) as t:
    front3('Chocolate')

