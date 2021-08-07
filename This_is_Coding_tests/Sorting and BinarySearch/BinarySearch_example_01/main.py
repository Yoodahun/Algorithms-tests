n, m = map(int, input().split()) # 떡의 개수와 요청한 떡의 길이
array = list(map(int,input().split())) #각 떡의 개별 높이 정보를 입력


# 이진 탐색을 위한 시작점과 끝 점 설정
start = 0
end = max(array)

#이진 탐색 수행 (반복적으로)
result = 0
while(start <= end):
    total = 0
    mid = round((start+end)/2)

    for x in array:
        if x > mid:
            total += x - mid    #잘랐을 떄의 떡의 양 계산.

    if total < m: # 원하는 떡의 길이보다 전체 양이 적다면,
        end = mid-1 # 왼쪽을 탐색하도록 mid의 이전값을 end값으로 지정
    else: # 원하는 떡의 길이가 전체 양보다 많거나 적다면,
        result = mid #최대한 적게 잘랐을 때가 정답이므로 여기서 result에 기록
        start = mid +1 #오른쪽을 탐색하도록 start를 mid의 다음값으로 지정.

print(result)
