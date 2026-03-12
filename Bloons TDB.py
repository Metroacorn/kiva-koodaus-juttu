import pygame

pygame.init()

screen = pygame.display.set_mode((1000,600))

screen.fill((255, 255, 255))

start=pygame.Rect(0,0,50,50)
end=pygame.Rect(0,0,50,50)
start.center=(25,100)
end.center=(550,575)

shop=pygame.Rect(600,0,400,600)

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,(255,0,0),start)
    pygame.draw.rect(screen,(255,0,0),end) 
    pygame.draw.rect(screen,(255,0,0),shop)    
    pygame.display.update()

pygame.quit()
