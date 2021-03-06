import sys
import heapq

# input_readline = sys.stdin.readline()  # 많은 양의 데이터를 한 번에 입력받을 때.
INF = int(1e9)  # 무한 수

# 노드의 개수, 간선의 개수를 입력받기.
n, m = map(int, input().split())

# 시작 노드를 입력받기
start = int(input())

# 각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)

# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a노드에서 b노드로 가는 비용이 c라는 것.


# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번화를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작노드 초기화
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


#################################

def dijkstra_using_heap(start):
    q = []
    # 시작 노드로 가기위한 최단 경로는 0으로 설정.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 꺼낸 적이 있다면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드들을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# dijkstra(start)
dijkstra_using_heap(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
