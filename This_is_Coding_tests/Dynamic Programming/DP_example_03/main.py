n, m = map(int, input().split()) #N개의 화폐정보, 만들고자하는 M원.

array = []
for _ in range(n):
    array.append(int(input()))

# dp 테이블 초기화
d = [10001] * (m+1)

d[0] = 0
for i in range(n): #동전의 개수만큼 하나씩 체크
    for j in range(array[i], m+1): #해당 동전을 하나하나 체크 시작.
        if [d[j - array[i]]] != 10001: #(i - k)원을 만드는 방법이 존재하는 경우.
            d[j] = min(d[j], d[j - array[i]]+1) #a[i] = min(a[i], a[i-k]+1) K는 동전값.

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])