import sys
import copy

sys.stdin = open('in4.txt', 'rt')

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

cmd_cnt = int(input())
cmd_matrix = [list(map(int, input().split())) for _ in range(cmd_cnt)]

for i in range(cmd_cnt):
    row, cmd, rot = map(int, cmd_matrix[i])
    row -= 1

    # if cmd == 0:  # left rot
    #     tmp = matrix[row][0:rot]
    #     matrix[row][0:len(matrix[row][rot:])] = matrix[row][rot:]
    #     matrix[row][len(matrix[row][rot:]):] = tmp
    # else:  # right rot
    #     tmp = matrix[row][-rot:]
    #     matrix[row][rot:] = matrix[row][0:len(matrix[row]) - rot]
    #     matrix[row][0:rot] = tmp

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

print(matrix)

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
