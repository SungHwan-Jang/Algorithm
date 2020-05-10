import sys
from collections import deque

N, M = map(int, input().split())
samples = list(map(int, input().split()))
samples = deque(samples)
# print(samples)
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
