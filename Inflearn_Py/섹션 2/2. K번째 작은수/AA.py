import sys

test_case = int(input())

for i in range(1, test_case+1):
    n, s, e, k = map(int, input().split())
    raw_data = list(map(int, input().split()))

    parsing_raw_data = raw_data[s - 1:e]
    parsing_raw_data.sort()

    print('#{}'.format(i), parsing_raw_data[k-1])
