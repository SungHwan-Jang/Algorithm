samples = list(map(str, input()))

res = []
flag = False
cnt = 0
for item in samples:
    if item == '(':
        res.append(item)
        flag = True
    elif item == ')' and flag == True:
        res.pop()
        flag = False
        cnt += len(res)
    elif item == ')':
        res.pop()
        flag = False
        cnt += 1

print(cnt)
