import sys

N = int(input())


def recursive_make_de_to_bi(n):
    if n == 0:
        return
    else:
        dv = n // 2
        remain = n % 2
        recursive_make_de_to_bi(dv)
        print(remain, end="")


if __name__ == '__main__':
    recursive_make_de_to_bi(N)
