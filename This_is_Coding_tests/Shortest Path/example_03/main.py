import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra_using_heap(start):
    q = []
    # 시작 노드로 가기위한 최단 경로는 0으로 설정.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 꺼낸 적이 있다면 무시, 즉 원래 노드거리보다 계산된 노드 거리가 더 짧다면, 무시.
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드들을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]  # 도시 개수만큼 반복문을 돌림.
distance = [INF] * (n + 1)  # 최단 거리 저장 테이블을 모두 무한으로 초기화

# 모든 가선 정보를 입력받기.
for _ in range(m):  # 간선 개수만큼 반복
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # x에서 y도시로 이어지 간선의 시간. 메세지가 전달되는 시간.

dijkstra_using_heap(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d) #제일 거리가 먼 경우를 추려냄.

# 시작 노드는 제외해야하기 때문에, count -1 실행
print(count - 1, max_distance)
