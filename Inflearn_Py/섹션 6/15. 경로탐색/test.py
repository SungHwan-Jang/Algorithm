import sys

sys.stdin = open("in4.txt", "r")


def dfs(level, start):  # 0 1
    global cnt

    if level == N:
        return

    for target in range(1, N + 1):
        if mapping[start][target] == 1:
            if target == N:
                cnt += 1
                print(start, target)
                print("end!")
                return
            else:
                if path[target] == 0:
                    path[target] = 1
                    print(start, target)
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

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(mapping[i][j], end=" ")
        print()

    dfs(0, 1)

    print(cnt)
