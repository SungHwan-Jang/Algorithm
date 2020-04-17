# import sys
#
# sys.stdin = open('test.txt', 'rt')

n, target = map(int, input().split())
# print(n, target)

samples = list(map(int, input().split()))
# print(samples)

stx = 0
etx = 1
tmp_sum = samples[stx]
res = 0
threshold_flag = False

while True:

    if tmp_sum < target:
        if threshold_flag == True:
            break
        tmp_sum += samples[etx]
        etx += 1

        if len(samples) - 1 < etx:
            if tmp_sum >= target:
                threshold_flag = True
                continue
            break

    elif tmp_sum == target:
        res += 1
        tmp_sum -= samples[stx]
        stx += 1
    else:
        tmp_sum -= samples[stx]
        stx += 1

print(res)
