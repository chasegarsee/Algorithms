#!/usr/bin/python

import sys


def eating_cookies(n, cache=None):
    cookie_count = 0  # base case is zero

    if n <= 1:
        return 1
    if n >= 3:  # eating 3 cookies at a time. this will tell us how many different ways we can eat the rest of the cookies
        cookie_count = cookie_count + eating_cookies(n - 3)
    if n >= 2:  # eating 2 cookies at a time.
        cookie_count = cookie_count + eating_cookies(n - 2)
    if n >= 1:  # eating only one cookie at a time.
        cookie_count = cookie_count + eating_cookies(n - 1)
    return cookie_count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
