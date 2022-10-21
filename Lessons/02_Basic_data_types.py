import sys
# a computer really only sees the world as 1 and 0, but we can choose how to interpret this to something we can work on
# this is where data types come in

# in this lesson, we will cover the following data types:
# 1. Boolean
# 2. Integer
# 3. String
# 4. Floating Point Number
# 5. Tuple
# 6. List
# 7. Set
# 8. Dictionary

# certain functions and actions in python are very sensitive to what data type the input to this function has.
# this is why this is important

# 1. Boolean
print("\n 1. Boolean")
# boolean is the most basic of variables, and represent only one single bit that is either 1 or 0, or True or False
is_done = True
is_satisfied = False

print("Are you done and satisfied?")
print(is_done and is_satisfied)  # if any of these boolean variables are False, the answer will be False

print("Are you either done or satisfied?")
print(is_done or is_satisfied)  # if any of these boolean variables are True, the answer will be True

print("Are you not done?")
print(not is_done)  # 'not' can inverse True to False and False to True

# boolean variables are used a lot as return variables from functions
print("Are these expressions true?")
print(5 > 3)
print(5 < 3)
print(len("THEMA") == 5) # remember len() operator from previous lesson
print(5 != 4 + 2) # '!=' means not equal to
print(not 5 == 4 + 2) # equal to previous expression

# you can cast or change a variable to a boolean type using the bool() casting function
non_boolean_variable = 1
boolean_variable = bool(non_boolean_variable)  # this really only makes sense for integers that are 1 or 0
print("Integer represented as a boolean variable:")
print(boolean_variable)

# the boolean concept is important when dealing with conditionals (if expressions) later on

# 2. Integer
print("\n2. Integer")
# when talking about integers, we have to start with geeking it out a bit with binary numbers
# Decimal number digits can be 0-9, and combined to represent any number.
# We can achieve the same with just each digit being 1 or 0 as in a binary system.
# Our normal decimal system is of base10
print(5789)
print("Is the same as:")
print((10**3 * 5) + (10**2 * 7) + (10**1 * 8) + (10**0 * 9))  # ** in python equals ^, so power of.

# the binary system is base2. So in the above logic we would have to switch out 10s for 2s
print("The binary number 1101 is equal to the decimal number:")
print((2**3 * 1) + (2**2 * 1) + (2**1 * 0) + (2**0 * 1))

# a quicker way to transform base2 to base10 is to use the int() casting function
base2_variable = '1101'
base10_variable = int(base2_variable, base=2) # specify the base of the number in the casting function
print(base10_variable)

# you will very rarely have to deal with binary numbers, but it's nice to know how integers are stored in memory.
# while boolean variables only use 1 bit, integers in python have a dynamic bit allocation based on size of number.
# the maximum bit allocation for integers in the standard python package is 64 bits.
# the first bit is used to specify if the value is negative or positive, hence integers must be between -2^63 and 2^63
# integers outside this range must be cast to Floating-Point Numbers. More on this later.

# casting string and floats to int
a_floating_point_number = 10.0
print(type(a_floating_point_number))  # type can be used to check what the data type of the variable is
an_integer = int(a_floating_point_number)  # if float can't be cast to int, program will crash
print(type(an_integer))

# the input() function always outputs a string that will have to be converted to an int if used in arithmetic
user_input = input("If you don't type in something that can be casted to integer, the program will crash: ")
user_input = int(user_input) + 3
print(user_input)
# we would never write a program that could crash so easily. More on error handling in a later lesson.


# 3. String
print("\n3. String")
# a computer only store and handle 0s and 1s, so how can characters be stored and represented?
# the answer is to have a standardised mapping between bit pattern and characters
# the ASCII standard is the grandfather of character encoding, and specify the mapping between bytes(8 bits) and charcters
# this is a link to the mapping table https://ascii-tables.com/
# as 8 bits only can make 2^8=255 unique bit combinations, this mapping is not sufficient for all signs we would need
# to account for this, an extension to ASCII was created, UTF-8. Characters not covered by ASCII will have > byte size
# this is most likely not something you would have to care about, but in some cases when reading in data, encoding standard must be specified

