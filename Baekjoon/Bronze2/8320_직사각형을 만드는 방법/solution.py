# 길이가 1인 정사각형 n개 입력
n = int(input())

result = {}
# 직사각형 만들기
for row in range(1, n + 1):

    for col in range(1, n + 1):

        condition = (row * col) > n

        if condition:
            break

        if (col, row) not in result:
            result[(row, col)] = 1

print(len(result))
