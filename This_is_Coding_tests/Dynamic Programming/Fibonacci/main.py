d = [0] * 100


def fibonacci_recursively(x):
    if x == 1 or x == 2:  # x가 1이나 2일 떄는 1을 리턴해줌.
        return 1

    return fibonacci_recursively(x - 1) + fibonacci_recursively(x - 2)


def fibonacci_top_down(x):
    if x == 1 or x == 2:  # x가 1이나 2일 떄는 1을 리턴해줌.
        return 1

    if d[x] != 0:
        return d[x]  # 재귀적으로 호출하다보면 특정 값들이 중복되어 계산되는데, 그때 이미 다른 곳에서 계싼된적이 있다면 그 값을 가져와서 사용함.

    d[x] = fibonacci_top_down(x - 1) + fibonacci_top_down(x - 2)  # 계산된 값을 배열에 미리 저장해놓음.
    return d[x]


print(fibonacci_top_down(4))
