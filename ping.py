from pygame import *
class GameSprite(sprite.Sprite):
   def init(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().init()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

back = (200, 255, 255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PING-PIP")
ball = Player('images.png', 200, 200, 15, 100, 10)
racets1 = Player('fff.png', 30, 200, 15, 100, 150)
racets2 = Player('fff.png', 520, 200, 70, 15, 90, 10)
game = True
finish = False
clock = time.Clock()
FPS = 60



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        ball.update()
        racets1.update()
        racets2.update()

        ball.reset()
        racets1.reset()
        racets2.reset()
    display.update()
    clock.tick(FPS)