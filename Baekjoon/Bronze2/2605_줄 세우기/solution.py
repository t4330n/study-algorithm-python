# 학생 수 입력 받기
# 학생 번호대로 리스트 만들기
N = int(input())
students = [i for i in range(1, N + 1)]

# 각 뽑은 숫자 입력받기
orders = list(map(int, input().split()))

result = []
# 학생 리스트 반복문
for student in students:
    # 뽑은 숫자
    order = orders[student - 1]

    # [:] + 학생 숫자 + [:] 형태로 결과 리스트 변형
    result = result[:len(result) - order] + [student] + result[len(result) - order:]

print(" ".join(list(map(str, result))))
