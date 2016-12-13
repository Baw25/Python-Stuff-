######################################
#These are sample interview questions 
######################################

#What are python dictionaries?

# Python's dictionaries are kind of hash table type. 
# They work like associative arrays or hashes found in Perl and 
# consist of key-value pairs. A dictionary key can be almost any Python type, 
# but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

#What are tuples in Python? 

# A tuple is another sequence data type that is similar to the list. 
# A tuple consists of a number of values separated by commas. Unlike lists, 
# however, tuples are enclosed within parentheses.

#Tuples can not update values and are immutable


#What is the PythonPath environment var? 

# This variable tells the Python interpreter where to locate the module 
# files imported into a program. It should include the Python source library 
# directory and the directories containing Python source code. PYTHONPATH is 
# sometimes preset by the Python installer.

#Explain how Python's compile time and run time code are different: 

# Python performs some amount of compile-time checking, but most of the checks 
# such as type, name, etc are postponed until code execution. Consequently, if 
# the Python code references a user -defined function that does not exist, the 
# code will compile successfully. In fact, the code will fail with an exception 
# only when the code execution path references the function which does not exists.

#Explain Python's zip function: 

#input : takes multiple lists 

#output: creates single list of tuples by matching them with the corresponding 
# elements in the othger list 

list1 = ['A',
'B','C'] and list2 = [10,20,30].
zip(list1, list2) 
# results in a list of tuples say [('A',10),('B',20),('C',30)]
