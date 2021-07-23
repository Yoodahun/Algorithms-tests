input_list = input()

result = int(input_list[0]) #먼저 집어넣고 판단.

for i in range(1, len(input_list)):

    #두 수 중에서 하나라도 0, 혹은 1인 경우 더하기. 그 외에는 곱하기.
    num = int(input_list[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num

print(result)