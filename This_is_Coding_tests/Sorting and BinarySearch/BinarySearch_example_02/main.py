from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value) #오른쪽부터 검색해서 넣어야할 위치
    left_index = bisect_left(array, left_value) #왼쪽에서부터 검색하여 제일 처음으로 넣어야할 위치
    return right_index - left_index #각각의 인덱스를 빼줌으로써 해당 원소가 몇개 들어있는지 알 수 있다. 오른쪽으로 가면 갈수록 인덱스의 값이 커지므로, 오른쪽에서 왼쪽 값을 빼준다.

n, x = map(int, input().split())
array = list(map(int, input().split()))

#오른쪽에서 검색할 값과 왼쪽에서부터 검색할 값을 같이 넣어준다.
count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)