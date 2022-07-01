import pygame
import os
import random
from pygame import mixer
pygame.init()

mixer.music.load('Background_song.wav')
mixer.music.play(-1)


pygame.display.set_caption('Muse')

#Variables
collision = mixer.Sound('Explosion_b.wav')
sound = mixer.Sound('Bullet.wav')
Width = 500
Height = 700
Screen = pygame.display.set_mode((Width,Height))
Player_w = 44
Player_h = 44
Asteroids_w = 90
Asteroids_h = 90
Vel = 5
Bullet_vel = 6
Player = pygame.image.load(os.path.join('gun.png'))
Player_size = pygame.transform.scale(Player, (Player_w, Player_h))
Asteroids = pygame.image.load(os.path.join('Asteroids.png'))
Asteroids_size = pygame.transform.scale(Asteroids, (Asteroids_w, Asteroids_h))
White = (255, 255, 255)
background = pygame.transform.scale(pygame.image.load(os.path.join('sky.png')), (Width,Height))

#Functions
def display(player_main, bullets, rocks, enemy, text, textRect, text2, textRect2, text3, textRect3, Lives):
    Screen.blit(background, (0,0))

    for bulletshape in bullets:
        pygame.draw.rect(Screen, White, bulletshape)
    
    for enemy in rocks:
        pygame.draw.rect(Screen, White, enemy)
        Screen.blit(Asteroids_size, (enemy.x - 27, enemy.y - 25))

    Screen.blit(Player_size, (player_main.x, player_main.y))
    Screen.blit(text, textRect)
    Screen.blit(text2, textRect2)

    if Lives == 0:
        Screen.blit(text3, textRect3)

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

def bullet_movement(bullets):
    for bulletshape in bullets:
        bulletshape.y -= Bullet_vel

def main():
    player_main = pygame.Rect(400, Height - 50, Player_w, Player_h)
    bullets = []
    FPS = pygame.time.Clock()
    Lives = 10
    Level = 0
    Score = 0
    rocks = []
    wave_length = 6
    lost = False
    lost_count = 0
    enemy = pygame.Rect(random.randrange(50, Width-100), random.randrange(-500, -100), 5, 10)

    font2 = pygame.font.Font('Spy Agency.ttf', 8)
    text3 = font2.render('Developed By: Mohammed Faizan Murshid - @moham.Faizann', True, (255, 255, 255, 255))
    textRect3 = text3.get_rect()
    textRect3.center = (Width // 2, 650)
    Te = Score
    He = str(Te)
    font = pygame.font.Font('Spy Agency.ttf', 32)
    text2 = font.render('Score:' + He, True, (255, 255, 255, 255))
    textRect2 = text2.get_rect()
    textRect2.center = (410,30)
    
    def Asteroid_movement(rocks):
        for enemy in rocks:
            enemy.y += Level

    run = True
    while run:
        FPS.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if len(rocks) == 0:
                Level += 1
                for i in range(wave_length):
                    enemy = pygame.Rect(random.randrange(50, Width-100), random.randrange(-500, -100), 26, 25)
                    rocks.append(enemy)
                    Screen.blit(Asteroids_size, (enemy.x, enemy.y))
                Asteroid_movement(rocks)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bulletshape = pygame.Rect(player_main.x + player_main.width // 2, player_main.y - player_main.height // 2, 5, 10)
                    bullets.append(bulletshape)
                    sound.play()

        for bulletshape in bullets:
            if bulletshape.y + 680  < Height:
                bullets.remove(bulletshape)
        
        for bulletshape in bullets:
            for enemy in rocks:
                Te = Score
                He = str(Te)
                font = pygame.font.Font('Spy Agency.ttf', 32)
                text2 = font.render('Score:' + He, True, (255, 255, 255, 255))
                textRect2 = text2.get_rect()
                textRect2.center = (410,30)
                collide = pygame.Rect.colliderect(enemy, bulletshape)
                if collide == True:
                    if bulletshape in bullets:
                        bullets.remove(bulletshape)
                    if enemy in rocks:
                        rocks.remove(enemy)
                        collision.play()
                    Score += 1

        for enemy in rocks:
            Xe = Lives
            Ye = str(Xe)
            font = pygame.font.Font('Spy Agency.ttf', 32)
            text = font.render('Lives:' + Ye, True, (255, 255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (80,30)
            if enemy.y + 75 > Height:
                Lives -= 1
                rocks.remove(enemy)
            if Lives < 1:
                if enemy in rocks:
                    rocks.remove(enemy)
                lost = True
                lost_count += 1
                Be = Score
                De = str(Be)
                font = pygame.font.Font('Spy Agency.ttf', 32)
                text2 = font.render('Score:' + De, True, (255, 255, 255, 255))
                textRect2 = text2.get_rect()
                textRect2.center = (Width // 2, Height // 2)
                text3 = font2.render('Developed By: Mohammed Faizan Murshid - @moham.Faizann', True, (255, 255, 255, 255))
                textRect3 = text3.get_rect()
                textRect3.center = (Width // 2, 650)
            if (lost == True) and (lost_count == 300):
                run = False

        Keys = pygame.key.get_pressed()
        movement(Keys, player_main)
        bullet_movement(bullets)
        Asteroid_movement(rocks)
        Screen.fill(0)
        display(player_main, bullets, rocks, enemy, text, textRect, text2, textRect2, text3, textRect3, Lives)

    pygame.quit()

if __name__ == "__main__":
    main()