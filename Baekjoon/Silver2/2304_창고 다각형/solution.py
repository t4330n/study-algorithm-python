# 입력받기
N = int(input())

storage = [0] * 1001

max_L, max_H = 0, 0

for _ in range(1, N+1):
    L, H = map(int, input().split())

    storage[L] = H
    
    if H > max_H:
        max_H = H
        max_L = L


result = 0

temp = 0
for i in range(1, max_L):
    h = storage[i]

    if h == 0:
       result += temp 
    else:
        if h > temp:
            result += h
            temp = h
        else:
            result += temp
    
temp = 0
for i in range(1000, max_L, -1):
    h = storage[i]

    if h == 0:
       result += temp 
    else:
        if h > temp:
            result += h
            temp = h
        else:
            result += temp


print(result+ max_H)