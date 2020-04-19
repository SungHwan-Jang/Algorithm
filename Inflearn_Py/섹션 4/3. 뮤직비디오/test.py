import sys

sys.stdin = open('test.txt', 'rt')

song_cnt, dvd_cnt = map(int, input().split())
samples = list(map(int, input().split()))


def check_in(samples, mid, cnt):
    idx = 0

    for i in range(cnt):
        sum_samples = 0

        if i == 0:
            idx = -1

        for j in range(idx + 1, len(samples)):
            sum_samples += samples[j]

            if sum_samples > mid:
                idx = j - 1
                sum_samples = 0
                break
            elif sum_samples == mid:
                idx = j
                sum_samples = 0
                if i == cnt - 1 and j == len(samples) - 1:
                    return True
                break
            elif i == cnt - 1 and j == len(samples) - 1:
                return True

    if idx < len(samples) - 1:
        return False
    else:
        return True


print(check_in(samples, 9, 9))

lpt = 1
rpt = sum(samples)
res = 2742000000

while lpt <= rpt:
    mid = (lpt + rpt) // 2
    i = 0

    if check_in(samples, mid, dvd_cnt):
        if mid < res:
            res = mid

        rpt = mid - 1
    else:
        lpt = mid + 1

print(res)

# lpt = sum(samples) // dvd_cnt

# while True:
#     dvds = [0] * (dvd_cnt)
#     sum_song_length = 0
#
#     for repeat in range(dvd_cnt):
#         sum_song_length = 0
#
#         if repeat == 0:
#             stx = 0
#         else:
#             stx = dvds[repeat - 1]
#
#         for i in range(stx + 1, song_cnt, 1):
#             if sum_song_length > lpt:
#                 dvds[repeat] = i - 2
#                 break
#             elif sum_song_length == lpt:
#                 dvds[repeat] = i - 1
#                 break
#             elif i == song_cnt - 1:
#                 dvds[repeat] = i
#                 break
#             else:
#                 sum_song_length += samples[i]
#
#     if dvds[3] == song_cnt - 1:
#         check = 0
#         for val in dvds:
#             check += samples[val]
#
#         if check == sum(samples):
#             break
#         else:
#             lpt += 1
#
#     else:
#         lpt += 1
#
# print(dvds)
# print(lpt)
