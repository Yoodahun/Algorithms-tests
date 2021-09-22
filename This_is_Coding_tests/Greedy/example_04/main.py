# N, M을 공백을 구분하여 입력
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 줄에서 가장 작은 값을 찾기
    min_value = min(data)

    # 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
