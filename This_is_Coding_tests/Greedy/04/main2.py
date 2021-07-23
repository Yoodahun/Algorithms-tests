n, k = map(int, input().split())
result = 0

# N이 K이 이상이라면 K로 계속 나누기
while n >= k:

    while n % k != 0:
        n -= 1
        result += 1

    #K로 N을 나눈 몫을 저장
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)