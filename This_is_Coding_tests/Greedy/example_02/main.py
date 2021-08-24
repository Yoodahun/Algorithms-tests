n = int(input())
x = list(map(int, input().split()))
x.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in x:
    count += 1  # 현재 그룹에 일단 포함시키기

    if count >= i:  # 현재 그룹에 포함된 모험가의 수가, 현재 공포도 이상이라면 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력
