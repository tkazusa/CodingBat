
# coding: utf-8

# In[1]:

## String-2.1 double_char
'''
Given a string, return a string where for every char in the original, there are two chars.
'''

def double_char(str):
    new_char = ""
    for char in str:
        new_char += char*2
    return new_char

double_char('Hi-There')


# In[2]:

## String-2.2 count_hi
'''
Return the number of times that the string "hi" appears anywhere in the given string.
'''

def count_hi(str):
    count = 0
    for i in range(0,len(str)-1):
        if str[i] + str[i+1] == "hi": count += 1
    return count

count_hi('hiho not HOHIhi')


# In[3]:

## String-2.3 cat_dog
'''
Return True if the string "cat" and "dog" appear the same number of times in the given string.
'''

def cat_dog(str):
    return str.count('dog') == str.count('cat')

cat_dog('catxdogxdogxcat')


# In[4]:

## String-2.4 count_code
'''
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
'''

def count_code(str):
    count = 0
    for i in range(0, len(str)-3):
        if str[i] =='c' and str[i+1] == 'o' and str[i+3] == 'e': 
            count +=1
    return count

count_code('xxcozeyycop')


# In[5]:

## String-2.5 end_other
'''
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
aNote: s.lower() returns the lowercase version of a string.

'''

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    longer, shorter = a, b
    if len(a) < len(b): longer, shorter= b, a
    return  longer[-len(shorter):] == shorter


end_other('ab', 'ab12')


# In[6]:

## String-2.6 xyz_there
'''
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.
'''

def xyz_there(str):


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



