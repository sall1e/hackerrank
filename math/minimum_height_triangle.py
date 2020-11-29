"""
Given integers  and , find the smallest integer , such that there exists a triangle of height , base , having an area of at least .

image

Example


The minimum height  is . One example is a triangle formed at points (0, 0), (4, 0), (2, 3).

Function Description

Complete the lowestTriangle function in the editor below.

lowestTriangle has the following parameters:

int b: the base of the triangle
int a: the minimum area of the triangle
Returns

int: the minimum integer height to form a triangle with an area of at least
Input Format

There are two space-separated integers  and , on a single line.
"""

import math


def lowest_triangle(base, area):
    # area = (base * height) / 2
    return math.ceil(2 * area / base)


if __name__ == '__main__':
    print('Answer: ', lowest_triangle(17, 100))