import sys

sys.stdin = open("test.txt", 'rt')

count = int(input())
samples = list(map(str, input().split()))

# print(count)
# print(samples)

digit_max = 0
idx = 0


def digit_sum(x):
    sum = 0
    for i in range(len(x) - 1, -1, -1):
        sum += int(x) // (10 ** i)
        x = int(x) % (10 ** i)
    return sum


for i in range(count):
    digit_max_tmp = digit_sum(samples[i])
    if digit_max_tmp > digit_max:
        digit_max = digit_max_tmp
        idx = i

print(samples[idx])
