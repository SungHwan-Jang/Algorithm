import sys

sys.stdin = open('in2.txt', 'rt')

n, k = map(int, input().split())
print(n, k)

samples = list(map(int, input().split()))
print(samples)

res = []

for i in range(n):
    for j in range(i + 1, n):
        for z in range(j + 1, n):
            res.append(samples[i] + samples[j] + samples[z])

res = set(res)
res = list(res)
res.sort()
print(res)
print(res[len(res) - k])
