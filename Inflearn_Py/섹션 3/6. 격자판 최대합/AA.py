# import sys
#
# sys.stdin = open('in5.txt', 'rt')

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
tmp_sum_diagonal_forward = 0
tmp_sum_diagonal_reverse = 0

for i in range(n):
    tmp_sum_row = 0
    tmp_sum_col = 0

    tmp_sum_diagonal_forward += matrix[i][i]
    tmp_sum_diagonal_reverse += matrix[i][n - 1 - i]

    for j in range(n):
        tmp_sum_row += matrix[i][j]
        tmp_sum_col += matrix[j][i]

    if max_sum < tmp_sum_row:
        max_sum = tmp_sum_row

    if max_sum < tmp_sum_col:
        max_sum = tmp_sum_col

    if max_sum < tmp_sum_diagonal_forward:
        max_sum = tmp_sum_diagonal_forward

    if max_sum < tmp_sum_diagonal_reverse:
        max_sum = tmp_sum_diagonal_reverse


print(max_sum)
