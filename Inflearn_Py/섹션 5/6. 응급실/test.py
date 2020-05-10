import sys
from collections import deque

sys.stdin = open("test.txt", "rt")

N, M = map(int, input().split())
samples = list(map(int, input().split()))
samples = deque(samples)
# 해당 samples를 enumerate 형식으로 순번, 데이터 같이 받아서 순번으로 중복처리를 가능케 하면된다.
print(samples)
cnt = 0
vip_patient = samples[M]
queue = []
flag = False

while True:
    patient = samples.popleft()

    if patient > max(samples):
        cnt += 1

        if vip_patient == patient:
            print(cnt)
            break

    elif patient == max(samples):
        if len(samples) == 1:
            print(cnt + 1)
            break

        if flag == False:
            samples.append(patient)
            flag = True
        else:
            cnt += 1

    else:
        samples.append(patient)
