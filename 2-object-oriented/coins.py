import random


# 1 - Let's create a class called OurClass, with a property named x.


# Create a variable called "our_object" that is an instance of this class.

# Access and print the property of our_object.

# Update and print our_object's property.


# 2 - The __init__() function.
# The above example is pretty much as simple as a class can get.
# Python classes use the built-in __init__() function, which is executed when the class is
# instantiated. We can use this to assign properties, or do anything else when the object is created.

# Let's create a class representing a coin, called "Coin", which is instantiated with a monetary
# value, which defaults to 1.0.
# Let's also define a property describing which side of the coin is face-up, defining a
# class function to "flip" the coin.


# Create an instance of the Coin class. Flip the coin and print the result.


# Let's flip the coin 10 times. Printing the result each time.


# 3 - Inheritance.
# When we define classes, we can inherit properties and function from other classes.
# This is called inheritance.
# The class being inherited from is called the Parent class, and the class that inherits is called
# the child class.

# Create another instance of "Coin", specifying a value of 0.05.


# In the UK, this would be a perfectly valid value for a coin to have, but in New Zealand,
# where the smallest denomination is 0.10, this isn't the case.

# You see that we might want to create new classes, which inherit all the properties of a coin,
# but have some changes specific to where the coin is from.

# Let's create a new class for New Zealand coins, which inherits from the Coin class.


# Let's try this new class out.
# Creating an object with a value of 0.05 should throw an exception.

# Creating a coin with a valid value works nicely.

# Let's flip the coin and print a description.


# This has barely scratched the surface of what you can do with Python classes. I would encourage
# you to search online for tutorials to help you practise and understand more.
