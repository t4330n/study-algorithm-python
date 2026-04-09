# N, K 입력 받기
N, K = map(int, input().split())

# 온도 배열로 입력 받기
temperatures = list(map(int, input().split()))

# 시작 온도 값 추가하기
results = []
tem = sum(temperatures[:K])
results.append(tem)

# 연속적인 K일의 온도의 합 찾기
for i in range(1, N - K + 1):
    tem = tem - temperatures[i - 1] + temperatures[i + (K - 1)]
    results.append(tem)

print(max(results))
