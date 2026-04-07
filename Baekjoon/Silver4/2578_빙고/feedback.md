### 1. 🔍 요구사항 분석 및 유형 파악

* **문제 유형:** 2차원 배열 시뮬레이션, 구현
* **유형 파악 키워드:** "3개의 선이 그어지는 순간", "몇 번째 수를 부른 후"
* **핵심 목표:** 숫자를 0으로 지우는 작업과, 0이 5개인 줄(선)을 세는 작업을 반복하기.
* **길어지는 원인 파악:**
    1. **로직의 혼재:** '숫자를 찾는(지우는) 로직'과 '빙고를 확인하는 로직'이 하나의 거대한 2중 for문 안에 전부 섞여 있습니다.
    2. **데이터의 중복:** `bingo`와 `t_bingo` 두 개의 판을 동시에 관리(업데이트)하느라 코드가 두 배로 늘어났습니다.

### 2. 🧠 논리적 설계 (주석 뼈대)

기능을 철저하게 분리(Decoupling)하여 메인 로직의 흐름을 3줄로 압축하는 뼈대입니다.

```markdown
1. 빙고판(5x5)을 입력받는다.
2. 사회자가 부르는 숫자들(5x5)은 다루기 쉽게 1차원 리스트(길이 25)로 쫙 펼친다.
3. [모듈 분리] 현재 빙고판의 선 개수를 세어 3 이상인지(True/False) 반환하는 함수를 만든다.
4. 사회자가 부르는 숫자를 순서대로 순회하며:
   4-1. 빙고판에서 해당 숫자를 찾아 0으로 바꾼다.
   4-2. 빙고 확인 함수를 호출하여 True면 현재 순서(cnt)를 출력하고 종료한다.
```

### 3. 💻 코드 구현 리뷰 (사용자 코드 분석)

* **다중 루프와 `found` 플래그:**
    ```python
    for row in numbers:
        for number in row:
            ...
        if result >= 3:
            found = True
            break
    if found:
        break
    ```
  부르는 숫자마저 2차원 배열로 받다 보니, 탈출을 위해 `found`라는 외부 변수와 `break`를 두 번이나 써야 했습니다. 입력받을 때부터 1차원 배열로 평탄화(Flatten)하면 for문 하나가 통째로
  날아갑니다.

### 4. 🛡️ 엣지 케이스 점검

* **동시 빙고 발생 (매우 중요):** 숫자 하나를 지웠을 때 가로줄과 세로줄이 십자(┼)로 동시에 완성될 수 있습니다. 이때 빙고 선의 개수는 2개에서 4개로 훌쩍 건너뜁니다. 사용자님께서
  `if result == 3`이 아니라 `if result >= 3`으로 처리하신 것은 이 치명적인 반례를 완벽하게 방어해 낸 최고의 로직입니다!

### 5. 🏆 최고 수준 최적화 (Review & Optimization)

리뷰 내용을 반영하여, 복잡했던 검사 로직을 `check_bingo()`라는 별도의 함수로 모듈화하고 파이썬의 강력한 내장 함수들로 압축한 코드입니다.

```python
import sys

input = sys.stdin.readline


# 빙고 확인 모듈 (독립적인 기능으로 분리)
def check_bingo():
    lines = 0

    # 1. 가로, 세로 선 확인
    for i in range(5):
        # 가로줄의 합이 0이면 빙고 (숫자들을 0으로 지웠으므로)
        if sum(bingo[i]) == 0:
            lines += 1
        # 세로줄의 합이 0이면 빙고 (zip 없이 리스트 컴프리헨션 활용)
        if sum(bingo[j][i] for j in range(5)) == 0:
            lines += 1

    # 2. 두 대각선 확인
    if sum(bingo[i][i] for i in range(5)) == 0:
        lines += 1
    if sum(bingo[i][4 - i] for i in range(5)) == 0:
        lines += 1

    return lines >= 3


# --- 메인 로직 ---
# 1. 빙고판 입력
bingo = [list(map(int, input().split())) for _ in range(5)]

# 2. 부르는 숫자 입력 (2차원 -> 1차원 배열로 한 줄로 펼치기)
numbers = []
for _ in range(5):
    numbers.extend(list(map(int, input().split())))

# 3. 시뮬레이션 시작
for cnt, num in enumerate(numbers, 1):  # enumerate로 1부터 카운트 자동 계산

    # 숫자 찾아 지우기
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0

    # 빙고 확인 모듈 호출
    if check_bingo():
        print(cnt)
        break
```

💡 **최적화 핵심 원리:**

* **함수 모듈화 (`def check_bingo`):** 코드가 획기적으로 짧고 읽기 쉬워진 이유입니다. 검사 로직을 밖으로 빼내면 들여쓰기(Indent)가 깊어지는 것을 막을 수 있고, 코드를 읽을 때 "아,
  여기서 빙고인지 검사하는구나" 하고 인간의 사고 흐름대로 읽히게 됩니다.
* **1차원 배열 평탄화 (`.extend()`):** `numbers`를 1차원 배열로 만들고 `enumerate(numbers, 1)`를 사용함으로써, 직접 `cnt += 1`을 계산하거나 이중 루프를 돌며
  `found` 플래그를 관리해야 하는 귀찮음을 완전히 제거했습니다.
