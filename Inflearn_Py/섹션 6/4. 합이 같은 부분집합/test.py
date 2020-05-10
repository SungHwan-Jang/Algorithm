import sys

sys.stdin = open("test.txt", "rt")

N = int(input())
samples = list(map(int, input().split()))


def dfs(x):
    global res

    if x == N:
        sum1 = 0
        sum2 = 0
        for i, val in enumerate(index_info):
            if val == 1:
                sum1 += samples[i]
            else:
                sum2 += samples[i]

        if sum1 == sum2:
            res = True
        else:
            pass
        return
    else:
        index_info[x] = 1
        dfs(x + 1)
        index_info[x] = 0
        dfs(x + 1)


if __name__ == '__main__':
    index_info = [0] * N
    res = False
    dfs(0)
    if res == True:
        print("YES")
    else:
        print("NO")
