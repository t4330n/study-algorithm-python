### 1. 🔍 요구사항 분석 및 유형 파악 (Upgrade!)
* **문제 유형:** 완전 탐색 (Brute-Force), 2차원 배열 구현
* **유형 파악 키워드:** "인접한 두 칸을 고른다", "서로 교환한다", "가장 긴 연속 부분(행 또는 열)을 고른다", **"$N$은 3에서 50 사이이다"**
    * $N$이 최대 50이라는 것이 가장 결정적인 단서입니다. 컴퓨터가 모든 인접한 칸을 다 바꿔보고, 매번 전체 보드를 다 훑어서 사탕 개수를 세어도 시간이 남아돈다는 뜻입니다. 머리를 쓰지 않고 무식하게 다 해보는 것이 이 문제의 정답입니다.
* **핵심 목표:** (1) 인접한 두 사탕을 교환한다. $\rightarrow$ (2) 보드 전체에서 가장 긴 사탕 길이를 찾는다. $\rightarrow$ (3) 사탕을 다시 원래대로 되돌려 놓는다. 이 과정을 모든 칸에 대해 반복하기.
* **입력 범위 및 시간 복잡도:** $N \le 50$. 인접한 칸을 바꾸는 경우의 수는 약 $2N^2$ (오른쪽, 아래쪽). 한 번 바꿀 때마다 가장 긴 길이를 찾는 연산은 전체 보드를 훑으므로 $O(N^2)$. 총 연산량은 $O(N^4) \approx 6,250,000$번으로 파이썬의 1초(약 2,000만 번) 제한 내에 넉넉하게 통과합니다.
* **주의할 엣지 케이스:** 사탕을 바꾼 후 길이를 재고, **반드시 다시 원래대로 되돌려 놓아야(Swap back)** 다음 탐색에 영향을 주지 않습니다.

### 2. 🧠 논리적 설계 (주석 뼈대)
코드가 꼬이는 것을 막기 위해, '사탕 길이를 세는 로직'을 독립적인 함수로 완전히 빼버리는 것이 설계의 핵심입니다.

```markdown
1. N을 입력받고, 사탕 보드를 2차원 리스트로 저장한다.
2. [모듈 분리] 보드 전체를 훑으며 '가장 긴 연속 사탕 길이'를 반환하는 함수를 만든다.
   2-1. 각 행을 검사하며 연속된 색깔의 최대 길이를 찾는다.
   2-2. 각 열을 검사하며 연속된 색깔의 최대 길이를 찾는다.
3. 최댓값을 저장할 변수(max_cnt)를 0으로 초기화한다.
4. 보드의 모든 칸(i, j)을 순회하며:
   4-1. '오른쪽 칸'과 색이 다르다면: 둘을 교환 -> 최대 길이 함수 호출 및 갱신 -> 원상 복구
   4-2. '아래쪽 칸'과 색이 다르다면: 둘을 교환 -> 최대 길이 함수 호출 및 갱신 -> 원상 복구
5. 찾은 최댓값을 출력한다.
```

### 3. 💻 코드 구현 (Pythonic)
뼈대대로 '길이 찾기'를 함수로 묶어내면, 메인 로직은 놀라울 정도로 깔끔해집니다. 파이썬의 다중 할당 교환(`a, b = b, a`)을 활용한 직관적인 코드입니다.

```python
import sys
input = sys.stdin.readline

def check_max_candies(board, n):
    max_len = 1
    
    # 가로, 세로 전체 검사
    for i in range(n):
        row_cnt = 1
        col_cnt = 1
        for j in range(1, n):
            # 가로(행) 검사
            if board[i][j] == board[i][j-1]:
                row_cnt += 1
            else:
                row_cnt = 1
            max_len = max(max_len, row_cnt)
            
            # 세로(열) 검사
            if board[j][i] == board[j-1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            max_len = max(max_len, col_cnt)
            
    return max_len

N = int(input())
board = [list(input().strip()) for _ in range(N)]
max_cnt = 0

for i in range(N):
    for j in range(N):
        # 1. 오른쪽 칸과 교환 (범위 초과 방지)
        if j + 1 < N and board[i][j] != board[i][j+1]:
            # 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            # 최대 길이 갱신
            max_cnt = max(max_cnt, check_max_candies(board, N))
            # 원상 복구
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
        # 2. 아래쪽 칸과 교환 (범위 초과 방지)
        if i + 1 < N and board[i][j] != board[i+1][j]:
            # 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            # 최대 길이 갱신
            max_cnt = max(max_cnt, check_max_candies(board, N))
            # 원상 복구
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max_cnt)
```

### 4. 🛡️ 엣지 케이스 점검
* **인덱스 초과 에러 (IndexError):** 오른쪽과 교환할 때는 `j + 1 < N`, 아래쪽과 교환할 때는 `i + 1 < N` 조건을 걸어 완벽하게 방어했습니다.
* **같은 색깔끼리 교환하는 낭비:** `if board[i][j] != board[i][j+1]:` 조건을 넣어, 어차피 교환해도 의미가 없는 같은 색깔일 때는 검사 자체를 건너뛰도록 하여 연산량을 최적화했습니다.

### 5. 🏆 최고 수준 최적화 (Review & Optimization)
위 코드로도 충분히 정답을 받지만, 파이썬에서 실행 시간을 극단적으로 줄이려면 **'조기 종료(Early Catch)'** 기법을 추가하는 것이 가장 파괴적입니다.

💡 **최적화 핵심 원리:**

이 보드에서 얻을 수 있는 가장 긴 연속 부분의 길이는 어차피 $N$입니다. 만약 탐색 도중에 연속된 사탕 길이가 $N$이 나왔다면, 그보다 더 큰 정답은 존재할 수 없으므로 **더 이상 탐색하지 않고 프로그램 전체를 종료**해 버리면 됩니다.

```python
# check_max_candies 함수 내부와 메인 for문 하단에 이 로직 추가
if max_len == n:
    return n

# 메인 로직에서
if max_cnt == N:
    print(N)
    exit()
```