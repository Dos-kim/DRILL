from pico2d import *
import random
import game_world


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
BIRD_SPEED_KMPH = 35.0  # Km / Hour
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x = random.randint(150,1450)
        self.y = random.randint(400,500)
        self.dir = random.randint(0,1)
        self.frame = 0
        self.velocity = 1

    def update(self):
        #비둘기의 속력은 인간보다 약간빠른 약 35km이다
        self.frame = (self.frame + 1) % 14

        if self.dir == 1:
            self.x += self.velocity * BIRD_SPEED_PPS
        else:
            self.x -= self.velocity * BIRD_SPEED_PPS
        if self.x >= 1600:
            self.dir = 0
            self.frame = 0
        elif self.x <= 0:
            self.dir = 1
            self.frame = 0






    def draw(self):
        # boy의 크기가 약 2.2m 라고 가정하고 10pixel당 30cm 라고 가정할때, 새의 크기는 약 80cm라고 생각한다면
        # 새의 크기는 10:30 = x : 80 이므로 80/3 pixel 의 크기가 되므로 26pixel의 좌우 크기를 가질것이다.
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y, 26, 26)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 26, 26)