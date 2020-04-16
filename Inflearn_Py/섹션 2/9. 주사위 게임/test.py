import sys

sys.stdin = open('test.txt', 'rt')

n = int(input())
mapping = [0] * 7
max_data = 0

for i in range(n):
    dice_samples = list(map(int, input().split()))
    for val in dice_samples:
        mapping[val] += 1

    overlap_num = max(mapping)
    res = 0

    if overlap_num == 1:
        for idx, val in enumerate(mapping):
            if val == 1:
                res = idx * 100
    elif overlap_num == 2:
        res = 1000 + mapping.index(2) * 100
    elif overlap_num == 3:
        res = 10000 + mapping.index(3) * 1000
    else:
        raise RuntimeError

    if max_data < res:
        max_data = res

    mapping = [0] * 7


print(max_data)
