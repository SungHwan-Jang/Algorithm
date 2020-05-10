import sys

sys.stdin = open("test.txt", "rt")

samples = list(map(str, input()))
print(samples)

res = []

for item in samples:
    if item.isdecimal():
        res.append(item)
    else:
        if item == '+':
            base_num = int(res.pop())
            res.append(int(res.pop()) + base_num)
        elif item == '-':
            base_num = int(res.pop())
            res.append(int(res.pop()) - base_num)
        elif item == '*':
            base_num = int(res.pop())
            res.append(int(res.pop()) * base_num)
        elif item == '/':
            base_num = int(res.pop())
            res.append(int(res.pop()) / base_num)

print(int(res.pop()))