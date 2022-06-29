import pygame

Width = 500
Height = 500

display = pygame.display.set_mode((Width,Height))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()