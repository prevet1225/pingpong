from pygame import *
from random import *
win = display.set_mode((1080 , 720))
clock = time.Clock()

init()

image_generator = font.Font(None,50)


class Player():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,30,150)
        self.speed = speed
        self.score = 0
        self.score_img = image_generator.render(str(self.score),True,(0,0,0),(255,255,255))


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
            ball.random_x = randint(1,5)
            ball.random_y = randint(1,5)
    def autopilot(self):
        if ball.hitbox.centery < self.hitbox.centery:
            self.hitbox.y -= self.speed
        else:
            self.hitbox.y += self.speed
                
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = -ball.speed
class Ball():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,34,34)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        self.random_x = 1
        self.random_y = 1
    def move(self):
        self.hitbox.x += self.speed_x * self.random_x #/ randint(1,4)
        self.hitbox.y += self.speed_y * self.random_y #/ randint(1,4)
        if self.hitbox.top < 0:
            self.speed_y = self.speed
        if self.hitbox.bottom > 720:
            self.speed_y = -self.speed
        if self.hitbox.left < 0:
            self.speed_x = self.speed
            self.hitbox.center = (540, 360)
            
            time.wait(1000)
            player_2.score += 1
            player_2.score_img = image_generator.render(str(player_2.score),True,(0,0,0),(255,255,255))
            self.random_x =1
            self.random_y =1
        if self.hitbox.right > 1080:
            self.speed_x = -self.speed
            player_1.score += 1
            player_1.score_img = image_generator.render(str(player_1.score),True,(0,0,0),(255,255,255))
            self.hitbox.center = (540, 360)
            time.wait(1000)
            self.random_x =1
            self.random_y =1

player_1 = Player(50, 240, 7)
player_2 = Player(1030,240,5)
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
    player_2.autopilot()
    draw.rect(win,(255,255,255),ball.hitbox)
    ball.move()
    win.blit(player_1.score_img,(20,20))
    win.blit(player_2.score_img,(1040,20))
    clock.tick(60)
    display.update()