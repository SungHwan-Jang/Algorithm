import sys

sys.stdin = open("test.txt", "rt")

sample1 = list(map(str, input()))
sample2 = list(map(str, input()))

data1_dict = dict()
data2_dict = dict()

print(sample1, sample2)

for val in sample1:
    data1_dict[val] = data1_dict.get(val, 0) + 1  # data1_dict.get(val, 0) -> val key값 없을시에 0으로 초기화

# for val in sample1:
#     data1_dict[val] = 0
#
# for val in sample1:
#     data1_dict[val] += 1

print(data1_dict)

for val in sample2:
    data2_dict[val] = data2_dict.get(val, 0) + 1  # data2_dict.get(val, 0) -> val key값 없을시에 0으로 초기화

# for val in sample2:
#     data2_dict[val] = 0
#
# for val in sample2:
#     data2_dict[val] += 1


# 이런 방식으로 해야 아나그램인지 판별도 하고...
# for key in data1_dict.keys():
#     if key in data2_dict.keys():
#         if data1_dict[key] != data2_dict[key]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break

for key, value in data2_dict.items():
    data1_dict[key] -= value

flag = True

for key, val in data1_dict.items():
    if val != 0:
        flag = False
        break

if flag == True:
    print("YES")
else:
    print("NO")
