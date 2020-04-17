import sys

sys.stdin = open('test.txt', 'rt')

n = int(input())
samples = [list(map(int, input().split())) for _ in range(n)]
matrix = []
peaks_count = 0

for i in range(n + 2):
    if i == 0:
        matrix.append([0 for _ in range(n + 2)])
    elif i == n + 1:
        matrix.append([0 for _ in range(n + 2)])
    else:
        tmp = [0]
        tmp.extend(samples[i - 1])
        tmp.append(0)
        matrix.append(tmp)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        myself = matrix[i][j]
        for k in range(-1, 1, 1):
            for z in range(-1, 1, 1):
                if k == 0 and z == 0:
                    continue
                
