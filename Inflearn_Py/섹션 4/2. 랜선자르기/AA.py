# import sys
#
# sys.stdin = open('test.txt', 'rt')

n, target = map(int, input().split())
samples = []
for _ in range(n):
    samples.append(int(input()))

max_length = 0
lpt = 0
rpt = max(samples) - 1
mid = (lpt + rpt) // 2

target_count = 0

while lpt < rpt:

    tmp = 0

    for i in range(n):
        tmp += samples[i] // mid

    if tmp >= target and mid > max_length:
        max_length = mid
        lpt = mid + 1
        mid = (lpt + rpt) // 2
    else:
        rpt = mid - 1
        mid = (lpt + rpt) // 2

print(max_length + 1)
