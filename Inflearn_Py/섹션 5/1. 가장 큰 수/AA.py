sample, m = map(str, input().split())
sample = list(sample)
m = int(m)

for i in range(len(sample)):
    sample[i] = int(sample[i])

res = []
cnt = 0

res.append(sample[0])

for i in range(1, len(sample)):
    if cnt == m:
        res.append(sample[i])
        continue

    before = res.pop()
    if before < sample[i]:
        while True:
            try:
                if before < sample[i]:
                    cnt += 1

                    if cnt == m:
                        res.append(sample[i])
                        break

                    before = res.pop()
                    continue
                else:
                    res.append(before)
                    res.append(sample[i])
                    break
            except:
                res.append(sample[i])
                break
    else:
        res.append(before)
        res.append(sample[i])

for _ in range(m - cnt):
    res.pop()

for val in res:
    print(val, end=' ')
