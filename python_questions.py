# This is a list of python interview questions I have encountered over time 

#########################################
#What is Python really? 
# It's interpreted programming language which means it doesn't ne
# need to be compiled before it runs 
# also like PHP and Ruby 


# dynamically typed which means you don't need to state data types with variables 

# is well suited OO programming language which allows class, 
# construction, composition, and inheritance 

# Python's functions are first class objects 
# - assigned to variables and returned from other functions and passed into functions 
# Classes are also first class objects 

# Python is quicked but still slower than compiled languages 
# like C++, C. But it does allow the inclusion of C based 
# extensions 
# Numpy is an example because the number crunching isn't actually done 
# in Python 

# Lastly, it's commonly used in 
# - web applications (Django, Pyaramid, Flask)
# -automation scripts 
#- scientific modeling through numpy, pandas, scipi
#- big data applications 
# - you can find as glue code to make other languages work 
# better each other 

###############################################

# Is Python and multi-threading a good idea? 

# IT DOESN'T ALLOW MULTI-THREADING IN THE TRUEST SENSE 
# Therefore it's not best to use Python for multithreading

# Why? 
# - it contains what's callled a global interpreter lock
# - a thread requires an GIL, does some work, and then passes into the next thread 
# - the threads are really just taking turns using the CPU core 
# You can still use this if efficiency isn't a concern 

#The multi-threading can be outsourced to another external application (Hadoop or Spark)
# or some code that your Python code calls (C multithreading code)



###############################################
# How do you keep track of different versions of your code? 

# Version-Control through Git and GitHub. It helps tracking cod generation, what's 
# actually added to the code base, finding different bugs in the code, and allows you 
# to conduct rollbacks to the code if it doesn't work 


###############################################
# What is monkey patching and is it ever a good idea? 

# Monkey patching is changing the behavior of a function or object before it is actually defined 
# It's a pretty bad idea because you want the functions to act in a well-defined way 



