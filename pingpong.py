from pygame import *

win = display.set_mode((1080 , 720))
clock = time.Clock

class Player():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,50,150)
        self.speed = speed
    def move(self):
        key_list = key.get_pressed()
        if key_list[K_w] == True:
            self.hitbox.y -= self.speed
        if key_list[K_s] == True:
            self.hitbox.y += self.speed
        if self.hitbox.bottom > 720:
            self.hitbox.bottom = 720
        if self.hitbox.top < 0:
            self.hitbox.top = 0

player_1 = Player(50,120,2)

while True:
    win.fill((0,0,0))
    event_list = event.get()
    for e in event_list:
        if e.type == QUIT:
            exit()
    draw.rect(win,(255,255,255),player_1.hitbox)
    player_1.move()
    display.update()