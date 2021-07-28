
def dfs(x, y):

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 칸막이로 바꾸어 버리기.

        dfs(x-1, y) # 상
        dfs(x + 1, y)  # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True

    return False


# N, M을 공백으로 구분받기
n, m = map(int, input().split())
graph = []

for i in range(n):
    # 2차원 리스트의 맵 정보 입력 받기
    graph.append(list(map(int, input())))

# 모든 노드에 대하여 확인하기.
result = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result +=1

print(result)