from collections import deque

# 노드의 개수와 간선의 개수를 입력받기.
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 노드 A에서 B로 이동.

    # 진입차수를 1 증가
    indegree[b] += 1


# 위상 정렬
def topology_sort():
    result = []  # 수행결과를 담을 리스트
    q = deque()  # queue생성

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)  # 첫 시작할 때, 진입 차수가 0인 노드를 큐에 삽입.

    while q:  # q에 내용이 없을 떄 까지.
        now = q.popleft()  # 큐에서 하나 꺼내기
        result.append(now)  # 결과에 일단 넣기.

        for i in graph[now]:
            indegree[i] -= 1 #해당 노드와 연결된 노드들의 진입차수에서 1을 빼기
            # 새롭게 진입차수가 0이 되는 노드를 큐에 다시 삽입

            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
