# Create a random password generator

import random

upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # all upper-case letters
lower_letters = upper_letters.lower() # all lower-case letters
digits = '0123456789' # all numbers
symbols = '!@#$%^&*()_-+=?><' # all symbols

#need to make them all true so the if statements can execute
upper = True 
lower = True
num = True
symb = True

#create an empty string to combine all variable
all = ''

# if statements execute while the variables are TRUE
if upper:
    all += upper_letters
if lower:
    all += lower_letters
if num:
    all += digits
if symb:
    all += symbols

# length: number of characters
# amount: number of passwords
length = 12
amount = 1

# for loop executes with the amount
for i in range(amount):
    # create password variable ''.join(joins the variables into the string) random.sample combines all and the length to create password
    password = ''.join(random.sample(all, length)) 

print(password)
