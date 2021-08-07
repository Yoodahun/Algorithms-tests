array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우는 실행하지 않음
        return

    pivot = start  # 피벗은 첫번째 원소
    left = start + 1
    right = end

    while (left <= right):  # 겹치지 않는 동안 반복수행
        while (left <= end and array[left] <= array[pivot]):  # 왼쪽값이 배열의 끝까지 가지 않고, 피벗보다 큰 데이터를 찾을 때 까지 반복
            left += 1
        while (right > start and array[right] >= array[pivot]):  # 오른쪽값이 배열의 첫부분까지 가지 않고, 피벗보다 작은 데이터를 찾을때까지 반복
            right -= 1

        if (left > right):  # 엇갈리게 되었다면
            array[right], array[pivot] = array[pivot], array[right]  # 작은 데이터와 피벗을 교체
        else:  # 아직 엇길리지 않았다면
            array[left], array[right] = array[right], array[left]  # 작은 데이터와 큰 데이터를 교체

    # 위 반복문 전체를 수행하였다면 반절로 쪼개졌을 것임. 왼쪽과 오른쪽을 나누어 재귀실행
    # 작은데이터와 피벗을 교체하였으므로, right는 이미 피벗이 된 상황임. 피벗=right를 기준으로 +1, -1을 진행해주어야 함.
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
