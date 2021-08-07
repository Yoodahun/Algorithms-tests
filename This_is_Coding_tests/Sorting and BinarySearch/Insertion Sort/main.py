array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #인덱스 i부터 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]: #한 칸씩 앞으로, 왼쪽으로 이동하는 것. 나보다 앞 원소가 더 크다면, 즉 내가 더 적다면
            array[j], array[j-1] = array[j-1], array[j] #앞과 나를 바꾸어준다.

        else: #자신보다 작은 데이터를 만다면 멈춤
           break

print(array)