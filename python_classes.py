# These are notes about Python classes 


class Complex:
  def __init__(self, realpart, imagpart):
      self.r = realpart
      self.i = imagpart

# __init__ is automatically invoked when a new instance is created 

x = Complex(3.0, -4.5)
x.r, x.i
(3.0, -4.5)

#


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs
'canine'
e.kind                  # shared by all dogs
'canine'
d.name                  # unique to d
'Fido'
e.name                  # unique to e
'Buddy'

####################################
#Things to Know:
####################################
# Python supports multiple inheritance 


####################################
# What are iterators? 
# Adding iterators to your classes: 

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self): #returns one element
        return self

    def __next__(self): #Accesses the elements one at a time 
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

####################################
#an example of a generator


They are written like regular functions but use the yield statement whenever 
they want to return data. Each time next() is called on it, the generator resumes 
where it left off (it remembers all the data values and which statement was last 
executed). An example shows that generators can be trivially easy to create:

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# f
# l
# o
# g

####################################
# What about special methods in Python? 

# Classes can implement certain operations with a special syntax 
# using the special methods


__init__ #initializes new instance of the class 

__new__ #returns an instance of the class followed by the __init__ method being invoked

__del__ #called to delete a method 

__repr__  #computes official string representation of an object 

__str__ #does the same as above only there are no exceptions

__bytes__ #gives bytes representation of an object

__format__ #does the same as above 

__hash__ #used for members of hash collections 

__bool__ #called for truth value testing and built for booleans

# getter and setters 

__get__ #get a attribute value (reader); method can be called like Class.method

__set__ # set attribute value (writer) Class.method = new_value

__delete__ #delete method delete Class_instance 

__len__ #returns the length of the object


__reversed__ # reverse iteration 

__contains__ #checks for membership in a data structure 

# What about for mathematical operations:

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)









