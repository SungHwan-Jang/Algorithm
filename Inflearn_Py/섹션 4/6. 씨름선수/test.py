import sys

sys.stdin = open('in5.txt', 'rt')

n = int(input())
samples = []
for _ in range(n):
    samples.append(list(map(int, input().split())))

samples.sort(reverse=True)

cnt = 1
ref = 0
for i, sample in enumerate(samples):
    if i == 0:
        continue

    flag = True
    ref = sample[1]

    for k in range(i - 1, -1, -1):
        if samples[k][1] > ref:
            flag = False

    if flag == True:
        cnt += 1

print(cnt)
