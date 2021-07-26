S = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in S:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자인 경우 따로 더하기
    else:
        value += int(x)

#알파벳을 오름차순으로 졍렬
result.sort()

# 숫자가 존재한다면, 문자로 바꾸어서 배열 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종결과 출력 - 문자의 배열을, 하나의 문자열로 join하여 출력.
print(''.join(result))