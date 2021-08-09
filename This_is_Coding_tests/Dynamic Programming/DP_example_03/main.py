n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

# dp 테이블 초기화
d = [10001] * (m+1)

d[0] = 0
for i in range(n): #동전의 개수만큼 하나씩 체크
    for j in range(array[i], m+1):
        if [d[j - array[i]]] != 10001: #(i - k)원을 만드는 방법이 존재하는 경우.
            d[j] = min(d[j], d[j - array[i]]+1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])