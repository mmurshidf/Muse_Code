import pygame
import os

#Variables
Width = 500
Height = 700
Win = pygame.display.set_mode((Width,Height))
Player_w = 33
Player_h = 33
Vel = 5
Bullet_vel = 6
Player = pygame.image.load(os.path.join('Ria.png'))
Player_size = pygame.transform.scale(Player, (Player_w, Player_h))
White = (255, 255, 255)
background = pygame.transform.scale(pygame.image.load(os.path.join('sky1.png')), (Width,Height))

#Functions
def display(player_main, bullets):
    Win.blit(background, (0,0))
    for bulletshape in bullets:
        pygame.draw.rect(Win, White, bulletshape)

    Win.blit(Player_size, (player_main.x, player_main.y))
    
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
    run = True
    while run:
        FPS.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bulletshape = pygame.Rect(player_main.x + player_main.width // 2, player_main.y - player_main.height // 2, 5, 10)
                    bullets.append(bulletshape)

        Keys = pygame.key.get_pressed()
        movement(Keys, player_main)
        bullet_movement(bullets)
        Win.fill(0)
        display(player_main, bullets)

    pygame.quit()

if __name__ == "__main__":
    main()