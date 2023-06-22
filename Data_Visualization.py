# 8.9 LAB: Data Visualization

# (1) Write a function, get_data_headers(), to prompt the user for a title, and column headers for a table. Return a list of three strings, and print the title, and column headers. (2 pt) 

# Ex:

# Enter a title for the data:
# Number of Novels Authored
# You entered: Number of Novels Authored

# Ex:

# Enter the column 1 header:
# Author name
# You entered: Author name

# Enter the column 2 header:
# Number of novels
# You entered: Number of novels

# (2) Write a function, get_data_points(), that prompts the user for data points, and returns a dictionary where the keys are the string component of the data points, and the values are the integer component of the data points.

# Data points must be in this format: string, int. Store the information before the comma into a string variable and the information after the comma into an integer. The user will enter -1 when they have finished entering data points. Output the data points on each iteration. (4 pts)

# Ex:

# Enter a data point (-1 to stop input):
# Jane Austen, 6
# Data string: Jane Austen
# Data integer: 6

# (3) Improve the get_data_points() function by performing error checking for the data point entries. If any of the following errors occurs, output the appropriate error message and prompt again for a valid data point.

# If entry has no comma
# Output: Error: No comma in string. (1 pt)
# If entry has more than one comma
# Output: Error: Too many commas in input. (1 pt)
# If entry after the comma is not an integer
# Output: Error: Comma not followed by an integer. (2 pts)

# Ex:

# Enter a data point (-1 to stop input):
# Ernest Hemingway 9
# Error: No comma in string.

# Enter a data point (-1 to stop input):
# Ernest, Hemingway, 9
# Error: Too many commas in input.

# Enter a data point (-1 to stop input):
# Ernest Hemingway, nine
# Error: Comma not followed by an integer.

# Enter a data point (-1 to stop input):
# Ernest Hemingway, 9
# Data string: Ernest Hemingway
# Data integer: 9

# (4) Write a function, print_data(), that takes the table header information list created in (1) and the dictionary created in (3). The function will output the information in a formatted table. The title is right justified with a minimum field width value of 33. Column 1 has a minimum field width value of 20. Column 2 has a minimum field width value of 23. (3 pts) 

# Ex:

#         Number of Novels Authored
# Author name         |       Number of novels
# --------------------------------------------
# Jane Austen         |                      6
# Charles Dickens     |                     20
# Ernest Hemingway    |                      9
# Jack Kerouac        |                     22
# F. Scott Fitzgerald |                      8
# Mary Shelley        |                      7
# Charlotte Bronte    |                      5
# Mark Twain          |                     11
# Agatha Christie     |                     73
# Ian Flemming        |                     14
# J.K. Rowling        |                     14
# Stephen King        |                     54
# Oscar Wilde         |                      1

# (6) Write a function, print_histogram(), to output the data point information formatted as a histogram. Each name is right justified with a minimum field width value of 20. (4 pts) 

# Ex:

#          Jane Austen ******
#      Charles Dickens ********************
#     Ernest Hemingway *********
#         Jack Kerouac **********************
#  F. Scott Fitzgerald ********
#         Mary Shelley *******
#     Charlotte Bronte *****
#           Mark Twain ***********
#      Agatha Christie *************************************************************************
#         Ian Flemming **************
#         J.K. Rowling **************
#         Stephen King ******************************************************
#          Oscar Wilde *


def get_data_headers():
    title = input("Enter a title for the data:\n")
    print(f'You entered: {title}\n')
    
    column1_header = input("Enter the column 1 header:\n")
    print(f'You entered: {column1_header}\n')
    
    column2_header = input("Enter the column 2 header:\n")
    print(f'You entered: {column2_header}\n')
    
    return [title, column1_header, column2_header]

def get_data_points():
    data_points = {}
    while True:
        data_point = input("Enter a data point (-1 to stop input):\n")
        if data_point == "-1":
            break
        parts = data_point.split(", ")
        if len(parts) < 2:
            print("Error: No comma in string.\n")
            continue
        elif len(parts) > 2:
            print("Error: Too many commas in input.\n")
            continue
        try:
            data_string, data_integer = parts[0], int(parts[1])
            data_points[data_string] = data_integer
            print(f'Data string: {data_string}')
            print(f'Data integer: {data_integer}')
        except ValueError:
            print("Error: Comma not followed by an integer.")
            continue
    return data_points

def print_data(headers, data):
    print(f'{headers[0]:>33}')
    print(f'{headers[1]:<20} | {headers[2]:>23}')
    print("-"*44)
    for key, value in data.items():
        print(f'{key:<20} | {value:>23}')

def print_histogram(data):
    for key, value in data.items():
        print(f'{key:>20} {"*"*value}')
    
if __name__ == '__main__':
    headers = get_data_headers()
    data = get_data_points()
    print_data(headers, data)
    print_histogram(data)