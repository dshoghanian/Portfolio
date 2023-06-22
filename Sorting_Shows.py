# 9.13 LAB: Sorting TV Shows (dictionaries and lists)

# Instructor note:
# Skills Reinforced:

# Writing to a file
# Dictionaries & Lists
# Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a list of TV shows are the values (since multiple shows could have the same number of seasons).

# Sort the dictionary by key (greatest to least) and output the results to a file named output_keys.txt. Separate multiple TV shows associated with the same key with a semicolon (;), ordering by appearance in the input file. Next, sort the dictionary by values (in reverse alphabetical order), and output the results to a file named output_titles.txt.

# Ex: If the input is:

# file1.txt
# and the contents of file1.txt are:

# 20
# Gunsmoke
# 30
# The Simpsons
# 10
# Will & Grace
# 14
# Dallas
# 20
# Law & Order
# 12
# Murder, She Wrote
# the file output_keys.txt should contain:

# 30: The Simpsons
# 20: Gunsmoke; Law & Order
# 14: Dallas
# 12: Murder, She Wrote
# 10: Will & Grace
# and the file output_titles.txt should contain:

# Will & Grace
# The Simpsons
# Murder, She Wrote
# Law & Order
# Gunsmoke
# Dallas
# Note: End each output file with a newline, and file1.txt is available to download.

def read_file(file_name):
    """
    Read a file and create a dictionary of TV shows by season.

    Args
    ----
    file_name : str
        The name of the file to read.

    Returns
    -------
    dict
        A dictionary where keys are seasons and values are lists of TV shows.
        
    """
    with open(file_name, 'r') as file:
        data = file.readlines()

    data = [item.strip() for item in data]

    tv_dict = {}
    for i in range(0, len(data), 2):
        season = int(data[i])
        tv_show = data[i + 1]

        if season in tv_dict:
            tv_dict[season].append(tv_show)
        else:
            tv_dict[season] = [tv_show]

    return tv_dict


def sort_and_write(file_name, tv_dict, by_value=False):
    """
    Sort a dictionary and write it to a file.

    Args
    ----
    file_name : str
        The name of the file to write to.
    tv_dict : dict
        A dictionary of TV shows by season.
    by_value : bool, optional
        Whether to sort by TV show title. Defaults to False.
    """
    if by_value:
        sorted_items = sorted([(k, v) for k, vs in tv_dict.items() for v in vs], key=lambda x: x[1], reverse=True)
    else:
        sorted_items = sorted(tv_dict.items(), key=lambda x: x[0], reverse=True)

    with open(file_name, 'w') as file:
        for item in sorted_items:
            if by_value:
                file.write(f'{item[1]}\n')
            else:
                file.write(f'{item[0]}: {"; ".join(item[1])}\n')


def main():
    """Read a file, create a dictionary of TV shows by season, and write it to two files."""
    file_name = input()
    tv_dict = read_file(file_name)
    sort_and_write('output_keys.txt', tv_dict)
    sort_and_write('output_titles.txt', tv_dict, by_value=True)


if __name__ == "__main__":
    main()
