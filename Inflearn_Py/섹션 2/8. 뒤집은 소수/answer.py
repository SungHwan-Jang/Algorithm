import sys

sys.stdin = open('in1.txt', 'rt')

n = int(input())
samples = list(map(int, input().split()))


# print(n, samples)

def isPrime(x):
    cnt = 1
    for i in range(2, x + 1):
        if x % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False


def reverse(x):
    res = 0

    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10

    return res


for i in range(n):
    sample = reverse(samples[i])
    if isPrime(sample) == True:
        print(sample, end=' ')
