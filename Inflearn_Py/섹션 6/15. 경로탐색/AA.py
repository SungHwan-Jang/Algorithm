# import sys
#
# sys.stdin = open("in4.txt", "r")


def dfs(level, start):  # 0 1
    global cnt

    if level == N:
        return

    for target in range(1, N + 1):
        if mapping[start][target] == 1:
            if target == N:
                cnt += 1
                return
            else:
                if path[target] == 0:
                    path[target] = 1
                    dfs(level + 1, target)
                    path[target] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())

    mapping = [[0] * (N + 1) for _ in range(N + 1)]
    path = [0] * (N + 1)
    path[1] = 1
    cnt = 0

    for i in range(M):
        stx, etx = map(int, input().split())
        mapping[stx][etx] = 1

    dfs(0, 1)

    print(cnt)
