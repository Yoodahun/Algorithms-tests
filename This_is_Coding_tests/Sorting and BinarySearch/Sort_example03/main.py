n = int(input())

array = []

# for _ in range(n):
#     text = input().split()
#     array.append((text[0], int(text[1])))
#
#
# array = sorted(array, key=lambda student: student[1])
#
# for student in array:
#     print(student[0], end=" ")

for _ in range(n):
    text = input().split()
    array.append((int(text[1]), text[0]))


array.sort()

for student in array:
    print(student[1], end=" ")