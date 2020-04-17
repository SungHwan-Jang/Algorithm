import sys

sys.stdin = open('test.txt', 'rt')

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
sum = 0
# print(matrix)

for i in range(n):
    center = n // 2  # fixed 2
    deviation = abs(center - i)  # 1
    count = n - (deviation * 2)  # root = 3
    rt = count // 2  # 3 - 2 = 1
    lt = -1 * (count // 2)  # 2 - 3 = -1

    sum += matrix[i][center]

    for r in range(center + 1, center + rt + 1, 1):
        sum += matrix[i][r]
    for l in range(center - 1, center + lt - 1, -1):
        sum += matrix[i][l]

print(sum)
# 13
