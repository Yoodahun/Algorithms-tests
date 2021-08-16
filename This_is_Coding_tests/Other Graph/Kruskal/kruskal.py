'''To find minimum spanning tree'''


def find_parent_path_compression(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_path_compression(parent, parent[x])

    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent_path_compression(parent, a)
    b = find_parent_path_compression(parent, b)

    if a < b:  # 노드 값이 높은 것을 부모 노드로 설정.
        parent[b] = a  # 즉, a의 값이 1에 가깝다면, b의 부모를 a로 설정.
    else:
        parent[a] = b  # 반대로 b의 값이 1에 가깝다면, a의 부모를 b로 설정.


v, e = map(int, input().split())  # 노드의 개수와 간선의 개수 입력 받기
parent = [0] * (v + 1)  # 부모테이블 초기화하기

# 모든 간선을 담을 리스트와 초종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서, 부모를 일단 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기.
# 간선의 비용과 a, b 노드입력받기

for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정

    edges.append((cost, a, b))

# 간선 오름차순 정렬
edges.sort()

for edge in edges:  # 간선을 하나씩 확인해나가며
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함

    if find_parent_path_compression(parent, a) != find_parent_path_compression(parent, b):
        # 같은 부모노드를 가지고 있다면, 그것은 사이클이 발생하는 것이기 때문에, 같은 부모노드가 아닐 때에만 하나의 집합으로 해줌.
        union_parent(parent, a, b)
        result += cost

print(cost)
