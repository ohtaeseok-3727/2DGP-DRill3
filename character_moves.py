from pico2d import *
import math
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
movesideup=False
movesidedown=False
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
            if x>=770:
                moveforward=False
                movebackward=False
                moveup=True
                movedown=False
        if moveup:
                y+=10
                if y>=550:
                    moveup=False
                    movedown=False
                    moveforward=False
                    movebackward=True
        if movebackward:
            x-=10
            if x<=30:
                moveforward=False
                movebackward=False
                moveup=False
                movedown=True
        if movedown:
            y-=10
            if y<=90:
                moveforward=True
                movebackward=False
                moveup=False
                movedown=False
        if startx==x and starty==y:
            x, y = startx, starty
            moverct = False
            movetrg = True
            moveforward = True
            movebackward = False
            moveup = False
            movedown = False
    delay(0.01)
    if movetrg:
        if moveforward:
            x+=10
            if x>770:
                moveforward=False
                movesideup=True
                movesidedown=False
        if movesideup:
            x-=8
            y+=10
            if y>550:
                movesideup=False
                movesidedown=True
        if movesidedown:
            x-=8
            y-=10
            if y<90:
                movesidedown=False
                moveforward=True
        if startx == x and starty == y:
            movetrg = False
            movecircle = True
            moveforward = False
            movebackward = False
            moveup = False
            movedown = False
    if movecircle:
        