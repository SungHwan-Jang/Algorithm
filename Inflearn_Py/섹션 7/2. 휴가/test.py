import sys

sys.stdin = open("in1.txt", "r")


def dfs(level, st, current_money):
    global money

    if level == N:
        return

    if st >= N:
        return

    if current_money > money:
        money = current_money

    for i in range(st, N):
        next_data = consultant_sch[i][0]
        current_money += consultant_sch[i][1]

        if i + next_data > N:
            continue

        print("add", i, current_money)
        dfs(level + 1, i + next_data, current_money)
        current_money -= consultant_sch[i][1]
        print("delete", i, current_money)


if __name__ == '__main__':
    N = int(input())
    consultant_sch = []
    money = 0

    for _ in range(N):
        consultant_sch.append(tuple(map(int, input().split())))

    print(consultant_sch)

    dfs(0, 0, 0)
    print(money)
