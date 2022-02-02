import numpy as np


def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0


def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0


def checkWin(board):
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


a = [['X', 'A', 'X'],
     ['X', 'A', 'X'],
     ['A', 'X', 'A']]

print(checkWin(a))
