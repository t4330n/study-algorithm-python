N, L = map(int, input().split())

road = [0 for _ in range(L+1)]

for _ in range(N):
    D, R, G = map(int, input().split())

    road[D] = [R, G]

result = 0
for idx in range(len(road)):
    result += 1

    if road[idx] != 0:
        if result % sum(road[idx]) < road[idx][0]:
            result += road[idx][0] - (result % sum(road[idx]))

print(result)