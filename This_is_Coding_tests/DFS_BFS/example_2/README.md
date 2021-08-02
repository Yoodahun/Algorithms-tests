# 미로 탈출

- 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔다. 미로에는 여러 마리의 괴물이 있어 빨리 탈출해야한다.
- 동빈이의 위치는 (1,1) 미로의 출구는 (N, M) 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이 때 괴물이 있는 부분은 0으로, 없는 부분은 1로 표시되어 있다.
- 이 때 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하시오.

## 입력 조건
- 첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 각각 M개의 정수 (0 혹은 1)로 미로의 정보가 주어진다. 각각의 수들은 공백없이 붙어서 입력으로 제시된다. 또한 시작과 마지막은 항상 1이다.

## 출력 조건
- 첫째 줄에 최소 이동칸의 개수를 출력한다.

## 문제 풀이
- BFS를 이용하여 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색할 수 있다.
- 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일
  - 따라서, (1, 1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있다.

예시로 다음과 같이 3 x 3크기의 미로가 있다고 가정한다.