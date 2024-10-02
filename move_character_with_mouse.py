from pico2d import*
import random

TUK_GROUND_WIDTH, TUK_GROUND_HEIGHT = 1280, 1024
open_canvas(1280,1024)

tuk_ground = load_image('TUK_GROUND.png')
arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

x, y = (TUK_GROUND_WIDTH // 2, TUK_GROUND_HEIGHT // 2) #소년위치
x2, y2 = random.randint(0,1280), random.randint(0,1024) #손가락 위치

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

frame = 0

running = True
while running:

    x1, y1 = x, y

    for i in range(0, 100, 2):
        tuk_ground.draw(TUK_GROUND_WIDTH // 2, TUK_GROUND_HEIGHT // 2 )
        t = i /100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        if x2 < x1:              #자를 위치 #자를 위치 #자를 크기 #그릴 위치
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)

        arrow.draw(x2, y2)
        frame = (frame + 1) % 8
        delay(0.05)
        handle_events()
        update_canvas()

    x2, y2 = random.randint(0,1280), random.randint(0,1024)



