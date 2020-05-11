# import sys
#
# sys.stdin = open("test.txt", "rt")

def dfs(sum, count):
    global res_count

    if count >= res_count:
        return

    if sum > M:
        return

    if sum == M:
        if res_count > count:
            res_count = count
            if res_count == 8:
                pass
        return

    for val in coin_list:
        sum += val
        count += 1
        dfs(sum, count)


if __name__ == '__main__':
    N = int(input())  # the number of coin type
    coin_list = list(map(int, input().split()))  # list of coin type
    M = int(input())  # refund dat
    count = 0
    res_count = 217000000
    coin_list.sort(reverse=True)
    dfs(0, 0)
    print(res_count)
