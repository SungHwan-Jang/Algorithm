import sys
import time

sys.stdin = open('test.txt', 'rt')

num = int(input())

st = time.time()


def find_prime_number_count(x):
    prime_count = 0
    for dut in range(1, x + 1):
        cnt = 0
        for i in range(1, dut + 1):
            if dut % i == 0:
                cnt += 1
            else:
                continue

        if cnt == 2:
            prime_count += 1

    return prime_count


print(find_prime_number_count(num))
end_time = time.time() - st
print(end_time)
