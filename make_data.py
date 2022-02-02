import time
import numpy as np
import pandas as pd
import random


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


data = pd.DataFrame(columns=list(range(1, 10)) + ['Ans'], dtype=int)

df = pd.DataFrame(data=[[0, 0, 0], [0, 0, 0], [0, 0, 0]])
field = np.array(df)
line = 0 # hello

while True:
    field = field.dot(0)
    steps = random.randint(1, 7)
    for step in range(steps + 1 * steps % 2):
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if field[x][y] == 0:
                break
        if step % 2 == 0:
            field[x][y] = 1
        else:
            field[x][y] = -1
    if checkWin(field) != 0:
        line -= 1
        continue
    print(field)
    ans = input('Ans: ')
    if ans == '':
        break
    ans = int(ans)
    data_line = {1: field[0][0], 2: field[0][1], 3: field[0][2], 4: field[1][0], 5: field[1][1], 6: field[1][2],
                 7: field[2][0], 8: field[2][1], 9: field[2][2], 'Ans': ans}
    print()
    data = data.append(data_line, ignore_index=True)
    line += 1

data.to_csv(f'tic-tac-toe_datasets/{time.strftime("%d.%m.%Y---%H-%M", time.localtime())}.csv', index=False)
print(data)
