n = int(input())
sample1 = list(map(int, input().split()))
m = int(input())
sample2 = list(map(int, input().split()))

# quicksort -> O(nlog(n))
# sample1.extend(sample2)
# sample1.sort()
# print(sample1)

# 정렬이 이미 되어있는것을 활용하면, O(n)으로 quicksort보다 훨씬 빠르다.

p1 = 0
p2 = 0
res = []

for _ in range(n + m):
    if sample1[p1] < sample2[p2]:
        res.append(sample1[p1])
        p1 += 1

        if p1 > n - 1:
            res.extend(sample2[p2:len(sample2)])
            break

    else:
        res.append(sample2[p2])
        p2 += 1

        if p2 > m - 1:
            res.extend(sample1[p1:len(sample1)])
            break

for val in res:
    print(val, end=' ')