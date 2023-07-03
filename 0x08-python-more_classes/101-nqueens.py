#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or board[i]-i == col - row or board[i]+i == col+row:
            return False
    return True


def solve_nqueens(n):
    def backtrack(board, row):
        if row == n:
            # Found a solution, add it to the result
            result.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    # Validate input
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the problem
    board = [-1] * n
    result = []
    backtrack(board, 0)

    # Print the solutions
    for solution in result:
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    solve_nqueens(0)
