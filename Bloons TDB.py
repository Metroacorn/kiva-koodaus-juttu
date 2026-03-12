import pygame

pygame.init()

screen = pygame.display.set_mode((1000,600))

screen.fill((255, 255, 255))

dart_monkeyshop=pygame.Rect(0,0,50,50)
tack_shootershop=pygame.Rect(0,0,50,50)
boomerang_monkeyshop=pygame.Rect(0,0,50,50)

dart_monkeyshop.center=(850,125)
tack_shootershop.center=(850,225)
boomerang_monkeyshop.center=(850,325)

start=pygame.Rect(0,0,50,50)
end=pygame.Rect(0,0,50,50)
start.center=(25,100)
end.center=(625,575)

shop=pygame.Rect(700,0,300,600)

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,(255,0,0),start)
    pygame.draw.rect(screen,(255,0,0),end) 
    pygame.draw.rect(screen,(139, 69, 19),shop)    
    pygame.draw.rect(screen,(0,255,0),dart_monkeyshop)
    pygame.draw.rect(screen,(0,255,0),tack_shootershop)
    pygame.draw.rect(screen,(0,255,0),boomerang_monkeyshop)
    pygame.display.update()

pygame.quit()
