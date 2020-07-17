# 1 - Printing
# Let's start with printing, and the traditional "Hello, world!" output.
# Here we're using the inbuilt print function to print a string to the output console.
print("Hello, world!")
# You can pass print multiple arguments.
print("Hello", "world")


# 2 - Maths
# 2.1 - Integers
# We can perform simple arithmetic on integers in Python, using all the basic mathematical
# operators:
# + : Addition
# - : subtraction
# * : multiplication
#
#
# For example:
5 + 7
6 - 2
8 * 4
9 / 3
7 % 2
2 ** 3
# Operator precedence is obeyed. The following should give an answer of 2:
10 - 2 * 4
# Parentheses (brackets) also work as you would expect. The following should give an answer of 32:
(10 - 2) * 4

# 2.2 - Floating point numbers
# Numbers with decimal points tend to behave a little strangely on computers.
# For example, see what happens when you divide 10 by 3, you get 3.3333333333333335.
# An error has been introduced.
# For now, just be aware that decimal numbers aren't handled perfectly by computers.
10 / 3
# As an aside, in older versions of Python, the / operator acting on integers used to do integer
# division. In other words, it would do simple division and ignore any remainder. So 10 / 3 would
# have been 3. This behaviour has been changed, but you can stil perform integer division by using
# the // operator.
10 // 3

# 2.3 - Printing our results
# Let's print the results of a sum.
print("The result of 2 + 2 is", 2 + 2)


# 3 - Variables
# Instead of printing or displaying the previous results, we could have stored that data in variables.
# In Python, we assign data to variables using the "=" operator.
# This stores the integer 2020 in the variable called year.
year = 2020
# We can print or display this variable in the Python console.
print(year)

# 3.2 - Numbers in variables
# We can store number in variables, and use them to perform calculations.
seats = 1000
attendees = 600
spare_seats = seats - attendees
print(spare_seats)

# 3.3 - Text in variables
# You can also store text in variables.
# You can use both single and double quotes to denote string variables.
name = "Your Name"
known_as = 'You'
print("name:", name)
print("known as:", known_as)
# When using single our double quotes, you might occasionally need to escape apostrophes.
message = "I'm a string"
message = 'I\'m a string'


# 4 - Types and Casting
# Python is a "typed language", meaning that there are multiple different types of objects,
# and they don't all act in the same way.
# So far we've looked at integers (int), floats (float), and strings (str).
# Different types don't always interact nicely. For example, try running the following:
# "7" + 8
# This will result in a TypeError. Python doesn't know how to add a string and a number.
# But, the following output might surprise you:
"7" + "8"
# The "+" operator concatenates strings.
"7" + "even"
# Likewise, the "*" operator "multiplies" string, i.e. concatenates them a certain number of times.
# e.g. the following will result in "77777777"
"7" * 8
# Where Python is able to do something sensible, it can cast between these types.
# For example, this will result in the int 7:
int("7")
# And this will result in the str "7":
str(7)


# 5 - Control flow using variables
# Now we know about variables and storing data, we can look at control flow (if / else statements).
# The following code looks at the number variable, and prints different strings depending on
# which comparision is true.
# NOTE: you can start a new line in the Python console by typing shift + enter. Once you've added
# as many lines as you need, you can then press enter twice to execute the code you've typed.
# Python is looking at each if statement in turn, and evaluating the truth of it.
number = 4
if number > 3:
    print("Bigger than 3")
elif number < 3:
    print("Smaller than 3")
else:
    print("Is 3")
# Each statement is producing a True / False value. These are Python objects of type bool.
print(number > 3)
# In fact, we can treat lots of things as True / False.
# 0 is False
bool(0)
# 1 is True
bool(1)
# The empty string is False.
bool("")
# A string with any contents is true, even if it says False!
bool("False")
# The fact that we can consider objects as True or False in Python is extremely useful.


# 6 - Lists
# In Python, list objects are an ordered collection of things, specified using the [ and ] characters.
# For example, we might have a list of countries:
countries = ["Mexico", "Portugal", "Kenya", "Nepal", "New Zealand"]
# 6.1 - Indexes
# Lists are ordered, so if you ask for the first element, it will always be the same value,
# unless you modify the list. Python uses 0 (zero) indexing, so the indexes start at 0, not 1.
# This is common throughout many program languages.
# We extract specific elements from a list using square braces ([]).
# We pull out the first element like so:
print(countries[0])
# And the third like this:
print(countries[3])
# You can use negative numbers to index from the end of the list.
# For example, the last element has the -1th index.
print(countries[-1])
# The following statement would throw an index error, because there's is no 5th element.
# countries[5]
# 6.2 - Modifying
# Lists are mutable, meaning that their contents can be changed once created.
# You can change the value of an existing element by setting the specific element.
countries[1] = "Spain"
print(countries)
# You can append.
countries.append("United Kingdom")
print(countries)
# You can sort a list. Either obtaining a new list.
sorted_countries = sorted(countries)
print(sorted_countries)
# or sorting in-place:
countries.sort()
print(countries)
# Lists are Python objects, and Python objects have methods defined on them.
# There are loads of these, have a look at the Python documentation for more detail:
# https://docs.python.org/3.5/tutorial/datastructures.html#more-on-lists
# 6.3 - Subsets
# You can get a subset of a list, using [] again, alongside a colon.
# To get the first 4 elements:
print(countries[0:4])
# You can omit the 0, like so:
print(countries[:4])
# You can get also go from index 4 to the end.
print(countries[4:])
# You can use negative numbers to index from the end of the list.
# The following will pull out the last 2 elements.
print(countries[-2:])
# If you use an index that is out of range, Python will just return what it finds
# instead of throwing an error.
# For example, this will just return the whole list, missing the first element.
print(countries[1:100])
# 6.4 - Nesting
# Since the elements of a list are just Python objects, and lists are themselves objects, nested
# Lists are a perfectly sensible thing.
# For example:
countries_by_continent = [["Mexico"], ["Portugal", "United Kingdom"], ["Kenya"], ["Nepal"], ["New Zealand"]]


