import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

screen.fill((255, 255, 255))

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        running = False

pygame.quit()
