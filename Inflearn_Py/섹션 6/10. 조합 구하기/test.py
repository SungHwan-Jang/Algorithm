import sys

sys.stdin = open("in1.txt", "r")


def combination_dfs(level, st):
    global cnt

    if level == M:
        cnt += 1
        print(res)
        return

    for i in range(st, N + 1):
        res[level] = i
        combination_dfs(level + 1, i + 1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    cnt = 0
    ch = [0] * (N + 1)
    res = [0] * M
    combination_dfs(0, 1)
    print(cnt)

# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# 6
