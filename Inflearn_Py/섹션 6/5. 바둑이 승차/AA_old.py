# import sys
#
# sys.stdin = open("test.txt", "rt")

C, N = map(int, input().split())
samples = [int(input()) for _ in range(N)]


# print(samples)

def dfs(level):
    global res

    if level == N:
        sum = 0
        for i, val in enumerate(lev_info):
            if val == 1:
                sum += samples[i]

        if sum > C:
            return
        else:
            if sum > res:
                res = sum
            return

    lev_info[level] = 0
    dfs(level + 1)
    lev_info[level] = 1
    dfs(level + 1)


if __name__ == '__main__':
    res = 0
    lev_info = [0] * N

    dfs(0)
    print(res)
