#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # sets Max to equal the price at index 1 minus the price at index 0
    max = prices[1] - prices[0]
    for i in range(1, len(prices)):  # iterate thru the lenth of the array
        j = 0
        while j < i:  # while j is less than i
            # if the iteration of i minus the iteration of j is greated that max
            if prices[i] - prices[j] > max:
                # max is assigned to the price of i munus j
                max = prices[i] - prices[j]
            j += 1  # increment

    return max


if __name__ == '__main__':
                # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
