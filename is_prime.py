#write a python program that keeps prompting the user for positive intergers OR a -ve int to quit!
#Your program should determine if a number is prime or not!           

while True:
    number = int(input("Enter number (- to quit): \n"))
    if number < 0:
        break
    isprime = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                isprime = False
    else:
        isprime = False
    if isprime:
        print("Number is Prime")
    else:
        print("Number is not Prime")
