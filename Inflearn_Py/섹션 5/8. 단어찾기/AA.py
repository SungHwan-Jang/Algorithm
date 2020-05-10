n = int(input())
hashmap = dict()

for _ in range(n):
    word = input()
    hashmap[word] = 1

for _ in range(n - 1):
    word = input()
    hashmap[word] = 0

for key, value in hashmap.items():
    if value == 1:
        print(key)
