import sys
from collections import deque

sys.stdin = open("test.txt", "rt")

MASTER = list(map(str, input()))
MASTER = deque(MASTER)
N = int(input())
print(MASTER)
samples = [list(map(str, input())) for _ in range(N)]
print(samples)

for sample in samples:
    ref = MASTER.copy()

    for lecture in sample:
        if len(ref) != 0 and lecture == ref[0]:
            ref.popleft()
            if len(ref) == 0:
                print('YES')
                break

    if len(ref) != 0:
        print("NO")