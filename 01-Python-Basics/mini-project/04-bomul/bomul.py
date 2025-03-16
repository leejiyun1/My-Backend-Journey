"""
[목표]
플레이어는 지도 상에서 보물을 찾아야 합니다. 지도는 그리드로 구성되며, 플레이어는 매 턴마다 이동하여 보물의 위치를 찾아야 합니다. 보물의 위치는 무작위로 설정됩니다.

[게임 설명]
게임 시작 시, 프로그램은 N x N 크기의 그리드를 생성하고, 그리드 내 무작위 위치에 보물을 배치합니다.
플레이어는 그리드 내의 특정 위치에서 시작합니다. 초기 위치도 무작위로 결정됩니다.
플레이어는 북(N), 남(S), 동(E), 서(W) 중 하나의 방향으로 한 칸 이동할 수 있습니다.
이동 후, 플레이어는 보물까지의 대략적인 거리를 알 수 있습니다. 정확한 위치는 알 수 없습니다.
플레이어가 보물 위치에 도달하면 게임이 종료되고, 이동 횟수가 공개됩니다.
[기능 요구 사항]
✅ 그리드 생성: N x N 크기의 게임 보드를 생성합니다.
✅ 보물 및 플레이어 위치 초기화: 보물과 플레이어의 위치를 무작위로 설정합니다.
✅ 이동 명령 수행: 플레이어로부터 이동 명령을 입력받고 수행합니다.
✅ 거리 힌트 제공: 플레이어에게 현재 위치에서 보물까지의 거리에 대한 힌트를 제공합니다.
✅ 게임 종료 조건 확인: 플레이어가 보물을 찾으면 게임을 종료합니다.

[개발 단계]
게임 환경 설정: 필요한 변수(보드 크기, 위치 정보 등)와 게임 보드를 초기화합니다.
플레이어 입력 처리: 플레이어로부터 이동 명령을 입력받고, 입력에 따라 플레이어의 위치를 업데이트합니다.
거리 계산 및 힌트 제공: 현재 플레이어 위치에서 보물까지의 거리를 계산하고, 이를 기반으로 힌트를 제공합니다.
게임 종료 및 결과 출력: 플레이어가 보물 위치에 도달하면 게임을 종료하고, 플레이어의 이동 횟수를 출력합니다.
"""
import random

# 게임 초기화
def initialize_game(n):

    # 보물 위치
    treasure_x = random.randint(0, n-1)
    treasure_y = random.randint(0, n-1)
    treasure_position = (treasure_x, treasure_y)

    # 플레이어 위치
    player_x = random.randint(0, n-1)
    player_y = random.randint(0, n-1)
    player_position = (player_x, player_y)

    # 겹치는거 방지
    while player_position == treasure_position:
        player_x = random.randint(0, n-1)
        player_y = random.randint(0, n-1)
        player_position = (player_x, player_y)

    # 값 반환
    return treasure_position, player_position


# 거리 계산
def calculate_distance(treasure_position, player_position):

    # 계산 및 반환 맨해튼 거리 공식 사용.
    return abs(player_position[0] - treasure_position[0] ) + abs(player_position[1] - treasure_position[1])

# 플레이어 이동
def move_player(board_size, player_position, direction):
    x, y = player_position

    # 이동
    if direction == 'N':
        x -= 1
    elif direction == 'S':
        x += 1
    elif direction == 'E':
        y += 1
    elif direction == 'W':
        y -= 1
    
    # 잘 못 입력시
    else:
        print("잘못된 입력입니다. N(북),S(남),E(동),W(서) 중 하나를 입력해주세요.")
        return player_position

    # 보드를 벗어나지 않도록 제한
    x = max(0, min(board_size - 1, x))
    y = max(0, min(board_size - 1, y))
    return(x, y)

# 게임 실행
def play_game(board_size):

    # 게임 초기화
    treasure_position, player_position = initialize_game(board_size)
    move_count = 0 # 이동 카운트

    print("보물찾기 게임을 시작합니다.")
    print(f"보드 크기 : {board_size}x{board_size}")

    while True:
        # 현재 거리 출력
        distance = calculate_distance(treasure_position , player_position)
        print(f"현재 위치: {player_position}, 보물까지의 거리: {distance}")

        if distance == 0:
            print(f"축하합니다! 보물을 찾았습니다. 이동 횟수: {move_count}")
            break

        direction = input("N(북),S(남),E(동),W(서) 중 하나를 입력해주세요. (종료: Q) ").strip().upper()

        if direction == "Q":
            print("게임을 종료합니다.")
            break

        # 이동 처리
        new_position = move_player(board_size, player_position, direction)

        # 이동이 유효한지 확인
        if new_position == player_position:
            print("❌ 이동할 수 없는 방향입니다. 다시 입력하세요.")
        else:
            player_position = new_position
            move_count += 1  # 이동 횟수 증가

# 게임 보드 크기 설정 및 게임 시작
if __name__ == "__main__":
    board_size = 5  # 보드 크기를 5x5로 설정
    play_game(board_size)