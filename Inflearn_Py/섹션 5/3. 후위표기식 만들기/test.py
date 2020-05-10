import sys

sys.stdin = open("test.txt", "rt")
samples = list(map(str, input()))
print(samples)

stack = []
res = ''

for x in samples:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()  # ( 제거를 위함. -> if ) 선입력 이라면 ?

while stack:
    res += stack.pop()  # 남은 ope 모두 pop

print(res)
