import sys

sys.stdin = open('test.txt', 'rt')

L = int(input())
samples = list(map(int, input().split()))
M = int(input())
samples.sort(reverse=True)

for _ in range(M):
    samples[0] -= 1
    samples[len(samples) - 1] += 1
    samples.sort(reverse=True)

print(samples[0] - samples[len(samples) - 1])
