n = int(input())
array = list(map(int, input().split()))

array.reverse() #순서를 뒤집어서 최장 증가 부분 수열 문제로 변환

# 다이나믹 프로그래밍을 위한 1차원 테이블 초기화
dp = [1] * n

#가장 긴 증가하는 부분 수열 알고리즘 수행
for i in range(1, n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외해야하는 병사수 출력
print(n - max(dp))