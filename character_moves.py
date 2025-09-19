from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
cha = load_image('character.png')

startx=400
starty=90
x=startx
y=starty
moverct=True
movecircle=False
movetrg=False
moveup=False
movedown=False
moveforward=True
movebackward=False
angle=4.75

grass.draw_now(400, 30)
cha.draw_now(x, 90)

while(True):
    clear_canvas()
    grass.draw_now(400, 30)
    cha.draw_now(x, y)
    if moverct:
        if moveforward:
            x+=10
            if x>770:
                moveforward=False
                movebackward=False
                moveup=True
                movedown=False
        if moveup:
                y+=10
                if y>550:
                    moveup=False
                    movedown=False
                    moveforward=False
                    movebackward=True
