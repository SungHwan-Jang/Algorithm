import sys

sys.stdin = open('test.txt', 'rt')

n = 7
matrix = [list(map(int, input().split())) for _ in range(7)]
ptr = [2, 3, 4]
