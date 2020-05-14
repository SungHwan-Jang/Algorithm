import sys

sys.stdin = open("test.txt", "r")


def dfs(level, start, before):  # 0 1
    global cnt

    if level == 5:
        return

    for target in range(1, N + 1):
        if mapping[start][target] == 1 and target != before:
            if target == N:
                cnt += 1
                print(start, target)
                print("end!")
                return
            else:
                print(start, target)
                dfs(level + 1, target, start)


if __name__ == '__main__':
    N, M = map(int, input().split())

    mapping = [[0] * (N + 1) for _ in range(N + 1)]
    ch = [0] * (N + 1)
    cnt = 0

    for i in range(M):
        stx, etx = map(int, input().split())
        mapping[stx][etx] = 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(mapping[i][j], end=" ")
        print()

    dfs(0, 1, 0)

    print(cnt)
