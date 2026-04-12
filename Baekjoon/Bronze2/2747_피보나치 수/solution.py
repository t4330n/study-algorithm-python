lst = [0] * 46
lst[0] = 0
lst[1] = 1

n = int(input())

for i in range(2, 46):
    lst[i] = lst[i - 1] + lst[i - 2]

print(lst[n])
