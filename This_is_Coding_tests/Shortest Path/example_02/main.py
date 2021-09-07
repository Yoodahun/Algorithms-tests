INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n, m = map(int, input().split())

# 2차원리스트를 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받고 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용을 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1  # a에서 b로 가는 비용을 1이라 설정.
    graph[b][a] = 1  # 양방향 간선이므로 동일함.

# 거쳐 갈 노드 K와 도착할 노드 X를 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            print(f"graph[{a}][{b}]: {graph[a][b]}, graph[{a}][{k}]+graph[{k}][{b}]: {graph[a][k]+graph[k][b]}")
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

#수행 결과를 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)