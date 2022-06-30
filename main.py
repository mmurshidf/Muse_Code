import pygame
import os
import random

#Variables
Width = 500
Height = 700
Screen = pygame.display.set_mode((Width,Height))
Player_w = 44
Player_h = 44
Asteroids_w = 66
Asteroids_h = 66
Vel = 5
Bullet_vel = 6
Player = pygame.image.load(os.path.join('gun.png'))
Player_size = pygame.transform.scale(Player, (Player_w, Player_h))
Asteroids = pygame.image.load(os.path.join('Asteroids.png'))
Asteroids_size = pygame.transform.scale(Asteroids, (Asteroids_w, Asteroids_h))
White = (255, 255, 255)
background = pygame.transform.scale(pygame.image.load(os.path.join('sky.png')), (Width,Height))

#Functions
def display(player_main, bullets, rocks):
    Screen.blit(background, (0,0))

    for bulletshape in bullets:
        pygame.draw.rect(Screen, White, bulletshape)
    
    for enemy in rocks:
        enemy.draw(Screen)

    Screen.blit(Player_size, (player_main.x, player_main.y))
    
    pygame.display.update()


def movement(Keys, player_main):
    if Keys[pygame.K_a] and player_main.x - Vel > 0:
        player_main.x -= Vel
    if Keys[pygame.K_d] and player_main.x + Vel + player_main.width < 500:
        player_main.x += Vel
    if Keys[pygame.K_RIGHT] and player_main.x + Vel + player_main.width < 500:
        player_main.x += Vel
    if Keys[pygame.K_LEFT] and player_main.x - Vel > 0:
        player_main.x -= Vel

def bullet_movement(bullets,enemy,rocks):
    for bulletshape in bullets:
        bulletshape.y -= Bullet_vel

class Asteroid_class:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.asteroid_img = None
    
    def draw(self, window):
        window.blit(self.asteroid_img, (self.x, self.y))

    def get_width(self):
        return self.asteroid_img.get_width()
    
    def get_height(self):
        return self.asteroid_img.get_height()


class Enemy(Asteroid_class):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.asteroid_img = Asteroids_size
    
    def move(self, vel):
        self.y += vel

def main():
    player_main = pygame.Rect(400, Height - 50, Player_w, Player_h)
    bullets = []
    FPS = pygame.time.Clock()
    level = 0
    Lives = 10
    rocks = []
    wave_length = 6
    
    run = True
    while run:
        FPS.tick(60)

        if len(rocks) == 0:
            level += 1
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, Width-100), random.randrange(-500, -100))
                rocks.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bulletshape = pygame.Rect(player_main.x + player_main.width // 2, player_main.y - player_main.height // 2, 5, 10)
                    bullets.append(bulletshape)
        for enemy in rocks:
            enemy.move(level)
            if enemy.y + enemy.get_height() > Height:
                Lives -= 1
                rocks.remove(enemy)
            if Lives == 0:
                print("end")

        for bulletshape in bullets:
            for enemy in rocks:
                if (enemy.y == bulletshape.y) and (enemy.x == bulletshape.x):
                    bullets.remove(bulletshape)
                    rocks.remove(enemy)

        Keys = pygame.key.get_pressed()
        movement(Keys, player_main)
        bullet_movement(bullets, enemy, rocks)
        Screen.fill(0)
        display(player_main, bullets, rocks)

    pygame.quit()

if __name__ == "__main__":
    main()