# BFS Queue사용
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 시험관 정보를 담음
data = [] # 전체 바이러스 정보를 담음

for i in range(n):
    #시험관을 한 줄 단위로 입력
    graph.append(list(map(int,input().split())))

    for j in range(n):
    #해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 바이러스 정보를 낮은 순부터로 정렬한 다음 큐로 옮겨 넣기.
data.sort() #오름차순
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치 상,
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 실행

while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break

    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        #해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            #아직 방문하지 않았다면, 위치에 바이러스를 집어 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny)) # queue에 다시 넣기

print(graph[target_x-1][target_y-1])