random_string = "Hello people"  # note that strings must be encapsulated in either "" or ''
encoded_string = random_string.encode("ASCII")  # pythonic way to encode to ASCII
binary_string = (bin(int.from_bytes(encoded_string, byteorder=sys.byteorder)))[2:]  # you're not expected to understand this code
decoded_string = encoded_string.decode("ASCII")  #pythonic way to decode from bytes to human readable string

print(f"The binary representation of {str(decoded_string)} is : {str(binary_string)}")  #note the syntax here to combine several strings into one

# because strings are a bundle of individual characters, they can be sliced, diced and merged as we want
string_to_be_sliced = "Ja vi elsker dette landet"
print(string_to_be_sliced[0])  # returns the first character in string
print(string_to_be_sliced[-1])  # returns the last character in string
print(string_to_be_sliced[:2])  # returns the first two characters in string
print(string_to_be_sliced[-2:])  # returns the last two characters in string
print(string_to_be_sliced[4:9])  # returns a slice from the middle section of the string
print(len(string_to_be_sliced))  # returns the number of characters in string

string_to_be_added = " som det stiger frem"
combined_string = string_to_be_sliced + string_to_be_added  # adding together two strings is easy.
# be careful to see if numbers are in string format. When trying to add that together things get funky. E.G. 2+3=23
print(combined_string)
print(combined_string.upper())  # upper capitalises all letters, lower() does the opposite.
word_list = combined_string.split(" ")  # .split() allows you to split a string into a list based on a specified delimiter. In this case space
print(word_list)  # the list data type will be explained further down

combined_string = "_".join(word_list)  # the opposite of split is to join an iterable of strings on a specified delimiter. _ in this case
print(combined_string)
print(combined_string.replace("_", " "))  # a regex function where we want to replace the string _ with a space

# 4. Floting Point Number
print("\n4. Floating Point Number")
# as you remember, integers had a lower and higher value it had to be between.
# number outside this range, and fractional values like 1.5, are represented as Floating Point numbers, or as a float
# a floating pont is an approximation of the actual value coded on this format int * base^exp. E.G. 7.6875 = 123*2^-4
# in general it requires more bits to represent floating numbers compared to integers.

# some functions specify that input and/or output must be either integer or float.
# integers can always be converted to floats, but fractional floats cast to ints will round down to the nearest integer
integer_number = int(10)
print(integer_number)
float_number = float(integer_number)
print(float_number)
print(int(1.8))  # this will be rounded down
print(integer_number+float_number)  # the results from arithmetics involving a float will also be of type float


# 5. Tuple
print("\n5. Tuple")
# tuples is a data structures that contains other variables and/or data structures.
# after they are created, they can't be changed in any way.
# should only be used where you have very fixed data you know will not need to be changed.
# tuples are faster than lists, but lists can be changed. They are immutable, meaning you can't order, append, edit or delete any tuple element
# no problems with duplicates, add whatever you like to a tuple as long as you do it all at once.

#the basic syntax of tuple is:
my_first_tuple = (3, "four", 5.0)  # the elements in a tuple can only be immutable. Meaning they can't be changed
print(len(my_first_tuple))  # the number of elements in a tuple can be found with len()
print(my_first_tuple[1])  # access tuple elements using index
print(my_first_tuple[1:])  # multiple elements can be accessed

