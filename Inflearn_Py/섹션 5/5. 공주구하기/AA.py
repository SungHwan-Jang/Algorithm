import sys
from collections import deque

N, K = map(int, input().split())
queue = list(i for i in range(1, N + 1))
queue = deque(queue)
cnt = 0
while True:
    cnt += 1

    if cnt == K:
        queue.popleft()
        cnt = 0

        if len(queue) == 1:
            break
    else:
        tmp = queue.popleft()
        queue.append(tmp)

print(queue.pop())
