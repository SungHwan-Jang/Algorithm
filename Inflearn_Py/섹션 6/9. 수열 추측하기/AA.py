# import sys
#
# sys.stdin = open("test.txt", "rt")


def pascal(level, data):
    if level == N - 1:
        return data[0]

    tmp = []

    for i in range(len(data) - 1):
        tmp.append(data[i] + data[i + 1])

    res = pascal(level + 1, tmp)
    return res


def dfs(level):
    global first_time

    if not first_time:
        return

    if level == N:
        if pascal(0, samples) == ANSWER:
            first_time = False
            for val in samples:
                print(val, end=' ')
            return
        else:
            pass

    for i in range(1, N + 1):
        if ch[i] == 0:
            ch[i] = 1
            samples[level] = i
            dfs(level + 1)
            ch[i] = 0


if __name__ == '__main__':
    N, ANSWER = map(int, input().split())
    ch = [0] * (N + 1)
    samples = [0] * N
    first_time = True
    dfs(0)
