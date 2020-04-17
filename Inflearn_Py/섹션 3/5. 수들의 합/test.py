import sys

sys.stdin = open('in5.txt', 'rt')

n, target = map(int, input().split())
print(n, target)

samples = list(map(int, input().split()))
print(samples)

res = 0

for i in range(n):
    tmp = samples[i]
    if tmp == target:
        res += 1
        continue
    for j in range(i + 1, n, 1):
        tmp += samples[j]
        if tmp == target:
            res += 1
            break

print(res)