# we can even have a tuple inside another tuple. Tuple-ception!
leonardo_deTupleio = ("something", (1, 2, 3), "something else")
print(len(leonardo_deTupleio))  # the number of elements in the tuple is still only three
print(leonardo_deTupleio[1][2])  # referencing nested tuples like this quickly turns messy, so don't over use such structures
print(sum(leonardo_deTupleio[1]))  # easy to sum up tuple values. Can also use min() and max() to find highest and lowest value
print("something" in leonardo_deTupleio)  # easy to check if a certain element/value is in tuple. But Set and Dictionary will be much quicker when dealing with many elements.

# code trying to edit tuple element. The try-except setup will be covered later, but it handles the error without crashing the program
try:
    leonardo_deTupleio[0] = leonardo_deTupleio[0].upper()
except Exception as e:
    print(f"Tuple error message: {e}")


# 6. List
print("\n6. List")
# list is the flexible cousin of tuples
# they are mutable, meaning you can go crazy and change and remove list elements, add new ones, and change the order

# the basic syntax of list is:
my_first_list = [1, "two", 3.0]
my_first_list.append("FOUR")  # appends new element at end of list
print(my_first_list[2])  # list elements are fetched in the same way as for tuples
my_first_list[0] = "One"  # list elements can be overwritten or changed
del my_first_list[2]  # list elements can be deleted. Be aware that this will reindex the list
print(my_first_list[:2])

# lists can also be initialized without any elements
my_second_list = []
my_second_list.append(5)
my_third_list = [4, 2, 1, 3]
my_second_list.extend(my_third_list)  # when joining two lists, use extend instead of append. Append would create a list inside a list instead of a common list
print(my_second_list)
print(sorted(my_second_list, reverse=True))  # lists can be sorted. Reverse is an optional argument that defaults to False

print(sum(my_second_list))  # easy to sum up lists. Can also use min() and max() to find highest and lowest value
print(3 in my_second_list)  # easy to check if value/element is in list. But Set and Dictionary will be much quicker when dealing with many elements.


# 7. Set
print("\n7. Set")
# like tuples and lists, sets are also used to store other elements/objects
# but items in tuples are not ordered and not indexed. Meaning you can't reference them by their place in the Set.
# objects in sets have to be unique, and existing objects in a set can't be changed. Objects can be added and deleted.
# what is unique with sets is that each object becomes its own reference, which makes it quick to look up in.
# it is the same reason why each object must be unique.
# if you want to read more about this, google hash tables

# this is the basic syntax of creating a Set
my_first_set = {10, 15, 20}  # like with tuples, only immutable objects can be in sets
print(my_first_set)

# set is most used for looking up values in
print(10 in my_first_set)  # when you have a lot of values to check for matches in, Sets are much quicker than tuples and lists

print(max(my_first_set))  # you can also use sum(), max() and min()

# elements are added to sets like this:
my_first_set.add(25)
my_first_set.add(15)  # when trying to add an element already in set, it will be ignored

# elements are removed like this:
my_first_set.discard(10)  # note that you have to specify the actual element. You can't specify position

my_second_set = {1, 2, 3}
my_second_set = my_second_set.union(my_first_set)  # you can join two sets using the union() operator
print(my_second_set)


# 8. Dictionary
print("\n8. Dictionary")

# dictionary is an extension of sets
# it allows for adding a value to the key used in set

# the syntax goes like this
my_first_dict = {"September": 30, "October": 31, "November": 30}  # here the unique keys are months, and the value is days in each mont
# the keys have to be unique and immutable, but the value can be whatever you like and can be changed later
print(my_first_dict)

# the value of each key can be fetched like this:
print(my_first_dict["October"])

print("November" in my_first_dict)  # like with set, dicts are also very efficient for looking up in

# new key-value pairs are added to the dict like this:
my_first_dict["December"] = 31
print(my_first_dict)
my_first_dict.pop("December")  # use pop() to remove keys and its associated value from dict
print(my_first_dict)

my_second_dict = {"June": 30, "July": 31, "August": 30}
my_second_dict.update(my_first_dict)  # there are many ways to merge two dictionaries. update() is one of them
print(my_second_dict)
