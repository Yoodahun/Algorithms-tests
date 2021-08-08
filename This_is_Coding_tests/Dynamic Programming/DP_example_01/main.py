n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

# Dynamic programming
d[0] = array[0] # 첫번쨰 값
d[1] = max(array[0], array[1]) #첫번째값과 두번째 값중 큰 값을 넣음.
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i]) # 바로 앞 값, 혹은 그 전 값+현재 값, 한 칸을 띄운 값 중에 큰 것을 설정함.

    # d[i-1] : i번째 식량창고까지의 최적의 해

print(d[n-1]) #마지막 위치의 값이 우리가 알고자하는 값.