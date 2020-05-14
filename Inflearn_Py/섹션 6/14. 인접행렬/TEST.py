import sys

sys.stdin = open("test.txt", "r")

if __name__ == '__main__':
    pass
# 무방향 그래프 예제 (2차원 리스트 즉, 배열로 맵을 만든다.)
# (1) = (2)
# ||    ||
# (3) = (4) = (5) 의 경우
# 모두 0 초기화
# mapping[1][2] = 1 (1은 2로 갈 수 있으므로)
# mapping[2][1] = 1 등으로 맵을 만든다.
n, m = map(int, input().split())

mapping = [[0] * (n + 1) for _ in range(n + 1)]

# 가중치 그래프, weight 값을 1 대신에 넣어준다.
for i in range(m):
    st, end, weight = map(int, input().split())
    mapping[st][end] = weight

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(mapping[i][j], end=' ')
    print()
