# iterating, or looping, is an efficient way to repeat the same code on several elements stored together
# loops can be computing intensive because it goes through one and one element. Particularily if we have loops inside other loops.
# but despite this, loops are actually a quite efficient computing form when used wisely.
# loops are very predictable for the operating system running your code, and it can optimise its execution

my_list_of_numbers = [23, 45, 22, 31, 12]

# lists are iterable, and really shine when used in iteration
# there are two basic ways we can iterate over a list. Both useful for different situations

# iterating over by index. We create a counting int variable that increases by one for each iteration
for i in range(len(my_list_of_numbers)):
    if my_list_of_numbers[i] > 30:
        print(f"The value at index {i} is high")

# we can also iterate over the elements itself
for number in my_list_of_numbers:
    if number % 2 == 0:  # checks if number is even number
        print(f"{number} is an even number")

# for most situations, the second approach presented here is the best as it is much easier to work on the object number instead of an index value
# learning when to use what approach is just trial and error. But remember that you must have a reason to use approach 1, approach 2 should be the default

# tuples can be iterated over in the same way as a list, but lists are more common to use when having to iterate
my_set = ("An", "iterable", "set")
for element in my_set:
    print(element)

# dictionaries are also iterable. As dicts and sets aren't indexed, the second approach in the list example must be used
my_dict_of_stuff = {"Jon": 31, "Maria": 26, "Axel": 53}
for name in my_dict_of_stuff:
    print(f"{name} is {my_dict_of_stuff[name]} years old")

# much like tuples, sets are iterable, but not often used for this
my_set = {"All", "unique", "values"}
my_other_set = {"Not", "that", "unique"}
for value in my_set:
    if value not in my_other_set:
        print(f"{value} is only in one set")
    else:
        print(f"{value} is in both sets")

# remember that sets and dictionaries aren't ordered, so do not use dict or set when the order of the iterable is important
# lists or tuples are your go-to for such cases


