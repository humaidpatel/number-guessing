import random

range = input('Enter the the range of whole numbers for random number generation:')
x = random.randint(1,int(range))


while True:
    y = input('Guess your number from 1 to {} : (Enter e to exit)'.format(range))
    try:
        num = int(y)
    except ValueError:
        if y=='e':
            print('Quit succesfully')
            break
        else:
            print('Please enter a valid input')
            continue
    if num<1 or num>int(range):
        print('The number is not in range')
        continue
    if num==x:
        print('Your guess is correct')
        break
    elif num<x:
        print('Guess a bigger number')
        continue
    else:
        print('Guess a smaller number')
        continue
