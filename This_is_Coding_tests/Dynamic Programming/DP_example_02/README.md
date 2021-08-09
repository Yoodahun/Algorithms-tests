# 1로 만들기
- 정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지 이다.
  - X가 5로 나누어 떨어지면, 5로 나눈다.
  - X가 3으로 나누어 떨어지면, 3으로 나눈다.
  - X가 2로 나누어떨어지면 2로 나눈다.
  - X에서 1을 뺀다.
- 정수 X가 주어졌을 대, 연산 4개를 적절히 사용하여 값을 1로 만들고자 한다. 연산을 사용하는 횟쉬의 최소값을 출력하라.

## 입력 조건
- 첫째 줄에 정수 X가 주어진다. `(1 <= X <= 30,000)`

## 출력 조건
- 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

## 문제 해결
- 최적 부분 구조와 중복되는 부분 문제를 만족하는지 확인해야할 것.