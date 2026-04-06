# 몇번 할지 입력받기
N = int(input())

for _ in range(N):
    # 각 케이스 마다 숫자, 학생들 입력받기
    orders = list(map(int, input().split()))
    t = orders[0]
    students = orders[1:]

    result = 0
    pointer = len(students) - 1
    for _ in range(len(students) - 1):
        if students[pointer] > max(students[:pointer]):
            pointer -= 1
            continue

        pivot = students[pointer]
        compare = students[:pointer]

        for i in range(len(compare)):
            if compare[i] > pivot:
                students.remove(pivot)
                students.insert(i, pivot)
                result += len(compare) - i
                break

    print(f'{t} {result}')
