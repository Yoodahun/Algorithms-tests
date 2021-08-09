


for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int,input().split())) #금광 정보를 저장할 배열

    dp = []
    index = 0

    for i in range(n): #행
        dp.append(array[index:index+m])
        index += m

    for j in range(1, m): #열.
        for z in range(n): #행

            #왼쪽 위에서 오는 경우
            if z == 0:
                left_up = 0
            else:
                left_up =dp[z-1][j-1]

            if z == n-1 : #왼쪽 아래에서 오는 경우.
                left_down = 0
            else:
                left_down = dp[z+1][j-1]

            #왼쪽에서 오는 경우
            left = dp[z][j-1]
            dp[z][j] = dp[z][j] + max(left_up, left_down, left)
    result = 0

    for i in range(n):
        result = max(result, dp[i][m-1]) #제일 마지막 배열값들이 최대값이기 때문에, 확인함.

    print(result)
