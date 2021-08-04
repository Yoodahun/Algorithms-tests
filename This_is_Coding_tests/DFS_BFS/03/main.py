# 조합 라이브러리를 사용
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # N x N 복도 정보
teacher = [] # 선생님의 위치 정보
spaces = [] #모든 빈 공간 정보

for i in range(n):
    board.append(list(input().split()))

    for j in range(n):
        #선생님의 존재하는 위치 저장
        if board[i][j] == 'T':
            teacher.append((i, j))

        # 장애물을 설치할 수 있는 빈 공간 위치 저장
        if board[i][j] == 'X':
            spaces.append((i,j))


def watch(x, y, direction):
    # 각 단계별로 보드의 끝까지 검색해봄.
    # 왼쪽으로 방향 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False

            y -= 1

    #오른쪽으로 방향 감시
    if direction == 1:
        while y < n:행
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False

            y += 1

    #위쪽으로 방향 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False

            x -= 1

    #아래쪽으로 방향 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == '0':
                return False

            x += 1

    return False

#장애물 설치 이후 학생이 감시되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teacher:
        # 4방향으로 감시가 가능한지 확인
        for i in range(4):
            if watch(x, y, i):
                return True

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는 지 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치
    for x, y in data:
        board[x][y] = '0'

    # 학생이 한 명도 감지되지 않는 경우
    if not process(): # Process 실행 -> 4번동안 4방향으로 watch 실
        find = True
        break

    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')