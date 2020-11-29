"""
At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?

Example

There are  attendees, ,  and .  shakes hands with  and , and  shakes hands with . Now they have all shaken hands after  handshakes.

Function Description

Complete the handshakes function in the editor below.

handshakes has the following parameter:

int n: the number of attendees
Returns

int: the number of handshakes
Input Format
The first line contains the number of test cases .
Each of the following  lines contains an integer, .
"""

from functools import reduce


def handshakes(n: int):
    # if n > 1:
    #     return (n - 1) + handshakes(n - 1)
    # return 0
    return sum(range(n))


if __name__ == '__main__':
    n = 4
    print(f'the number of {n} persons is equal to: {handshakes(n)}')




