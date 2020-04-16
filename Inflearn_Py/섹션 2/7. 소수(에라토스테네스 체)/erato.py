import sys
import time

sys.stdin = open('test.txt', 'rt')

num = int(input())

st = time.time()


def find_prime_number_count(x):
    num_lists = list(range(2, x + 1))
    i = 0

    while True:
        if i >= len(num_lists):
            break

        for j in range(i + 1, len(num_lists)):
            if num_lists[j] % num_lists[i] == 0:
                num_lists[j] = 1
            else:
                continue

        while 1 in num_lists:
            num_lists.remove(1)

        i += 1

    return len(num_lists)


print(find_prime_number_count(num))
end_time = time.time() - st
print(end_time)
