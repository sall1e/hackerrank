"""
Luke is daydreaming in Math class. He has a sheet of graph paper with  rows and  columns, and he imagines that there is an army base in each cell for a total of  bases. He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot. If a base contains at least one package inside or on top of its border fence, then it's considered to be supplied. For example:

image

Given  and , what's the minimum number of packages that Luke must drop to supply all of his bases?

Example


Packages can be dropped at the corner between cells (0, 0), (0, 1), (1, 0) and (1, 1) to supply  bases. Another package can be dropped at a border between (0, 2) and (1, 2). This supplies all bases using  packages.

Function Description

Complete the gameWithCells function in the editor below.

gameWithCells has the following parameters:

int n: the number of rows in the game
int m: the number of columns in the game
Returns

int: the minimum number of packages required
"""


def gameWithCells(n: int, m: int):
    n_squares = (n // 2) * (m // 2)
    n_lines = (((n % 2) * m // 2) + ((m % 2) * n // 2))
    n_dots = (n % 2) * (m % 2)
    return n_squares + n_lines + n_dots


if __name__ == '__main__':
    n, m = 10, 10
    print('Answer: ', gameWithCells(n, m))
