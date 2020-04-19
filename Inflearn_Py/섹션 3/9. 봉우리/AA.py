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
        judge = True
        myself = matrix[i][j]

        for k in range(-1, 2, 2):
            if myself <= matrix[i + k][j] or myself <= matrix[i][j + k]:
                judge = False

        if judge == True:
            peaks_count += 1

print(peaks_count)
