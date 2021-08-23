n = 1260

coins = [500, 100, 50, 10]
count = 0

for coin in coins:
    count += n // coin # 나눈 몫을 count로 더해가며 세줌
    n %= coin # 나머지 값을 다시 다른 동전으로 나누어주어야 하므로 N으로 바꾸어나감.

print(count)