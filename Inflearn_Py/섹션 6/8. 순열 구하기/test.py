import sys

sys.stdin = open("test.txt", "r")


def dfs(level):
    global cnt

    if level == M:
        for i in range(M):
            print(res[i], end=" ")
        print()
        cnt += 1
        return

    for i in range(1, N + 1):
        if keymap[i] == 0:
            keymap[i] = 1
            res[level] = i
            dfs(level + 1)
            keymap[i] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    keymap = [0] * (N + 1)
    res = [0] * (M)
    cnt = 0
    dfs(0)
    print(cnt)
