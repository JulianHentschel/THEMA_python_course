# so far we have only looked at code that executes from top to bottom
# in this lesson we will learn how to structure code into custom functions that can be called throughout the code

# functions are declared with def followed by an optional function name and ()
# note that code that 'belongs' to the function is indented under the function
def main():

    first_input_int = 4
    second_input_int = 8

    # if we want to square these two number, we could just do this:
    print(first_input_int**2)
    print(second_input_int**2)

    # or we could write our own custom function we could call with these integers as input.
    # Locate the function square_int further down in the script to have a look at it
    print(square_int(first_input_int))
    print(square_int(second_input_int))
    # as you can see, calling this custom function is just like calling any other function
    # the reason we customise functionality like this, is to organise code into chunks, and minimize duplication of code

    # function inputs can be specified in two ways. Positionally as previous example, or as keyword arguments as showed here:
    print(sum_ints(int1=first_input_int, int2=second_input_int, as_string=True))

    # we can have functions with a variable number of inputs
    print(make_string("T", "H", "E", "M", "A"))  # here each letter is an input argument

    # we can also have functions with a variable number of named inputs
    print(f"In non leap years there are {sum_winter_months(January=31, February=28, December=31)} winter days")

    # the input formats can be mixed up, but positional arguments must come first
    print(personal_text_maker("Simen", age=31))


# here we define an expected input to the function
def square_int(int_input):

    # what the function will return
    return int_input**2


# we can also specify optional inputs. Here as_string is optional, and defaults to False if not given
def sum_ints(int1, int2, as_string=False):
    if as_string:
        return str(int1+int2)
    else:
        return int1+int2

# we can also make functions where the number of input arguments is flexible
# *args can be several input arguments, but they have to be positional arguments
def make_string(*args):
    return_string = str()
    for arg in args:  # more on this iteration in next lesson
        return_string += str(arg)

    return return_string

# we can also make functions where the input arguments are flexible in both numbers and keyword
# this is often used in addition to required inputs in order to expand the functionality of the function without making the function input definition look messy
def sum_winter_months(**kwargs):
    return kwargs["December"] + kwargs["January"] + kwargs["February"]


# There are function documentation standards we should do our best to follow diligently.
# Especially for code that'll be exposed externally. Remember, less is not necessarily more
# When passing dictionaries or more advanced data structures, more extensive documentation is expected. See lesson 6.
def personal_text_maker(name, age, Norwegian=True):
    """
    Function for writing personal text

    Args:
        name(str):
        The name of the person

        age(int):
        The age of the person

        Norwegian(bool, optional):
        Boolean indicator of Norwegian nationality

    Returns:
         personal_text (str):
         A personal text based on the given inputs
    """
    personal_text = f"{name} is {age} years old"
    if not Norwegian:
        personal_text += " and has moved to Norway from abroad"

    return personal_text

# this is good coding practice to have at bottom of scripts to avoid the entire script running when importing file into other code
# google it if you want to understand why it is smart to do
if __name__=="__main__":
    main()