# import sys
#
# sys.stdin = open('test.txt', 'rt')
N = int(input())
reverse_seq = list(map(int, input().split()))

# print('rev:', reverse_seq)
# [5, 3, 4, 0, 2, 1, 1, 0]
# 4 8 6 2 5 1 3 7

res = [0] * N

for i in range(N):
    cnt = 0
    for j in range(0, N):

        if reverse_seq[i] == 0:
            for k in range(0, N):
                if res[k] == 0:
                    res[k] = i + 1
                    break
            break

        if res[j] == 0:
            cnt += 1
            if cnt == reverse_seq[i]:
                for k in range(j + 1, N):
                    if res[k] == 0:
                        res[k] = i + 1
                        break
                break

for val in res:
    print(val, end=' ')
