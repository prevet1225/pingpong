from pygame import *

win = display.set_mode((1080 , 720))
clock = time.Clock()

class Player():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,30,150)
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
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = ball.speed
    def aoutopilot(self):
        self.hitbox.y = ball.hitbox.y
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = -ball.speed

class Ball():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,34,34)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
    def move(self):
        self.hitbox.x += self.speed_x
        self.hitbox.y += self.speed_y
        if self.hitbox.top < 0:
            self.speed_y = self.speed
        if self.hitbox.bottom > 720:
            self.speed_y = -self.speed
        if self.hitbox.left < 0:
            self.speed_x = self.speed
            self.hitbox.center = (540, 360)
            time.wait(3000)
        if self.hitbox.right > 1080:
            self.speed_x = -self.speed

player_1 = Player(50, 240, 7)
player_2 = Player(1030,240,1)
ball = Ball(340,260,5)

while True:
    win.fill((0,0,0))
    event_list = event.get()
    for e in event_list:
        if e.type == QUIT:
            exit()
    draw.rect(win,(255,255,255),player_1.hitbox)
    player_1.move()
    draw.rect(win,(255,255,255),player_2.hitbox)
    player_2.aoutopilot()
    draw.rect(win,(255,255,255),ball.hitbox)
    ball.move()
    clock.tick(60)
    display.update()