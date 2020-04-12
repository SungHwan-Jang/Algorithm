import sys

sys.stdin = open('in1.txt', 'rt')


def get_average(samples):
    sum = 0
    aver = 0

    for val in samples:
        sum += val

    aver = sum / len(samples)
    return aver


n = int(input())
print(n)

samples = list(map(float, input().split()))
print(samples)

average = round(get_average(samples) + 0.5)
print('%s %d' % ('average : ', average))

res_val_list = []
res_key_list = []
ref_diff = 100.0

for i in range(n):
    diff = abs(samples[i] - average)
    if ref_diff > diff:
        del res_val_list
        del res_key_list
        res_val_list = []
        res_key_list = []
        res_val_list.append(samples[i])
        res_key_list.append(i)
        ref_diff = diff
    elif ref_diff == diff :
        res_val_list.append(samples[i])
        res_key_list.append(i)
    else:
        continue

if len(res_val_list) == 2:
    if res_val_list[0] >= res_val_list[1]:
        print(average, res_key_list[0] + 1)
    else:
        print(average, res_key_list[1] + 1)
elif len(res_val_list) > 2:
    print(average, res_key_list[0] + 1)
else:
    print(average, res_key_list[0] + 1)
