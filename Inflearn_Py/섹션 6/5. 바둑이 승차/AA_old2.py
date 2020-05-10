# import sys
#
# sys.stdin = open("test.txt", "rt")

C, N = map(int, input().split())
samples = [int(input()) for _ in range(N)]


# print(samples)

def dfs(level, sum):
    global result

    if sum > C:
        return
    else:
        if sum > result:
            result = sum

        if level == N:
            return

    dfs(level + 1, sum + samples[level])
    dfs(level + 1, sum)


if __name__ == '__main__':
    samples.sort(reverse=True)
    result = 0
    dfs(0, 0)

    print(result)
