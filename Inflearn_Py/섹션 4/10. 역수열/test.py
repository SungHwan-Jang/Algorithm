import sys

sys.stdin = open('test.txt', 'rt')
N = int(input())
reverse_seq = list(map(int, input().split()))

print('rev:', reverse_seq)
# [5, 3, 4, 0, 2, 1, 1, 0]
# 4 8 6 2 5 1 3 7

res = []
for _ in range(N):
    res.append(2740000000)

for i in range(N):
    ref = reverse_seq[i]  # 5
    cnt = 0

    for j in range(N):
        if res[j] > i + 1 and cnt != ref:  # max > 1
            cnt += 1

        if cnt == ref:  # cnt == 5
            if res[j + 1] > i + 1:
                res[j + 1] = i + 1
                break
            else:
                continue

print('res:', res)
