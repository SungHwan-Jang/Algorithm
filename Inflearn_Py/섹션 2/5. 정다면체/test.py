import sys

sys.stdin = open("test.txt", 'rt')

n, m = map(int, input().split())
print(n, m)

sum_array = []

for n_val in range(1, n + 1):
    print(n_val)
    for m_val in range(1, m + 1):
        sum_array.append(n_val + m_val)

sum_count_array = []
for idx in range(2, n + m + 1):
    sum_count_array.append(sum_array.count(idx))

print(sum_count_array)

for idx, cnt in enumerate(sum_count_array):
    if cnt == max(sum_count_array):
        print(idx + 2, end=' ')
