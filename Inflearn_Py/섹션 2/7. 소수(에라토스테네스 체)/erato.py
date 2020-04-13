import sys
import time

sys.stdin = open('test.txt', 'rt')

num = int(input())

st = time.time()


def find_prime_number_count(x):
    num_lists = list(range(2, x + 1))
    manipulated_num_list = []

    while True:
        i = 0
        manipulated_num_list = []
        manipulated_num_list.append(num_lists[i])

        for j in range(i + 1, len(num_lists)):
            if num_lists[j] % num_lists[i] == 0:
                continue
            else:
                manipulated_num_list.append(num_lists[j])

        num_lists = manipulated_num_list.copy()
        del manipulated_num_list
        i += 1

        if i > x:
            break
    return


print(find_prime_number_count(num))
end_time = time.time() - st
print(end_time)
