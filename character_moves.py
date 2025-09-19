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
moveforward=False
moverbackward=False
angle=4.75

grass.draw_now(400,30)
cha.draw_now(x,y)
while(True):