# 7 - Tuples
# These are just like lists, an ordered collection of objects, but they are immutable.
# This means that once they're created, they can't be changed. Trying to modify a tuple will
# result in a TypeError.
# Tuples are represented by ( and ) characters.
countries = ("Mexico", "Portugal", "Kenya", "Nepal", "New Zealand")
print(countries)
# Indexing etc. all work as with lists, only the elements can't be changed.
print(countries[0:3])
# If you do need to update the contents of a tuple, you can always cast as a list.
countries_list = list(countries)
countries_list.append("UK")
# You can then cast back to a tuple.
countries = tuple(countries_list)


# 8 - Dictionaries
# Dictionary objects store key-value pairs. Where keys and their values can be any Python object.
# For example, we might want to map countries with their official languages.
# Notice that we can use a list for NZ's multiple languages.
languages = {
    "UK": "English",
    "New Zealand": ["English", "Te Reo Maori", "NZSL"]
}
# We can access entries using square braces:
print(languages["New Zealand"])
# We can add or modify entries in dictionaries by using square braces.
languages["Canada"] = ["English", "French"]
# We can also delete entries.
del(languages["UK"])
# 8.1 - .keys(), .values(), and .items()
# Like lists, dicts have plenty of object methods.
# There are methods to get hold of lists containing keys, values,
# and lists of tuples describing key-value pairs.
print(languages.keys())
print(languages.values())
print(languages.items())
# These lists can be useful for iterating through the contents of dictionaries.
# Note that unlike lists, dictionaries aren't sorted in any way.


# 9 - Comprehensions
# Python offers something incredibly powerful called comprehensions.
# These provide a compact way to define lists.

# For example, you might want to create a list containing the first 5 square numbers.
# Let's first trying this using Python's for loop.
# The indentation here is important. Notice as well how the code reads like a sentence.
numbers = [1, 2, 3, 4, 5]
square_numbers = []
for number in numbers:
    square_number = number**2
    square_numbers.append(square_number)

# This can be compacted down using Python list comprehensions.
# This is basically saying:
#     For each x in this list, create a new list by squaring the elements of the first list.
square_numbers = [x**2 for x in numbers]
# You can also add restrictions. For example, what if we only want the square of odd numbers?
square_odd_numbers = [x**2 for x in numbers if x % 2 == 1]
# In actual fact, because of the truthy-ness of 0 and 1, you don't need the "==" check at the end.
square_odd_numbers = [x**2 for x in numbers if x % 2]
# These list comprehensions can be split up into the following sections, separated by <>:
# [<output expression> for <variable> in <input sequence> <optional test>]

# You can also do similar things for dictionaries, as well as a few other Python types.


# 9 - Functions
# A function is a collection of statements grouped together, that can be called later to run these statements.
# Python has loads of built-in functions that you can use. One example is the print function.
print("This is a function")
# You can store the output of a function in a variable for use later.
# We'll do this with the built-in function len().
length_of_string = len("this is my string")
print(length_of_string)
# Try running len on a list as well.
print(len([1, 2, 3, 4]))


# 9.1 - Defining functions
# You can create your own methods. This is done using the def keyword, providing a unique name for
# the function, and specifying any parameters that may be accepted by the function.
# We then write the code we want to be run when the function is called.
# Again, indentation is important, the body of the function is indented from the definition.
def print_name():
    print("My name is blah")

# Calling this function is like calling any other we've seen.
print_name()
# Notice that there were no arguments to this method. We can change the method to use a parameter.
# If we were to run this as a script Python would complain, because we've defined two methods with
# the same name.
def print_name(name):
    print("My name is " + name)

print_name("blah")

# We can enhance a function further by specifying default values for parameters if one is not provided.
# This is done using the = character.
def print_name(name = "blah"):
    print("My name is " + name)


# These functions print a string, but they return None (the "nothing" value in Python,
# other languages often call this null). We can return something using the return statement.
def get_statement(name="blah"):
    return "My name is " + name

# We can then use the output of this function as we would any other variable.
statement = get_statement("B. Blah")
print(statement)

# Functions make writing and reading code a lot easier. It reduces the need to copy and paste code,
# and allows developers to abstract away complicated logic.
# As a general rule, code will be read more times than it is written, so making it easier to read is very important.
