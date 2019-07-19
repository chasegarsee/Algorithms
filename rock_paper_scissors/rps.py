#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    elif n == 1:
        return [["rock"], ["paper"], ["scissors"]]
    else:
        result = []
        previous = rock_paper_scissors(n - 1)
        for play in previous:
            for choice in ["rock", "paper", "scissors"]:
                newPlay = play.copy()
                #print("PLAY COPY", newPlay)
                newPlay.append(choice)
                #print("CHOICE", newPlay)
                result.append(newPlay)
        return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
