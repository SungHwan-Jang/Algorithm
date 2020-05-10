# min-heap (heapq module) -> pop()맨 아래 레벨에서 오른쪽을 최상위 루트로 올린뒤에 자식중에 작은값과 자기자신을 재귀적으로 바꾼다.
# push() 자식과 비교 후 왼쪽부터 채워나간다.

import sys
import heapq as hq

sys.stdin = open("test.txt", "rt")
a = []

while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
