
# coding: utf-8

# In[1]:

## logic-2.1 make_bricks
'''
We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops.
'''

def make_bricks(small, big, goal):
    result = (goal%(5*big))%small
    return result == 0

make_bricks(3, 2, 10)


# In[2]:

## logic-2.2 lone_sum
'''
Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values, it does not count towards the sum.
'''

def lone_sum(a, b, c):
    sum = 0
    sum += a if a not in [b,c] else 0
    sum += b if b not in [a,c] else 0
    sum += c if c not in [a,b] else 0
    return sum

lone_sum(3, 2, 3)


# In[3]:

## logic-2.3 lucky_sum
'''
Given 3 int values, a b c, return their sum. 
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
So for example, if b is 13, then both b and c do not count.
'''

def lucky_sum(a, b, c):
    sum = 0
    for i in [a,b,c]:
        if i == 13: break
        sum += i
    return sum
        
lucky_sum(1, 2, 13)


# In[4]:

## logic-2.4 no_teen_sum
'''
Given 3 int values, a b c, return their sum.
However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
Define the helper below and at the same indent level as the main no_teen_sum().
'''

def no_teen_sum(a, b, c):
    def fix_teen(n):
        return n if n not in [13,14,17,18,19] else 0
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

no_teen_sum(2, 1, 14)


# In[5]:

## logic-2.5 round_sum
'''
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
Write the helper entirely below and at the same indent level as round_sum().
'''

def round_sum(a, b, c):
    def round10(num):
        if num%10 <=4: roundnum = num//10 * 10
        else: roundnum = (num//10+1)*10
        return roundnum
    return round10(a)+round10(b)+round10(c)

round_sum(12, 13, 14)


# In[6]:

## logic-2.6 close_far
'''
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. 
Note: abs(num) computes the absolute value of a number.
'''

def close_far(a, b, c):
    return (abs(abs(b)-abs(c))>=2)     and ((abs(abs(b)-abs(a))<=1 
    and abs(abs(c)-abs(a))>=2) 
    or (abs(abs(c)-abs(a))<=1 
    and abs(abs(b)-abs(a))>=2))
    
close_far(1, 2, 3)


# In[7]:

## logic-2.7 make_chocolate 
'''
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done.
'''

def make_chocolate(small, big, goal):
    result = -1
    remain = 0
    for i in range(0,big):
        if 5*i < goal: 
            remain = goal % 5*i  
    if remain <= small: result = remain
    return result
    
make_chocolate(7, 2, 13) 


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



