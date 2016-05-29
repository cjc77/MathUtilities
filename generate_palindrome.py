#! usr/bin/env python3

"""
If num is not palindrome, generate palindrome.

if num not palindrome --->> num = num + reversed(num)
"""

import sys

def is_pal(num):
    """
    Test to see if num is a palindrome.

    If not, call new_num(num).
    """
    half1 = num[:len(num) // 2]
    half2 = num[::-1]
    half2 = half2[:len(half1)]
    if half1 == half2:
        print(str(num) + " is a palindrome.")
    else:
        new_num(num)

def new_num(num):
    """
    Set num equal to (num + reversed(num))

    call is_pal(num)
    """
    print("Generating...")
    num = int(num) + int(num[::-1])
    is_pal(str(num))

if __name__ == "__main__":
    num = sys.stdin.read().strip('\n')
    is_pal(num)
