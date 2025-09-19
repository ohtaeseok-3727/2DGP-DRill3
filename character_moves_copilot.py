from pico2d import *
import math

open_canvas(800, 600)
grass = load_image('grass.png')
character = load_image('character.png')

# 시작 위치 및 상태 변수
startx, starty = 400, 90
x, y = startx, starty

# 사각형 경로 변수
rect_points = [
    (400, 90), (400, 510), (700, 510), (700, 90), (400, 90)
]
rect_index = 0

# 삼각형 경로 변수
tri_points = [
    (400, 90), (150, 300), (650, 300), (400, 90)
]
tri_index = 0

# 원 경로 변수
angle = 4.75  # 원 시작 각도 (아래쪽)

# 상태 플래그
moverct = True
movetrg = False
movecircle = False

# 이동 속도
speed = 5
angle_speed = 0.05

while True:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)
    get_events()

    if moverct:
        tx, ty = rect_points[rect_index + 1]
        dx, dy = tx - x, ty - y
        dist = math.hypot(dx, dy)
        if dist < speed:
            x, y = tx, ty
            rect_index += 1
            if rect_index == len(rect_points) - 1:
                moverct = False
                movetrg = True
                rect_index = 0
        else:
            x += speed * dx / dist
            y += speed * dy / dist

    elif movetrg:
        tx, ty = tri_points[tri_index + 1]
        dx, dy = tx - x, ty - y
        dist = math.hypot(dx, dy)
        if dist < speed:
            x, y = tx, ty
            tri_index += 1
            if tri_index == len(tri_points) - 1:
                movetrg = False
                movecircle = True
                tri_index = 0
                angle = 4.75
        else:
            x += speed * dx / dist
            y += speed * dy / dist

    elif movecircle:
        x = int(400 + 250 * math.cos(angle))
        y = int(300 + 210 * math.sin(angle))
        angle += angle_speed
        if angle >= 4.75 + 2 * math.pi:
            movecircle = False
            moverct = True
            x, y = startx, starty
            angle = 4.75

close_canvas()

