from pico2d import *
import math

from pico2d import close_canvas

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
        if abs(startx - x) < 10 and abs(starty - y) < 10:
            x, y = startx, starty
            moverct = False
            movetrg = True
            moveforward = True
            movebackward = False
            moveup = False
            movedown = False
    if movetrg:
        if moveforward:
            x+=10
            if x>=770:
                moveforward=False
                movesideup=True
                movesidedown=False
        if movesideup:
            x-=8
            y+=10
            if y>=550:
                movesideup=False
                movesidedown=True
        if movesidedown:
            x-=8
            y-=10
            if y<=90:
                movesidedown=False
                moveforward=True
        if abs(startx - x) < 10 and abs(starty - y) < 10:
            x, y= startx, starty
            movetrg = False
            movecircle = True
            moveforward = False
            movebackward = False
            moveup = False
            movedown = False
    if movecircle:
        x=int(400+250*math.cos(angle))
        y=int(340+250*math.sin(angle))
        angle+=0.05
        if angle>=4.75+2*math.pi:
            movecircle=False
            moverct=True
            x=startx
            y=starty
            moveforward=True
            movebackward=False
            moveup=False
            movedown=False
            angle=4.75
    delay(0.01)
close_canvas()