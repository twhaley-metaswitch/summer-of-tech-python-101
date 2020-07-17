import random


# 1 - Let's create a class called OurClass, with a property named x.
class OurClass:
    x = 7


# Create a variable called "our_object" that is an instance of this class.
our_object = OurClass()
# Access and print the property of our_object.
print(our_object.x)
# Update and print our_object's property.
our_object.x = 0
print(our_object.x)


# 2 - The __init__() function.
# The above example is pretty much as simple as a class can get.
# Python classes use the built-in __init__() function, which is executed when the class is
# instantiated. We can use this to assign properties, or do anything else when the object is created.

# Let's create a class representing a coin, called "Coin", which is instantiated with a monetary
# value, which defaults to 1.0.
# Let's also define a property describing which side of the coin is face-up, defining a
# class function to "flip" the coin.
class Coin:

    # Notice that the first parameter is self. This refers to the current instance
    # of an object, and is (almost) always the first parameter of functions in classes.
    def __init__(self, value=1.0):
        self.value = value
        self.side_facing_up = "heads"

    # Again, the first (and only) argument is self, referring to the current object instance.
    def flip(self):
        # Let's get Python to generate a random integer between 0 and 1,
        # using that to choose head or tails.
        if random.randint(0, 1):
            self.side_facing_up = "heads"
        else:
            self.side_facing_up = "tails"


# Create an instance of the Coin class. Flip the coin and print the result.
# This creates us an instance of the Coin class.
coin = Coin()
# We use the flip function to "flip" the coin.
coin.flip()
# We print the side that is currently face up.
print(coin.side_facing_up)

# Let's flip the coin 10 times. Printing the result each time.
# Let's use a for loop to ensure we don't have to write the same code over and over again.
# The range function gives us a list of numbers to iterate through.
for x in range(10):
    coin.flip()
    # Here we can use Python's f-strings to make the string formatting nicer.
    print(f"Flip #{x}: {coin.side_facing_up}")


# 3 - Inheritance.
# When we define classes, we can inherit properties and function from other classes.
# This is called inheritance.
# The class being inherited from is called the Parent class, and the class that inherits is called
# the child class.

# Create another instance of "Coin", specifying a value of 0.05.
coin = Coin(0.05)

# In the UK, this would be a perfectly valid value for a coin to have, but in New Zealand,
# where the smallest denomination is 0.10, this isn't the case.

# You see that we might want to create new classes, which inherit all the properties of a coin,
# but have some changes specific to where the coin is from.

# Let's create a new class for New Zealand coins, which inherits from the Coin class.
class NewZealandCoin(Coin):
    # We define a list of allowed values that the coin can have.
    allowed_values = [0.10, 0.20, 0.50, 1.0, 2.0]

    # We use the __init__() function again, using a default value of 1.0.
    def __init__(self, value = 1.0):
        # When initialising child classes, you can use Python's super() function to inherit the
        # methods and properties from the parent class.
        super().__init__(value)

        # In addition to this, we want to check that the specified value is valid,
        # raising an Exception if not.
        # Notice that we are able to extract
        if self.value not in self.allowed_values:
            raise Exception(f"Specified value of coin is not in allowed list: {self.value}")

    # We can add new methods to this child class.
    def print_description(self):
        # Notice that this string is split over multiple lines. Python code often sticks to a
        # maximum line length. I've tried to stick to a maximum length of 100 characters.
        print(
            f"This is a New Zealand coin with value {self.value}, "
            f"and {self.side_facing_up} facing up"
        )


# Let's try this new class out.
# Creating an object with a value of 0.05 should throw an exception.
# Uncomment the line below to see this for yourself.
# nz_coin = NewZealandCoin(0.05)
# Creating a coin with a valid value works nicely.
nz_coin = NewZealandCoin(0.5)
# Let's flip the coin and print a description.
nz_coin.flip()
nz_coin.print_description()


# This has barely scratched the surface of what you can do with Python classes. I would encourage
# you to search online for tutorials to help you practise and understand more.
