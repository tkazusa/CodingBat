
# coding: utf-8

# In[1]:

## String-1.1 hello_name
'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
'''

def hello_name(name):
    return 'Hello ' + name + '!'

hello_name('xyz!')


# In[2]:

## String-1.2 make_abba
'''
Given two strings, a and b, return the result of putting them together in the order abba,
e.g. "Hi" and "Bye" returns "HiByeByeHi".
'''

def make_abba(a, b):
    return a + b + b + a

make_abba('x', 'y')


# In[3]:

## String-1.3 make_tags
'''
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
'''

def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

make_tags('body', 'Heart')


# In[4]:

## String-1.4 make_out_word
'''
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>". 
'''

def make_out_word(out, word):
    front = out[:2]
    back = out[2:]
    return front + word + back

make_out_word('[[]]', 'word')


# In[5]:

## String-1.5 extra_end
'''
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
The string length will be at least 2.
'''

def extra_end(str):
    return str[-2:]*3

extra_end('Candy')


# In[6]:

## String-1.6  first_two
'''
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "". 
'''


def first_two(str):
    if len(str) < 2:
        return str
    return str[0:2]

first_two('Kitten')


# In[7]:

## String-1.7  first_half
'''
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo". 
'''

def first_half(str):
    n = int(len(str)/2)
    return str[0:n]

first_half('kitten')


# In[8]:

## String-1.8  without_end
'''
Given a string, return a version without the first and last char, so "Hello" yields "ell". 
The string length will be at least 2.
'''

def without_end(str):
    return str[1:-1]

without_end('kitten') 


# In[9]:

## String-1.9  combo_string
'''
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty (length 0).
'''

def combo_string(a, b):
    na, nb  = len(a), len(b)
    if na > nb: longer , shorter = a , b
    else: shorter , longer = a , b
    return shorter + longer + shorter 

combo_string('aaa', 'bb')


# In[10]:

## String-1.10  non_start
'''
Given 2 strings, return their concatenation, except omit the first char of each. 
The strings will be at least length 1.
'''

def non_start(a, b):
    return a[1:] + b[1:]

non_start('java', 'code')


# In[11]:

## String-1.11  left2
'''
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
The string length will be at least 2.
'''

def left2(str):
    return str[2:] + str[0:2]

left2('Chocolate')

