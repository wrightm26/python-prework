#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1:
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
#The first line of the code has been defined as below. def hello_name(user_name):
def hello_name(user_name):
    """Display a simple greeting."""
    print("\nhello_" + user_name.upper() + "!")

hello_name('username')


# In[15]:


#Question 2:
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
def first_odds():
    """Display odd numbers up to 100."""
    current_number = 0
    while current_number <100:
        current_number += 1
        if current_number %2 == 1:
            print(current_number)
            continue

first_odds()


# In[10]:


#Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list.
#The first line of the code has been defined as below. def max_num_in_list(a_list):
a_list = [1, 2, 3, 4, 5, 6, 7]
def max_num_in_list(a_list):
    """Display the maximum number in the list."""
    max(a_list)

print(max(a_list))


# In[11]:


#Question 4:
#Please write a Python function, max_num_in_list to return the max number of a given list.
#The first line of the code has been defined as below. def max_num_in_list(a_list):
def is_leap_year(a_year):
    """Return True if the year inputted is a leap year."""
    year = False

    if a_year % 400 == 0:
        year = True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        year = True
    return year

a_year = int(input())
print(is_leap_year(a_year))





# In[9]:


#Question 5:
#Write a function to check to see if all numbers in the list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type. def is_consecutive(a_list):
def is_consecutive(a_list):
    """Return True if the numbers are consecutive."""
    maximum = max(a_list)
    if sum(a_list) == maximum * (maximum + 1) /2:
        return True
    return False

a_list = [1,2,3,4,5,,6,7]
is_consecutive(a_list)


# In[2]:


os.chdir(c:Users\18649\OneDrive\Documents\python_prework\python_questions)


# In[ ]:
