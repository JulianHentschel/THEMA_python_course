
# conditional statement is to do a specific operation based on if something is True or False
# if statements are incredibly useful, but try not to overuse them or at least use them smartly
# what happens in the computer when an if happens, is that it can initiate a "jump" in the command sequence
# if we have a lot of if statements forcing the program jump back and forth in the execution, this impacts performance

a_random_number = 5
# makes a statement that returns a boolean True or False
if a_random_number <= 10:
    print(f"{a_random_number} is lower or equal to 10")  # this line of code is encapsulated under the above if

# if the above if is False, the code in else will run. Having else in if statements is optional
else:
    print(f"{a_random_number} is higher than 10")

# if statements can have multiple conditions
random_string = "THEMA"
if len(random_string) == 5 and "MA" in random_string:
    print("It checks out!!")

# you can add a second if that only is tried if the first one is not True
elif len(random_string) < 5:
    print("Something has changed")

lookup_set = {1, 2, 3, 4}
random_int = 6
# several boolean approaches showed in last lesson can be used as conditionals
if random_int in lookup_set or random_int > max(lookup_set):
    print("All good")

