import sys

sys.stdin = open('in3.txt', 'rt')

N, M = map(int, input().split())
# saver boat <= 2 people, <= M(kg)
people = list(map(int, input().split()))
res = 0
people.sort(reverse=True)
print(people)
while True:
    if people.__len__() > 1:
        tmp = people[0] + people[len(people) - 1]
    elif people.__len__() == 1:
        tmp = people[0]
        res += 1
        break
    else:
        break

    if tmp <= M:
        people.pop()
        people.pop(0)
        res += 1
    else:
        people.pop(0)
        res += 1

print(res)