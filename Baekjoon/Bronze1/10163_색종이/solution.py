# 평면 1001 * 1001
arr = [[0] * 1001 for _ in range(1001)]

# 색종이 개수 N 입력받기
N = int(input())

# 색종이 개수만큼 반복 
for i in range(1, N+1):

#     색종이 정보 입력 받기
    s_y, s_x, w, h = map(int, input().split())

#     평면에 색종이 번호로 색칠하기
    for x in range(s_x, s_x + h):
        for y in range(s_y, s_y + w):
            arr[x][y] = i



# 평면에서 색종이 넓이 출력하기
for i in range(1, N+1):
    count = 0
    for row in arr:
        for col in row:
            if col == i:
                count += 1
    print(count)
