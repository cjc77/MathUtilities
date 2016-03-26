#! usr/bin/python3

import math, sys

def find_sqrt(num):
    """Find Perfect squares num is divisible by."""
    global squares, sqr_times_what
    squares = (x ** 2 for x in range(1, num) if num % (x * x) == 0)
    sqr_times_what = (num / x for x in squares)
    print_squares(squares)

def print_squares(ls):
    """Print in readable way res of find_sqrt."""
    num_squares = 0
    for num in squares:
        print('Square: ', num, '------', 'Square Root:',
              int(math.sqrt(num)))
        print(num, '*', int(inp_num / num), '=', inp_num)
        num_squares += 1
    print('Div by', num_squares, 'perfect squares')

def find():
    global inp_num
    inp_num = int(sys.stdin.readline())
    find_sqrt(inp_num)

if __name__ == "__main__":
    find()
