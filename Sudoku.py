from typing import List
from copy import deepcopy


class Sudoku:
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.origin = deepcopy(board)
        self.rowSets = [set() for _ in range(9)]
        self.colSets = [set() for _ in range(9)]
        self.squareSets = [[set() for _ in range(3)] for _ in range(3)]
        if not self.init():
            print("This is not a valid Sudoku Question")

    def init(self) -> bool:
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                num = self.board[row][col]
                if num != 0:
                    if num in self.rowSets[row] or num in self.colSets[col] \
                            or num in self.squareSets[row // 3][col // 3]:
                        return False
                    else:
                        self.rowSets[row].add(num)
                        self.colSets[col].add(num)
                        self.squareSets[row // 3][col // 3].add(num)
        return True

    def printBoard(self) -> None:
        """
        prints self.answer in a pretty way
        """
        for row in range(9):
            for col in range(9):
                if col != 8:
                    print(self.board[row][col], end=" ")
                else:
                    print(self.board[row][col])
                if col == 2 or col == 5:
                    print("|", end=" ")
            if row == 2 or row == 5:
                print("- " * 11)

    def solve(self, r=0, c=0) -> bool:
        row, col = self.findNextEmpty(r, c)
        if (row, col) == (-1, -1):  # Base Case, all block filled, return True
            return True
        for i in range(1, 10):
            if self.valid(row, col, i):
                self.board[row][col] = i
                self.rowSets[row].add(i)
                self.colSets[col].add(i)
                self.squareSets[row // 3][col // 3].add(i)
                if self.solve(row, col):
                    return True
                self.rowSets[row].remove(i)
                self.colSets[col].remove(i)
                self.squareSets[row // 3][col // 3].remove(i)
        self.board[row][col] = 0

        return False  # Unable to solve the Sudoku

    def findNextEmpty(self, r: int, c: int) -> (int, int):
        """
        :param r: row of previous empty box
        :param c: col of previous empty box
        :return (int, int): (row ,col) of the next empty box
        """
        for col in range(c + 1, 9):
            if self.board[r][col] == 0:
                return r, col
        for row in range(r + 1, 9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return -1, -1

    def valid(self, row, col, val) -> bool:
        if val in self.rowSets[row] or val in self.colSets[col] or val in self.squareSets[row // 3][col // 3]:
            return False
        return True


if __name__ == '__main__':
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    su = Sudoku(board)
    su.printBoard()
    su.solve()
    print(" ")
    su.printBoard()
