import sys

sys.stdin = open('test.txt', 'rt')

sample = list(input())
to_decimal = []

for i in range(len(sample)):
    if sample[i].isdecimal() == True:
        to_decimal.append(sample[i])

res = int(''.join(to_decimal))
print(res)

cnt = 0

for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1

print(cnt)
