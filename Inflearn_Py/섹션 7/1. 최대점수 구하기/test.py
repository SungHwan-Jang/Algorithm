import sys

sys.stdin = open("test.txt", "r")


def dfs(level, st, current_score):
    global time
    global score

    if level == N:
        print("end!")
        return

    for i in range(st, N):
        time += samples[i][1]

        if time > M:
            print("over!")
            time -= samples[i][1]
            continue
        else:
            print("add !",samples[i][0], samples[i][1])
            current_score += samples[i][0]
            if current_score > score:
                print("change! score!")
                score = current_score

            dfs(level+1, i+1, current_score)
            print("delete !", samples[i][0], samples[i][1])
            time -= samples[i][1]
            current_score -= samples[i][0]


if __name__ == '__main__':
    N, M = map(int, input().split())
    samples = []
    ch = [0] * (N)
    score = 0
    time = 0

    for _ in range(N):
        samples.append(tuple(map(int, input().split())))

    samples.sort(reverse=True)
    dfs(0, 0, 0)
    print(score)

    # no relate sequence - combination
    # prevent stack overflow - cut off edge (remain find)
    # for fast catch - quick sort samples
