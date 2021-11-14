import sys
def collatz(number):
    if number % 2 == 0:
        # Even number
        ret = number // 2
    elif number % 2 == 1:
        # Odd number
        ret = 3 * number + 1
    print(ret)
    return ret

print('Enter the number:')
try:
    number = int(input())
    res = collatz(number)
    while res != 1:
        res = collatz(res)
except ValueError:
    print('Must enter an integer number')
