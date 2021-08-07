n, k = map(int, input().split())  # N과 K를 입력받아 정수로 변환하여 저장
a = list(map(int, input().split()))  # A배열을 입력받아 정수로 변환하여 저장
b = list(map(int, input().split()))  # B배열을 입력받아 정수로 변환하여 저장

a.sort()  # 오름차순 정렬
b.sort(reverse=True)  # 내림차순 정렬

for i in range(k):  # 첫 번째 인덱스부터 확인하여 비교해가며, 두 배열을 최대 K번 비교
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]  # a배열 원소보다 b배열 원소가 큰 경우, 서로 교환
    else:
        break
        # A의 원소가 B원소보다 크거나 같다면, 반복문을 탈출. B배열은 내림차순 정렬이라 이미 제일 첫 원소부터, 배열 내의 제일 큰 값.
        # 그럼에도 불구하고 A원소가 크거나 같다면, 이후 A원소는 오름차순이라 전부 큰 값이므로 비교하는 의미가 없음.

print(sum(a))  # A배열의 모든 원소를 더한 값을 출력.
