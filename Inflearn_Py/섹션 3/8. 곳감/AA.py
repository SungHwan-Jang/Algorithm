# import sys
#
# sys.stdin = open('test.txt', 'rt')

import copy

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

cmd_cnt = int(input())
cmd_matrix = [list(map(int, input().split())) for _ in range(cmd_cnt)]

for i in range(cmd_cnt):
    row, cmd, rot = map(int, cmd_matrix[i])
    row -= 1

    if cmd == 0:  # left rot
        # move = n % rot
        tmp_matrix = copy.deepcopy(matrix)
        for i in range(n):
            matrix[row][(i - rot) % n] = tmp_matrix[row][i]
        del tmp_matrix
    else:  # right rot
        tmp_matrix = copy.deepcopy(matrix)
        for i in range(n):
            matrix[row][(i + rot) % n] = tmp_matrix[row][i]
        del tmp_matrix

stx = 0
etx = n
res = 0

for i in range(n):
    for j in range(stx, etx):
        res += matrix[i][j]

    if i >= (n // 2):
        stx -= 1
        etx += 1
    else:
        stx += 1
        etx -= 1

print(res)
