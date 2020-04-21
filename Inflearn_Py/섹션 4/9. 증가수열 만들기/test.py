import sys

sys.stdin = open('in5.txt', 'rt')

N = int(input())
sequence = list(map(int, input().split()))
# print(sequence)
res = []
res_cnt = 0
tmp = 0

if sequence[0] < sequence[len(sequence) - 1]:
    tmp = sequence[0]
    sequence.pop(0)
    res.append('L')
    res_cnt += 1
elif sequence[0] > sequence[len(sequence) - 1]:
    tmp = sequence[len(sequence) - 1]
    sequence.pop()
    res.append('R')
    res_cnt += 1

while True:
    if sequence.__len__() == 1:
        if sequence[0] > tmp:
            sequence.pop(0)
            res.append('L')
            res_cnt += 1
            break
        else:
            break
    else:
        if sequence[0] > tmp and sequence[len(sequence) - 1] > tmp:
            if sequence[0] < sequence[len(sequence) - 1]:
                tmp = sequence[0]
                sequence.pop(0)
                res.append('L')
                res_cnt += 1
            elif sequence[len(sequence) - 1] < sequence[0]:
                tmp = sequence[len(sequence) - 1]
                sequence.pop()
                res.append('R')
                res_cnt += 1
        elif sequence[0] > tmp:
            tmp = sequence[0]
            sequence.pop(0)
            res.append('L')
            res_cnt += 1
        elif sequence[len(sequence) - 1] > tmp:
            tmp = sequence[len(sequence) - 1]
            sequence.pop()
            res.append('R')
            res_cnt += 1
        else:
            break

print(res_cnt)
for val in res:
    print(val, end='')
