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
#You want to keep it simple 

#The only reasons to monkey patch would be testing

##############################################
# What does this stuff mean: *args, **kwargs? And why would we use it?

# *args --> allows multiple arguments as a list or tuple when we don't know how many 
# arguments there should be 

# kwargs --> we don't know how many keywords should be passed to a function 


#############################################
# What do these mean to you: @classmethod, @staticmethod, @property?

# a decorator is a special type of function which takes a function and returns a function 

# ex) 
@some_decorator 
def some_function(stuff): 
  # do_some_stuff

# More examples: 

class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kwargs):
        print("calling normal_method({0},{1})".format(args,kwargs))
    @classmethod
    def class_method(*args,**kwargs):
        print("calling class_method({0},{1})".format(args,kwargs))
    @staticmethod
    def static_method(*args,**kwargs):
        print("calling static_method({0},{1})".format(args,kwargs))
    @property
    def some_property(self,*args,**kwargs):
        print("calling some_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_property
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print("calling some_property setter({0},{1},{2})".format(self,args,kwargs))
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kwargs):
        print("calling some_other_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_other_property


# Know the OOprogramming well and know how the super function works 


#############################################
# How does Python prepare garbage collection? 

# This how it works in gist: 
# 1. Maintains count of reference to objects in memory 

# 2. The garbage collection looks for reference cycles and cleans them up periodically 
 # 
# 3. Heuristics are used to speed garbage collection. Recently created objects are more likely 
# to be dead. Objects are created and the object collector assigns them to generations. Each object 
# gets generations, and younger generations are dealt with first. 

#############################################
# Which is the most efficient? 
# checks if value in array is < 0.5 and returns it's squared value
# 

def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5] #most n length
    l2 = sorted(l1) #most n length 
    return [i*i for i in l2] #

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

# Use cProfile to evaluate efficiency 

# it's obviously quicker to sort a list if it's a smaller list 
# therefore, you shoul filter the list before it's sorted to reduce its size 

# Yes I'm currently working a on data visualization projects using the D3.js library 
# I've created a couple of projects as listed on my resume, but most of my projects lately are data graphs using D3.js 


#############################################
