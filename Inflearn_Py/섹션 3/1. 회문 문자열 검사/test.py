import sys

sys.stdin = open('test.txt', 'rt')

n = int(input())

for idx in range(n):
    test_case = list(input().lower())
    # print(test_case)
    res = True
    for i in range(len(test_case) // 2):
        if test_case[i] == test_case[len(test_case) - 1 - i]:
            continue
        else:
            res = False

    if res == True:
        print('#{} {}'.format(idx + 1, 'YES'))
    else:
        print('#{} {}'.format(idx + 1, 'NO'))
