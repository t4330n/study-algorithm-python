# H, W 입력받기
H, W = map(int, input().split())

cloud = [list(input()) for _ in range(H)]

result = [[0] * W for _ in range(H)]
for x in range(H):
    for y in range(W):
        if cloud[x][y] == 'c':
            result[x][y] = 0
        else:
            result[x][y] = -1

for row in range(len(result)):
    for col in range(1, len(result[row])):
        if result[row][col] == -1 and result[row][col - 1] >= 0:
            result[row][col] = result[row][col - 1] + 1

for row in result:
    print(*row)
