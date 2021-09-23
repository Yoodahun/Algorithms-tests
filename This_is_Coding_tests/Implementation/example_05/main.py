# 맵 크기 입력
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화.
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 좌표와 방향을 입력받기.
x, y, direction = map(int, input().split())
d[x][y] = 1

# 전체 맵 입력받기.
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방향 정의, 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 북 0 / 동 1 / 남 2 / 서 3

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:  # 북쪽인데 -1이된다면, 서쪽을 바라보게끔.
        direction = 3


# Start
count = 1
turn_time = 0
while True:
    # 현재 방향에서 왼쪽으로 회전.
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 후 정면에 가보지 않은 칸이 존재한다면, 이동할 것.
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1  # 이동
        # 이동한 좌표를 현재 좌표로 갱신
        x = nx
        y = ny
        # 이동 횟수 추가
        count += 1
        # 회전 횟수 초기화
        turn_time = 0
        continue
    else:  # 이미 가본 곳이나 바다라면,
        turn_time += 1
        # 회전 회수를 증가시키고, 다시 반복문의 처음부터 시작. 제자리에서 뱅글뱅글 도는 것.
    print(f"{x}, {y}")
    if turn_time == 4:  # 만약 4 방향 다 갈 수 없는 경우라면,
        # 방향을 유지하고 뒤로 가기.
        nx = x - dx[direction]
        ny = y - dx[direction]
        # 뒤로 갈 수 있는지 일단 체크하고 가기.
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:  # 뒤가 바다라면
            break

        turn_time = 0

print(count)
