

def main():

    # you will be asked to write a series of functions that you can test with predefined inputs

    # alter this variable to run code for the different tasks
    task_to_run = 1

    if task_to_run == 1:
        # task 1
        # write the function show_me_the_math() with the inputs num_1 and num_2
        # the function should return a tuple with these calculations:
        # num_1 + num_2, num_1 * num_2, num_1 mod num_2

        # this code calls your functions and prints the output
        my_calculations = show_me_the_math(num_1=2, num_2=9)
        print(f"The func return should be (11, 18, 1). The actual return is {my_calculations}")

        my_calculations = show_me_the_math(num_1=2020465, num_2=430485)
        print(my_calculations)


    elif task_to_run == 2:
        # task 2
        # write a function that calculates the fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21, etc.) and returns it as a list
        # the function must be called calc_fibo() and have length as an input.
        # the length parameter will specify the length of the fibonacci sequence to be returned from the function
        # E.G. length=4 should return [1, 1, 2, 3], while length=7 should return [1, 1, 2, 3, 5, 8, 13]
        # the function must also have the optional input only_last, which is by default set to False
        # if only_last is set to True, only the last value in the fibonacci sequence should be returned as an integer
        # a tip is to think simple, use list, loop and positional referencing

        my_fibo_list = calc_fibo(7)
        print(my_fibo_list)
        my_fibo_int = calc_fibo(length=60, only_last=True)
        print(f"The func return should be 1548008755920. The actual return is {my_fibo_int}")
        my_very_short_fibo_list = calc_fibo(1)
        print(f"The func return should be [1] of type <class 'list'>. The actual return is {my_very_short_fibo_list} "
              f"of type {type(my_very_short_fibo_list)}")

    elif task_to_run == 3:
        # task 3
        # create the function count_chars that has the input input_string
        # the func should return a dictionary where the keys are characters and the values are the number of time that char was in the input text
        # E.G count_chars("Hello hi") should return {'H': 2, 'E': 1, 'L': 2, 'O': 1, 'I': 1}
        # all characters should be counted, but lower case and upper case letters shouldn't be separated, and space shouldn't be counted.

        my_letter_dict = count_letters("To be or not to be")
        print(my_letter_dict)



    elif task_to_run == 4:
        # task 4
        # create a custom numeric sorting function called custom_sort.
        # the function will have two inputs. input_list and the optional input reverse=False
        # the func will sort numeric input in the input list in ascending order, and in descending order if reverse=True
        # do not use any built-in functions like max(), min() or sorted.
        # this is a tricky task, so here follows some pointers to a possible approach
        # use a loop inside another loop. An outer loop that adds new numbers to a sorted list and removes these number from the input list
        # the inner loop can find the lowest or highest number in the input list

        unsorted_list = [5, 12, 4, 21, 3, 16, 40, 4, 13]
        sorted_list = custom_sort(unsorted_list)
        print(sorted_list)
        reverse_sorted_list = custom_sort(unsorted_list, True)
        print(reverse_sorted_list)


    else:
        print("Your task_to_run variable has an invalid number")



if __name__ == "__main__":
    main()


