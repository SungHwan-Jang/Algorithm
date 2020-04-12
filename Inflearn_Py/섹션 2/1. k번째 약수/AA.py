import sys

# sys.stdin = open("in1.txt", "rt")
n, k = map(int, input().split(' '))
# print(n, k)

lists = []

for i in range(n):  # range(1, n+1)
    if n % (i + 1) == 0:  # i
        lists.append(i + 1)  # i
    else:
        pass

try:
    res = lists[k - 1]
except:
    res = -1

print(res)
