# 4.18 LAB: In-N-Out Ordering (Long)

# Design a program to manage the basic In-N-Out ordering of shakes and french-fries.

# A few menus and prompts are pasted below. Since this program is heavy on input/output interactions, please study the output for each of the test cases given.

# We suggest you program incrementally. When writing input statements, end each input string with "\n"

# ~~~Welcome to In-N-Out~~~
# We'd like to take your order
# ~~ Shake Menu ~~~
#      V : Vanilla    ($3)
#      C : Chocolate  ($3)
#      S : Strawberry ($3)
#      N : Neapolitan ($5)
# Please make a selection from the above:
# ~~ Fries Menu ~~~
#      A : Animal Fries ($4)
#      C : Cheese Fries ($3)
#      F : French Fries ($2)
# Please make a selection from the above:

print("~~~Welcome to In-N-Out~~~")
print("We'd like to take your order\n")

shake_menu = {
   'V': {
       'cost': 3,
       'name': 'Vanilla Shake',
   },
   'C': {
       'cost': 3,
       "name": "Chocolate Shake",
   },
   'S': {
       'cost': 3,
       "name": "Strawberry Shake",
   },
   'N': {
       'cost': 5,
       "name": "Neapolitan Shake",
   },
}

fry_menu = {
   'A': {
       'cost': 4,
       "name": "Animal Fries",
   },
   'C': {
       'cost': 3,
       "name": "Cheese Fries",
   },
   'F': {
       'cost': 2,
       "name": "French Fries",
   },
}

shake = input("Would you like a shake? Y/N\n")
output = []
fry_price = 0
shake_price = 0
shakeValid = False
fryValid = False
if shake.upper() == 'Y':
   print("~~ Shake Menu ~~~")
   print("     V : Vanilla    ($3)")
   print("     C : Chocolate  ($3)")
   print("     S : Strawberry ($3)")
   print("     N : Neapolitan ($5)")
   shake_choice = input('Please make a selection from the above:\n')
   if shake_choice.upper() in shake_menu:
       output.append(shake_menu[shake_choice.upper()]['name'])
       shake_price = shake_menu[shake_choice.upper()]['cost']
       shakeValid = True
   else:
       print(f"{shake_choice}: Invalid selection")

fries = input("Would you like fries? Y/N\n")
if fries.upper() == 'Y':
   print("~~ Fries Menu ~~~")
   print("     A : Animal Fries ($4)")
   print("     C : Cheese Fries ($3)")
   print("     F : French Fries ($2)")
   fry_choice = input('Please make a selection from the above:\n')
   if fry_choice.upper() in fry_menu:
       output.append(fry_menu[fry_choice.upper()]['name'])
       fry_price = fry_menu[fry_choice.upper()]['cost']
       fryValid = True
   else:
       print(f"{fry_choice}: Invalid selection")

totalCost = fry_price + shake_price
print("~~~Order Summary~~~")
if shake.upper() == 'N' and fries.upper() == 'N':
   print("Not Hungry? That's OK... Have a nice day!")
else:
   if totalCost == 0:
       print("Not Hungry? That's OK... Have a nice day!")
   else:
       if shake.upper() == 'Y' and fries.upper() == 'Y' and shakeValid is True and fryValid is True:
           print(f"{shake_menu[shake_choice.upper()]['name']}, and {fry_menu[fry_choice.upper()]['name']}")
       else:
           print(f"{' '.join(output)}")
       print(f"Your total is: ${totalCost}")
       
           