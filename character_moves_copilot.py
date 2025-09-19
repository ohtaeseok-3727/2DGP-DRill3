from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 경로 (시작/종료점 (400, 90), 화면 전체 활용)
rect_points = [
    (400, 90), (750, 90), (750, 570), (50, 570), (50, 90), (400, 90)
]
rect_index = 0

# 삼각형 경로 (정삼각형, (400, 90)에서 시작/종료, 시계방향)
tri_points = [
    (400, 90), (750, 90), (400, 570), (50, 90), (400, 90)
]
tri_index = 0

# 원 경로 (중심, 반지름, 시작 각도)
circle_center = (400, 330)
circle_rx = 350
circle_ry = 240
angle = -math.pi / 2  # (400, 90)에서 시작

# 상태
state = 'rect'  # 'rect', 'tri', 'circle'

# 시작 위치
x, y = 400, 90

speed = 15  # 이동속도를 더 빠르게 수정
angle_speed = 0.02  # 원운동 각속도도 약간 빠르게

def near_start(px, py):
    return abs(px - 400) < 6 and abs(py - 90) < 6

while True:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)
    get_events()

    if state == 'rect':
        tx, ty = rect_points[rect_index + 1]
        dx, dy = tx - x, ty - y
        dist = math.hypot(dx, dy)
        if dist < speed:
            x, y = tx, ty
            rect_index += 1
            if rect_index == len(rect_points) - 1 and near_start(x, y):
                state = 'tri'
                tri_index = 0
                x, y = tri_points[0]
                rect_index = 0
        else:
            x += speed * dx / dist
            y += speed * dy / dist

    elif state == 'tri':
        tx, ty = tri_points[tri_index + 1]
        dx, dy = tx - x, ty - y
        dist = math.hypot(dx, dy)
        if dist < speed:
            x, y = tx, ty
            tri_index += 1
            if tri_index == len(tri_points) - 1 and near_start(x, y):
                state = 'circle'
                angle = -math.pi / 2
                tri_index = 0
        else:
            x += speed * dx / dist
            y += speed * dy / dist

    elif state == 'circle':
        x = int(circle_center[0] + circle_rx * math.cos(angle))
        y = int(circle_center[1] + circle_ry * math.sin(angle))
        angle += angle_speed
        # (400, 90)에 도달하면 원운동 종료
        if near_start(x, y) and angle > -math.pi / 2 + 0.1:
            state = 'rect'
            rect_index = 0
            x, y = rect_points[0]

close_canvas()
