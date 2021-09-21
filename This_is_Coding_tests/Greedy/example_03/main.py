# 각각의 값을 입력받아 숫자로 만든 후 각각의 변수에 할당.
# 배열의 길이, 최대한 숫자를 더할 횟수, 최대숫자를 연속으로 더할 수 있는 횟
n, m, k = map(int, input().split())

# 공백으로 구분된 입력값들을 하나의 배열로 만듦.
data = list(map(int, input().split()))

data.sort(reverse=True)

first_value = data[0]
second_value = data[1]

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:
            break
        result += first_value  # 가장 큰 수를 K번 반복 더하기
        m -= 1  # 한 번 더할 때마다 최대횟수 감소

    if m == 0:  # 최대횟수가 0이라면 반복문 탈출
        break

    result += second_value  # K번 연속으로 더한 후에, 두번째로 큰 값을 더함.
    m -= 1  # 한 번 더할 때마다 최대횟수 감소.

print(result)
