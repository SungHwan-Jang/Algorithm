n = int(input())
samples = list(map(int, input().split()))

# print(n, samples)

sum = 0
weight = 0

for i in range(n):

    if samples[i] == 0:
        weight = 0
    else:
        weight += 1
        sum += weight

print(sum)
