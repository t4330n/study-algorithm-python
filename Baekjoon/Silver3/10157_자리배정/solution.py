# C(row), R(col) 입력받기
C, R = map(int, input().split())

row, col = C, R

arr = [[0] * (col+2) for _ in range(row+2)]

# 우, 하, 좌, 상
di = [[0,1], [1,0], [0,-1], [-1,0]]
dc = 0

x, y = 1, 1

# 번호 입력 받기
K = int(input())

if K > row * col:
    print(0)
else:
    for i in range(1, (C*R)+1):
        arr[x][y] = i

        n_x, n_y = x + di[dc%4][0], y + di[dc%4][1]

        if 1 > n_x or n_x > row or 1 > n_y or n_y > col or arr[n_x][n_y] != 0:
            dc += 1
            n_x, n_y = x + di[dc%4][0], y + di[dc%4][1]
        
        x = n_x
        y = n_y

    for i in range(1, row+1):
        for j in range(1, col+1):
            if arr[i][j] == K:
                print(i, j)