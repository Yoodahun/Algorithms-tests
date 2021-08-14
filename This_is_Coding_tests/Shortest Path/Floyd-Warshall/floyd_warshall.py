INF = int(1e9)

#노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())

#2차원리스트를 만들고, 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받고 그 값으로 초기화
for _ in range(m):
    #A에서 B로 가는 비용을 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c #a에서 b로 가는 비용을 c라 설정.

#플로이드 워셜 알고리즘을 점화식에 따라 수행
for k in range(1, n+1): #특정 노드를 거쳐가는 값들을 확인할 것 인지
    for a in range(1, n+1): #출발 노드
        for b in range(1, n+1): #도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            #출발노드와 도착노드의 합계보다 그냥 시키는게 더싼지 물어보고있다.

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        #도달할 수 없는 경우 무한
        if graph[a][b] == 1e9:
            print("INFINITY")
        else:
            print(graph[a][b], end=" ")
    print()

        #도달할 수 있는 경우 해당 값 출력