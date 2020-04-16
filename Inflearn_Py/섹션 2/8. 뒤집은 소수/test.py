import sys

sys.stdin = open('test.txt', 'rt')

n = int(input())
samples = list(map(int, input().split()))


# print(n, samples)

def isPrime(x):
    cnt = 0
    for i in range(2, x):
        if x % i == 0:
            cnt += 1

    if cnt != 2:
        return False
    else:
        return True


def reverse(x):
    str_x = str(x)
    tmp = []
    for i in range(len(str_x) // 2):
        tmp = str_x[len(tmp) - 1 - i]
        str_x[len(tmp) - 1 - i] = str_x[i]
        str_x[i] = tmp

    return int(str_x)


for i in range(n):
    sample = reverse(samples[i])
    if isPrime(sample) == True:
        print(sample, end=' ')
