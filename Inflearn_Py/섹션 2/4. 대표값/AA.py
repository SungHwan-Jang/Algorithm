import sys

#sys.stdin = open('test.txt', 'rt')

n = int(input())

samples = list(map(float, input().split()))
average = round((sum(samples) / n) + 0.5)

min = 2147000

for idx, x in enumerate(samples):
    tmp = abs(x - average)

    if tmp < min:
        min = tmp
        score = x
        res = idx + 1

    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
    else:
        pass

print(average, res)
