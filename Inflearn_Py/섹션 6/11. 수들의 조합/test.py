import sys

sys.stdin = open("in4.txt", "r")


def dfs(level, st):
    global cnt

    if level == K:
        # print(combiantion)
        if sum(combiantion) % M == 0:
            cnt += 1
        return

    for i in range(st, len(samples)):
        combiantion[level] = samples[i]
        dfs(level + 1, i + 1)


if __name__ == '__main__':
    N, K = map(int, input().split())
    samples = list(map(int, input().split()))
    M = int(input())
    cnt = 0

    combiantion = [0] * K
    dfs(0, 0)

    print(cnt)

# 5 3
# 2 4 5 8 12
# 6
