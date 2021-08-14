# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def find_parent_path_compression(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_path_compression(parent, parent[x])

    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:  # 노드 값이 높은 것을 부모 노드로 설정.
        parent[b] = a  # 즉, a의 값이 1에 가깝다면, b의 부모를 a로 설정.
    else:
        parent[a] = b  # 반대로 b의 값이 1에 가깝다면, a의 부모를 b로 설정.


v, e = map(int, input().split())  # 노드의 개수와 간선의 개수 입력 받기
parent = [0] * (v + 1)  # 부모테이블 초기화하기

# 부모 테이블 상에서, 부모를 일단 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False #사이클 발생 여부

# Union수행
for i in range(e):
    a, b = map(int, input().split())

    #사이클이 발생한 경우 종료
    if find_parent_path_compression(parent, a) == find_parent_path_compression(parent, b):
        #각각의 노드의 부모가 같다면.
        cycle = True
        break
    else: # 사이클이 발생하지 않았다면 합집합 실행
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생하였습니다.")
else:

    # 각 원소가 속한 집합 출력하기
    print('각 원소가 속한 집합: ', end='')
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')

    print()

    # 부모 테이블 내용 출력하기
    print('부모 테이블: ', end='')
    for i in range(1, v + 1):
        print(parent[i], end=' ')
