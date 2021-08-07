def binary_search_recursively(array, target, start, end):
    if start > end:
        return None  # 못찾고 배열의 범위를 넘어가게 되는 경우.

    mid = (start + end) / 2  # 중간값 계산

    if array[mid] == target:
        return mid  # 찾고자하는 값과 배열의 중간값이 일치한다면, 인덱스 리턴.
    elif array[mid] > target:  # 찾고자하는 값보다 배열의 중간값이 크다면, 배열의 왼쪽, 중간값보다 작은 값들로만 찾음.
        return binary_search_recursively(array, target, start, mid - 1)
    else:  # 찾고자하는 값보다 배열의 중간값이 작다면, 배열의 오른쪽, 중간값보다 큰 값들로만 찾음.
        return binary_search_recursively(array, target, mid + 1, end)


def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) / 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_recursively(array, target, 0, n - 1)
if result == None:
    print("There is no element")
else:
    print(result + 1)
