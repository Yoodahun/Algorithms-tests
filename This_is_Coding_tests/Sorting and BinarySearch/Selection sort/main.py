array = [7, 5, 9, 0, 3, 1, 6,2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]: # min_index 자리의 수가 j자리의 수보다 크다면, min_index를 j로 바꿈. 즉, 작은 값을 참조하게끔.
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print(array)