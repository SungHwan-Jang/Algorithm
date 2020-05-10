import sys

sys.stdin = open("test.txt", "rt")

C, N = map(int, input().split())
samples = [int(input()) for _ in range(N)]


# print(samples)

def dfs(level, sum, remain_sum):
    global result

    if sum + (total_sum - remain_sum) < result:
        return

    if sum > C:
        return
    else:
        if sum > result:
            result = sum

        if level == N:
            return

    dfs(level + 1, sum + samples[level], sum + samples[level])
    dfs(level + 1, sum, sum + samples[level])


if __name__ == '__main__':
    samples.sort(reverse=True)
    total_sum = sum(samples)
    result = 0
    dfs(0, 0, 0)

    print(result)
