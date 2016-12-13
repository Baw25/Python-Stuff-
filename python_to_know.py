#############################################
# These are the things you must know: 
#############################################

# What are the high level differences between Python 2 and 3? 

# One thing you must understand is that as long as the version, 
# supports the libraries you want to use, you can use either of them 


#############################################
# What can Python be used for?: 
#############################################
#Scripting language for large applications
# supplies high level dynamic language types and supplies dynamic checking 
# easily integrates with C and C++ 
# supports automatic garbage collection
# 

#############################################
# What are some differences between 2 and 3: 
#############################################

#Print


#1. print function was changed to wrapping the 
# printable objects within a parantheses 
# end = option to print more text on the same line 

#Division 

# 2. A slight change in the division operation: 
# which allows decimal answers

# to make it compatible for Python 2, in Python 3 it's 
# best to still use the decimal version for the divisor or 
# dividend or use float

# Unicode - there's UTF-8 and 2 byte classes in byte and 
# byte array's 

# Strings are now UTF-8 


#3. range() in Python 3 is implemented like xrange()
# for creating iterable objects 


#4. Raising exceptions must be in parantheses in Python 3

# 5. Handling Exceptions: where the as keyword must be used 
# - 


# 6. for loop variables no longer leak into global namespace 
# variables again 

# 7. List comprehensions have similar syntactic sugar similar 
# to generator expression inside a list 


# 8. A TypeError is changed when we try to compare unorderable 
# types in 

#9. Input in Python 3 always reads input() as strings 


# 10. New Standard way of rounding - decimals are now rounded to the next
# even number which rounding up eliminating bias towards larger numbers

#############################################
# Main things to know: 
#############################################

# 1. Python has strong typing which is completely different from JS

# you can't just add 'hello' + 10 == hello10 (concatenate string with int)


# 2. You don't need an interface for a required function paramater which
# makes polymprphism easier than C++ 

# 3. The ability to extend Python with C and C++ 


#4. Common Web Technologies in Python: 
# Develop in Django or Pyramid or Flask 

#5. Ability to use it in scientific communities with libraries like: 
# numpy 
# scipy
# Pandas 
# IPython shell 

# 5. Standard libraries that support internet protocol: 
# HTML and XML 
# JSON 
# Email - processing 
# FTP and IMAP internet protocols
#Web socket interfaces 


#6. Pythons ability to be used as a support language: 
# - for build control 
# - management 
#  - testing 

# using Scons, Buildbot and Apache Gump, and Roundup 

#############################################
# Testing your code in Python: 
#############################################
# Focus on tiny bits of functionality using 
# each test is run alone regardless of the order in the test suite 
# handled by setup() and teardown() methods 

# always run the full testing suite before coding sessions

# Using Unittest - all included test module

import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

# DocTest -  searches for pieces of text that look like interactive 
# Python sessions in docstrings, and then executes those sessions to 
# verify that they work exactly as shown.

# Sample 

def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# Testing libraries and modules: 

# Mock 
# Pytest 
# Tox for automating test evironments
# Nose 


#############################################
# Difference between a dictionary and set: 
#############################################

#Sets

# Sets are like lists but hold distinct elements 
# the set doesn't change when you add element X to the 
# set because X is already there

# In a list it wil change

#Dictionaries 

# are used if you want to make associative data hashable 
# and super fast lookup times with a constant BigO 
# No ordering in dictionaries 


#############################################
# Copies and Lists: 
#############################################

list1 = [1,2,3,4,5]  
list2 = list1  
list2.append(6)  
list2  
[1, 2, 3, 4, 5, 6]  
list1  
[1, 2, 3, 4, 5, 6]  

# making one list equal to another means that you making 
# two vars pointing to the same list in memory 


# Changing dictionary within a dictionary will result 
# in updates to the outer dictionary too 
# The solution to this is using a deep copy method 

#############################################
# What does the yield keyword do?:
#############################################

The yield enables a function to comeback where it left off when it is called again. 
It allows the function to remember its state 

#############################################
# Generators:
#############################################

#Generator function is a way to create an iterator. A new generator object is returned each time the generator is called.
# allows for processing data's in batches instead of all at once for huge data sets


# Generators in Python provide us with the advantageous concept of lazy evaluation, 
# so when we “construct” generators, we don’t actually evaluate some value within it 
# unless it’s absolutely needed. 

# This saves memory

# Therefore it's better to use xrange() over range() because 
# xrange() is a generator and its capable of lazy evaluation 
#range possesses xrange() qualities in python 3 


# However, we still need lists because values in generator objects 
# don't exist unless needed on demand. Also the second loop for gnerators 
# tends to fail. Therefore, generators are not best for looping. 

# What are generators best for? 

# If we construct a generator that consists of the numbers 1 through N for 
# large N, and our code ends up only needing the first three numbers, then Python 
# doesn’t need to construct and store the remaining numbers in memory as it would 
# for a list. (This hypothetical scenario could happen because there might be a 
# function with different N values for each call that uses a generator.

#############################################
# #File Management:
#############################################

#ex) 

f = open('test.txt', 'r')  
for line in f:  
  # Read each line  
f.close()  

# We use f.close() to free up memory or use with 

# You use File IO for reading and writing files 


#############################################
# #Lists:
#############################################

list2 = list1[start:stop:step]  









