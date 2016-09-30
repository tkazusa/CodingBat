
# coding: utf-8

# In[1]:

## logic-1.1 cigar_party
'''
When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.
'''

def cigar_party(cigars, is_weekend):
    return cigars >= 40 if is_weekend else cigars in range(40,61)

cigar_party(70, True) 


# In[2]:

## logic-1.2 date_fashion
'''
When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.
'''

def date_fashion(you, date):
    if you <= 2 or date <=2:
        return 0
    elif you >=8 or date >=8:
        return 2
    else:
        return 1
    
date_fashion(5, 2) 


# In[3]:

## logic-1.3 squirrel_play
'''
The squirrels in Palo Alto spend most of the day playing. 
In particular, they play if the temperature is between 60 and 90 (inclusive).
Unless it is summer, then the upper limit is 100 instead of 90.
Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
'''

def squirrel_play(temp, is_summer):
    return temp in range(60, 101 if is_summer else 91)
    
squirrel_play(95, False)


# In[4]:

## logic-1.4 caught_speeding
'''
You are driving a little too fast, and a police officer stops you.
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. 
If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
'''

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed += 5
    if speed > 80:
        return 2
    elif speed> 60:
        return 1
    else:
        return 0
    
caught_speeding(65, False)


# In[5]:

## logic-1.5 sorta_sum
'''
Given 2 ints, a and b, return their sum. 
However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
'''

def sorta_sum(a, b):
    result = a + b
    if 9 < result < 20: result = 20
    return result


# In[6]:

## logic-1.6 sorta_sum
'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. 
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
'''

def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6: return 'off'
        else: return '10:00'
    else:
        if day == 0 or day == 6: return '10:00'
        else: return '7:00'
        
alarm_clock(5, False) 


# In[7]:

## logic-1.7 love6

'''
The number 6 is a truly great number.
Given two int values, a and b, return True if either one is 6.
Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
'''

def love6(a, b):
    return  a == 6 or b == 6 or a-b== 6 or a+b == 6 or b-a == 6

love6(7, 5)


# In[8]:

## logic-1.8 in1to10

'''
Given a number n, return True if n is in the range 1..10, inclusive.
Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
'''

def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    return 1<=n<=10

in1to10(10, True)


# In[9]:

## logic-1.9 near_ten

'''
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
'''

def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8
    
near_ten(155)


# In[ ]:




# In[ ]:




# In[ ]:



