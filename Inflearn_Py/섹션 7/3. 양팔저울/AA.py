import sys


# sys.stdin = open("test.txt", "r")


def dfs(level, current_sum):
    if level == N:
        if current_sum > 0:
            res[current_sum] = 1
        return

    if current_sum > 0:
        res[current_sum] = 1

    dfs(level + 1, current_sum + samples[level])
    dfs(level + 1, current_sum - samples[level])
    dfs(level + 1, current_sum)


if __name__ == '__main__':
    N = int(input())
    samples = list(map(int, input().split()))
    samples.sort(reverse=True)
    sum_samples = sum(samples)
    res = [0] * (sum_samples + 1)
    res[0] = 1

    dfs(0, 0)

    print(res.count(0))
