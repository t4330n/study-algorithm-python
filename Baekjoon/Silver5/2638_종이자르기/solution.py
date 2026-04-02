# 직사각형 모양의 종이 크기 입력 받기
s, g = map(int, input().split())

# 몇 번 자를지 입력받기
N = int(input())

gl, sl = [], []
# 어떻게 자르는지 입렫받기 단, 가로 세로 구별해서 저장하기
for _ in range(N):
    d, l = map(int, input().split())

    if d == 0:
        gl.append(l)
    if d == 1:
        sl.append(l)

# 입력받은 가로 세로 정렬하기
sgl = [0] + sorted(gl) + [g]
ssl = [0] + sorted(sl) + [s]

igl, isl = [], []
# 자른 후 각 길이 구하기
for i in range(len(sgl) - 1, 0, -1):
    for j in range(i - 1, i - 2, -1):
        igl.append(sgl[i] - sgl[j])

for i in range(len(ssl) - 1, 0, -1):
    for j in range(i - 1, i - 2, -1):
        isl.append(ssl[i] - ssl[j])

max_g = max(igl)
max_s = max(isl)

print(max_g * max_s)
