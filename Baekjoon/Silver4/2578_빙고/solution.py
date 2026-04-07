bingo = [list(map(int, input().split())) for _ in range(5)]
t_bingo = list(map(list, zip(*bingo)))
numbers = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
found = False

for row in numbers:
    for number in row:
        cnt += 1

        # 숫자 불렀고
        # 부른 숫자 빙고판에서 찾아서 0으로 만들기
        for row2 in range(len(bingo)):
            for col2 in range(len(bingo[0])):
                if bingo[row2][col2] == number:
                    bingo[row2][col2] = 0
                    t_bingo[col2][row2] = 0

        result = 0
        # 빙고 확인하기 (0이 5개이면 빙고)
        # 가로
        for row3 in bingo:
            if row3.count(0) == 5:
                result += 1
        # 세로
        for row4 in t_bingo:
            if row4.count(0) == 5:
                result += 1
        # 대각선
        temp1 = 0
        temp2 = 0
        for i in range(len(bingo)):
            temp1 += bingo[i][i]
            temp2 += bingo[i][4 - i]
        if temp1 == 0:
            result += 1
        if temp2 == 0:
            result += 1

        if result >= 3:
            print(f'{cnt}')
            found = True
            break
    if found:
        break
