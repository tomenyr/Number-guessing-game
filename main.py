import random

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


def guess_number():
    num1 = random.randint(1, 100)
    print(‘Welcome to number guessing game’)
    
    while True:
         n = input(' Enter a number from 1 to 100:')
         if is_valid(n) == False:
            print('How about entering an integer from 1 to 100?')
        else:
            n = int(n)
            break
    
    while n != num1:
        n = int(n)
        if n < num1:
            print(‘Your number is lower than the one you guessed, try again’)
            n = input()
        elif n > num1:
            print(‘Your number is higher than the number you guessed, try again’)
            n = input()
        else:
            print(‘You guessed it, congratulations!’)
            break

print(‘Thanks for playing the numerical guessing game. See you later!')

guess_number()
