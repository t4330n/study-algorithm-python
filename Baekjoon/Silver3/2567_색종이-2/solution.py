N = int(input())

arr = [[0] + [0] * 100 + [0] for _ in range(102)]
for _ in range(N):

    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

result = 0
for x in range(102):
    for y in range(102):

        if arr[x][y] == 0:
            for dx, dy in direction:
                check_x = x + dx
                check_y = y + dy
                if 0 <= check_x <= 101 and 0 <= check_y <= 101 and arr[check_x][check_y] == 1:
                    result += 1

print(result)
