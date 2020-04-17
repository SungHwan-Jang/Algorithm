import sys

sys.stdin = open('in1.txt', 'rt')

n = 10
deck = [i + 1 for i in range(20)]


# print(deck)

def reverse_section(st, end, deck):  # index 기반 입력 가정시,
    length = end - st + 1
    for i in range(length // 2):
        tmp = deck[st + i]
        deck[st + i] = deck[end - i]
        deck[end - i] = tmp


for _sq in range(n):
    command = list(map(int, input().split()))
    reverse_section(command[0] - 1, command[1] - 1, deck)

for val in deck:
    print(val, end=' ')
