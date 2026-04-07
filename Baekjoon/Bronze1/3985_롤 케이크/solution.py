# 롤 케이크 길이 입력 받기
N = int(input())
roll_cake = [0] *(N+1)
# 인원 수 입력 받기
person = int(input()) + 1

# 인덱스, 케이크 개수
expect = [0,0]
real = [0,0]

# 인원 수 만큼 반복
for i in range(1, person):
    count = 0

    # 한 인원당 가지는 롤 케이크 입력받기
    p, k = map(int, input().split())

    # expect 케이크 개수보다 크면 바꾸기 
    if k-p > expect[1]:
        expect = [i, k-p]

    # 롤케이크 범위 반복문
    for idx in range(p,k+1):
        if roll_cake[idx] != 0:
            continue
        # 롤케이크 인덱스로 처리하기 
        roll_cake[idx] = i
        count += 1

    if count > real[1]:
        real = [i, count]

print(expect[0])
print(real[0])
