# 이진탐색은 리스트의 원소들이 정렬되어 있어야만 사용할 수 있다.

# low = 0
# high = len(list) - 1
# mid = (low + high) / 2
# guess = list[mid]
#
# if guess < item:
#     low = mid + 1
#
import math


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while True:
        mid = (low + high) / 2
        mid = math.ceil(mid)

        if list[mid] > item:
            high = mid - 1
        elif list[mid] < item:
            low = mid + 1
        elif list[mid] == item:
            return list[mid]
        elif mid == high or mid == low:
            return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9))
