import sys

sys.stdin = open('in2.txt', 'rt')

n, m = map(int, input().split())
samples = list(map(int, input().split()))

# def sort_ascending(data_list):
#     for i in range(len(data_list)):
#         for j in range(i, len(data_list)):
#             if data_list[i] > data_list[j]:
#                 tmp = data_list[j]
#                 data_list[j] = data_list[i]
#                 data_list[i] = tmp
#
# sort_ascending(samples)

samples.sort()

print(samples)


def find_value_ret_idx(data_list, m):
    stx = 0
    end = len(data_list) - 1
    mid = (end - stx) // 2

    while True:
        if m > data_list[mid]:
            stx = mid + 1
            mid = (end + stx) // 2
        elif m == data_list[mid]:
            return mid + 1
        else:
            end = mid - 1
            mid = (end + stx) // 2


print(find_value_ret_idx(samples, m))
