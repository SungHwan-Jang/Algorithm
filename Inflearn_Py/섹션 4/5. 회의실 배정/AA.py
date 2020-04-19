import sys
import operator
#
# sys.stdin = open('in5.txt', 'rt')

# 그리디 알고리즘
# 문제를 푸는데 가장 좋은것을 선택하면 됨 (정렬하여 차례로 선택하는 형태)
# 회의가 끝나는 시점을 기준으로 정렬해야 한다.

n = int(input())
samples = []

for _ in range(n):
    samples.append(list(map(int, input().split())))

# print(samples)


def sorting_times(lists):
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if lists[i][1] > lists[j][1]:
                tmp = lists[i]
                lists[i] = lists[j]
                lists[j] = tmp


# sorting_times(samples)

samples = sorted(samples, key=operator.itemgetter(1))
# print(samples)

ref_ptr = 0
cnt = 1

for i in range(len(samples)):
    if samples[ref_ptr][1] <= samples[i][0]:
        ref_ptr = i
        cnt += 1

print(cnt)