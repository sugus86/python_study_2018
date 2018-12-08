# -*- coding: utf-8 -*-
row = 7
column = 10
board = []
for i in range(0,row):
    board.append([])
    for j in range(0,column):
        board[i].append('')

board[0][0] = '┏'
board[0][column-1] = '┓'
board[row-1][0]= '┗'
board[row-1][column-1] = '┛'

for i in range(1,row-1):
    board[i][0] = '┣'

for i in range(1,row-1):
    board[i][column-1] = '┫'

for i in range(1,column-1):
    board[0][i] = '┳'

for i in range(1,column-1):
    board[row-1][i] = '┻'

for i in range(1,row-1):
    for j in range(1,column-1):
            board[i][j] = '╋'
print(' ', end=' ')
for i in range(0,column):
    print(i, end=' ')
print()
for i in range(0, row):
    print(i, end=' ')
    for j in range(0,column):
        print('\b'+board[i][j], end=' ')
    print()