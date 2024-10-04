from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('R move.png')
hand_arrow = load_image('hand_arrow.png')

x = TUK_WIDTH/2
y = TUK_HEIGHT/2

def Move_To_Hand(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    frame=0
    global x, y

    for i in range(0, 50,1):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand_arrow.draw(p2[0], p2[1])
        t = i/50
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        if x1<=x2:
            character.clip_draw(frame * 64, 0, 64, 65, x, y, 100,100)
        else:
            character.clip_composite_draw(frame * 64, 0, 64,65,0,'h', x, y,100,100)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)



while True:
    ranvalue = [random.randint(50, 750), random.randint(50, 550)]
    Move_To_Hand((x,y), (random.randint(50, 750), random.randint(50, 550)))





close_canvas()




