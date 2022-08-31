import pandas
import time

# some code to make it easier to run a selection of this pandas lesson
import pandas as pd

part_dict = {"1": "Importing and viewing data", "2": "Making subsets",
             "3": "Extending and combining data", "4": "Iterating over a data frame",
             "5": "Do vectorized operations on data frame"}
print("\nParts in Pandas lesson:")
for option in part_dict:
    print(f"{option}: {part_dict[option]}")
user_input = ""
while user_input not in part_dict:
    user_input = input("Select the number corresponding to the part you want to run code for: ")



# pandas is THE goto tool for basic data handling in python
if int(user_input) == 1:
    # part 1, Importing and viewing data
    print("\nPart 1")
    # csv files are easily imported like this
    data_file = pandas.read_csv("Data/Production.csv")

    # with head() you can specify how much of the file to print out. Great for inspecting the data
    print("\nThe data head:")
    print(data_file.head(4))

    print("\nThe data head for the Profile column:")
    print(data_file["Profile"].head(4))

    # index is a great way to make it easier to follow the unique data in the dataset
    # setting one or multiple columns as index can be done with set_index, or by specifying index column when reading in data
    data_file.set_index("Description", inplace=True)
    print("\n The data head after indexing:")
    print(data_file.head(4))

    # note the difference compared to the same command earlier before setting an index
    print("\nThe data head for the Profile column after indexing:")
    print(data_file["Profile"].head(4))

elif int(user_input) == 2:
    # part 2, Making subsets
    print("\nPart 2")

    # data is fetched, and index is specified as column 0
    data_file = pandas.read_csv("Data/Production.csv", index_col=0)

    # pandas makes it easy to get out specific information from the data frame (df)
    # here we get the index and profile where the column REF_2025 is above a certain value
    filtered_df = data_file["Profile"].loc[data_file['REF_2025'] > 40000000]
    print("\nA subset of the df:")
    print(filtered_df)

    # when using the index, this is the approach to get the Profile for a given index
    single_value = data_file.loc["AUT_Industry"]["Profile"]
    print("\nThe profile for AUT_Industry:")
    print(single_value)

    # when not using the index, iloc[0] must be added to get the actual value.
    # without it, you will get a df with the index and the value
    new_single_value = data_file["Zone"].loc[data_file["Profile"] == "D_CHE_HEAT"].iloc[0]
    print("\nThe Zone for the profile D_CHE_HEAT:")
    print(new_single_value)

    # data frames can also be subset by positional index, but this is rarely a great idea
    a_bad_way_to_subset = data_file["Zone"].iloc[4]
    print("\nThe Zone for row 5:")
    print(a_bad_way_to_subset)

elif int(user_input) == 3:
    # part 3, Extending and combining data
    print("\nPart 3")

    # we create our own df from a list of list
    our_own_df = pd.DataFrame([["Norway", "Oslo"], ["Sweden", "Stockholm"], ["Denmark", "Copenhagen"]],
                              columns=["Country", "Capital"])
    our_own_df.set_index("Country", inplace=True)
    print("\nOur special df:")
    print(our_own_df)

    # we can now easily expand this df with another column
    our_own_df["EU_member"] = [False, True, True]
    print("\nOur special df after adding a column:")
    print(our_own_df)

    # we create another similar df
    another_df = pd.DataFrame([["Germany", "Berlin", True], ["France", "Paris", True]], columns=["Country", "Capital", "EU_member"])
    another_df.set_index("Country", inplace=True)

    # these two dfs can be merged together using concat. Remember to have the same index and columns
    concatenated_dfs = pd.concat([our_own_df, another_df])
    print("\nThe concatenated dfs:")
    print(concatenated_dfs)

    yet_another_df = pd.DataFrame([["Norwegian", "NOK"], ["Swedish", "SEK"], ["Danish", "DKK"],
                                   ["German", "EUR"], ["French", "EUR"]], columns=["Language", "Currency"])

    # when using concat to add together dfs horizontally, axis must be =1 or ='columns'
    # pandas will also expect the index to be the same, so here we had to reset index for our original df to make it work
    even_more_concatenated_dfs = pd.concat([concatenated_dfs.reset_index(), yet_another_df], axis="columns").set_index("Country")
    print("\nMore concatenated dfs:")
    print(even_more_concatenated_dfs)

    # joining pandas dfs together can be a bit tricky, so practice makes master.
    # this site has a lot of good examples: https://realpython.com/pandas-merge-join-and-concat/

    # the syntax for saving panda dfs as csv files
    even_more_concatenated_dfs.to_csv("Data/Country_facts.csv")

elif int(user_input) == 4:
    # part 4, Iterating over a data frame
    print("\nPart 4")

    # we read in the data we have saved
    df = pd.read_csv("Data/Country_facts.csv", index_col=0)

    print("\nThe output from iterrow():")
    # the most basic way to iterate over df is by using iterrows()
    for index, row in df.iterrows():
        print(f"\nThe entire content of row for {index}:\n{row}")
        print(f"The capital of {index} is {row['Capital']}")

    # iterating over a df is not particularly efficient, but can be justified on small data sets
    # a better option is often to use vectorization

elif int(user_input) == 5:
    # part 5, Do vectorized operations on data frame
    print("\nPart 5")

    # vectorized operations are a way to utilize that most modern CPUs have the possibility to apply the same operation
    # to multiple data points at the same time, significantly speeding up execution compared to a standard loop
    # further reading: https://stackoverflow.com/questions/1422149/what-is-vectorization#:~:text=Vectorization%20is%20the%20term%20for%20converting%20a%20scalar,%22vector%22%20--%20of%20numbers%20in%20a%20single%20step.

    # let's read in the biggest file I could find in our systems
    data_file = pandas.read_csv("Data/Profile_Summary.txt")
    print(data_file.head())

    # let's imagine we have to do some funky arithmetics on these figures
    # let's write it out in a regular loop and time it
    data_file_copy = data_file
    start_time = time.time()
    our_computed_thingy = []
    for index, row in data_file.iterrows():
        if row["Average/Total"] == "-":
            my_number = 0
        else:
            my_number = float(row["Average/Total"])
        our_computed_thingy.append(round(my_number * 3 / 6 ** 1.2) % 37)




    print(f"Not using vectorization took {time.time()-start_time} sec to execute")
    print(data_file_copy.head(5))



