import sys

sys.stdin = open('in2.txt', 'rt')

xi_cnt, horse_cnt = map(int, input().split())

xi_list = []

for _ in range(xi_cnt):
    xi_list.append(int(input()))
xi_list.sort()

print(xi_list)

lpt = 0
rpt = len(xi_list) - 1


def find_max_mid(lpt, rpt, xi_lists):
    diffrence_l_r = 2740000000
    tmp_lpt = lpt
    tmp_rpt = rpt
    center = 0

    while tmp_lpt <= tmp_rpt:
        mid = (tmp_lpt + tmp_rpt) // 2
        diff_l = xi_list[mid] - xi_list[lpt]
        diff_r = xi_list[rpt] - xi_list[mid]
        diff = abs(diff_l - diff_r)

        if diff_l > diff_r:
            if diffrence_l_r > diff:
                diffrence_l_r = diff
                center = mid
            tmp_rpt = mid - 1
        else:
            if diffrence_l_r > diff:
                diffrence_l_r = diff
                center = mid
            tmp_lpt = mid + 1

    return center


# print(find_max_mid(lpt, rpt, xi_list))

check_list = [0] * len(xi_list)
check_list[lpt] = 1
check_list[rpt] = 1
check_list[find_max_mid(lpt, rpt, xi_list)] = 1

print(check_list)

for _ in range(horse_cnt - 3):
    diff = 0
    idx = 0
    ptr = idx + 1

    stx = 0
    etx = 0
    res = 0

    for i in range(ptr, len(check_list)):
        if check_list[i] == 1:
            tmp = xi_list[i] - xi_list[idx]
            if tmp > diff:
                diff = tmp
                stx = idx
                etx = i

            idx = i
            ptr = idx + 1

    mid = find_max_mid(stx, etx, xi_list)
    check_list[mid] = 1

print(check_list)
print(stx, mid, etx)

if xi_list[mid] - xi_list[stx] < xi_list[etx] - xi_list[mid]:
    print(xi_list[mid] - xi_list[stx])
else:
    print(xi_list[etx] - xi_list[mid])
