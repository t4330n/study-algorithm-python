from cmath import inf

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = float(-inf)

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if result < cards[i] + cards[j] + cards[k] <= M:
                result = cards[i] + cards[j] + cards[k]

print(result)