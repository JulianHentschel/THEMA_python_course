
# the first thing that has to be said about python syntax is that # comments out what's left of it
# meaning that it will avoid being run as code and is good practice to add to explain code

# the code in a python file can either be run from the terminal (the geeky way), or by pressing play in your IDE
# on execution of code files, all the code in the file will be run
# if the file imports code from other files, this will also be run
# you can also work in a notebook where parts of the code can be run more easily and the results are kept in memory

# python is particularly great because there are so many packages that can be imported into your code.
# packages are just pieces of code other people have written, so that you don't have to.
# this is the basic syntax of importing:

# importing the whole package
import os

# importing the whole package but renaming it. This is very common for certain packages like pandas and numpy
import pandas
import pandas as pd
import numpy as np

# only import a certain part of a package. Can be useful if the package is big, and you only need a very small part of it
from math import sqrt, pi


# often you will have to install these packages in you python enviroment. Some are in the python core itself, others are not.
# use this syntax in your terminal window to install packages: pip install package_name
# E.G. pip install pandas. Or multiple packages at the same time, pip install pandas, numpy
# it is also possible to install it with the help of your IDE

print("Hello!")  # a super useful command that can print out more or less anything to command line. Indispensable for debugging

# variables/objects are used to store data temporarily while the code executes
greeting_message = "Hello!" # the operating system allocates a slot to this data in memory(RAM) that can be accessed later
print(greeting_message)

# something that separates python from many other languages (like Java) is that you don't need to declare the variable type
the_first_number = 9  # this in Java would be int the_first_number = 9;
the_second_number = 4  # this in Java would be int the_second_number = 4;

# python does its best in guessing what variable type it is.
# variable type can also be changed during code execution, or specified clearly by us as coders.
# more on this in the next lesson

# basic arithmetic is also embedded in python
# calculates the sum of these numbers
the_sum = the_first_number + the_second_number
print("The sum of the numbers:")
print(the_sum)

# calculates the modulus of these numbers
the_modulus = the_first_number % the_second_number
print("The modulus of the numbers")
print(the_modulus)

# let us make some objects based on some of the packages we imported. More on these packages later.
df = pd.DataFrame()  # creates an empty table
array = np.array([])  # creates an empty array

# the function we imported from math can be used on its own
the_root = sqrt(9)  # calculates the square root
print("The square root of a number:")
print(the_root)

# the os package was imported in its entirety, so the syntax for accessing its functions is this:
the_current_working_directory = os.getcwd()
print("The current working directory: ")
print(the_current_working_directory)

# as you might have noticed, when executing functions we end with (). Sometimes with some input inside the ().
# but when we're just interested in getting a variable, we have to drop the ().
the_number_pi = pi #  we imported the variable of pi earlier
print("The number pi:")
print(the_number_pi)

# what this means is that you will need to know if what you are accessing in a package/object is a function or a variable


# we also have to talk about python style guide.
# the agreed upon style guide for python code is PIP 8 (https://peps.python.org/pep-0008/)
separate_using_under_score = "Thumbs up"  # the naming convention for python is using underscore
separateUsingCamelCase = "Thumbs down"  # some other code languages use camelCase to split up names. Not Python!

# it is also good coding practice to use descriptive variable and function names.
var1 = "Never do this!"
user_feedback = "Do this!"
# certain special cases for using variable names like i and x can be acceptable to use sometimes. More on this later.

# input(input message) can be used to have user input from the terminal.
# python use indentation to encapsulate code. Other programming languages can use {} to encapsulate code.
user_input = input("Input a word: ")
if len(user_input) > 5:  # checks if length of word is more than 5 characters. More on the use of 'if' later
    print("User input is more than 5 letters")  # this is encapsulated under the above 'if'
else:
    print("User input is less than or equal to 5 letters")  # this is encapsulated under the above 'else'


# this concludes lesson 1!

