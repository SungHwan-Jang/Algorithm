import sys

sys.stdin = open('test.txt', 'rt')

n = int(input())
samples = []
for _ in range(n):
    samples.append(list(map(int, input().split())))

samples.sort()
# print(samples)

ref = samples[0][0]
st = 0
for i in range(1, len(samples)):
    if ref >= samples[i][0]:
      st = i
      break

for _ in range(st + 1):
    samples.pop(0)

samples.sort(key= lambda x: [x[1], x[0]])
# print(samples)

ref = samples[0][1]
st = 0
for i in range(1, len(samples)):
    if ref >= samples[i][1]:
      st = i
      break

for _ in range(st + 1):
    samples.pop(0)

print(len(samples))
