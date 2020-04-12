import sys

sys.stdin = open("in1.txt", "rt")
test_case = int(input())

for i in range(1, test_case+1):
    n, s, e, k = map(int, input().split(" "))
    raw_data = list(map(int, input().split(" ")))

    print(n, s, e, k, raw_data)
    parsing_raw_data = raw_data[s - 1:e]
    print(parsing_raw_data)
    parsing_raw_data.sort()

    print('#{}'.format(i), parsing_raw_data[k-1])

