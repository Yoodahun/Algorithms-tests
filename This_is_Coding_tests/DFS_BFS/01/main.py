# BFS를 하기 위해 deque를 import
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 #출발 도시 까지의 거리는 0으로 설정

q = deque([x]) #x를 넣고 시작. 출발도시

while q:
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면
if check == False:
    print(-1)
