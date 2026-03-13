import pygame

pygame.init()

screen = pygame.display.set_mode((1000,600))

screen.fill((255, 255, 255))

def background():
    pygame.draw.rect(screen,(255,0,0),start)
    pygame.draw.rect(screen,(255,0,0),end) 
    pygame.draw.rect(screen,(139, 69, 19),shop)    
    pygame.draw.rect(screen,(0,255,0),dart_monkeyshop)
    pygame.draw.rect(screen,(0,255,0),tack_shootershop)
    pygame.draw.rect(screen,(0,255,0),boomerang_monkeyshop)

def dart_monkeyplace():
    screen.fill((255,255,255))
    background()
    
    dartx,darty = pygame.mouse.get_pos()
    
    
    
    pygame.draw.circle(screen,(0,0,0),(dartx,darty),25)
    
    dart_monkeyhit=pygame.Rect(0,0,45,45)
    dart_monkeyhit.center=(dartx,darty)
    
    pygame.draw.rect(screen,(255,0,0),dart_monkeyhit)

def dart_monkeyplaced():
    pygame.draw.circle(screen,(0,0,0), (dartstayx,dartstayy),25)
    dart_monkeyhit=pygame.Rect(0,0,45,45)
    dart_monkeyhit.center=(dartstayx,dartstayy)
    
    pygame.draw.rect(screen,(255,0,0),dart_monkeyhit)

    
dart_monkeysamount=1
    
dart_monkeys=[[]*dart_monkeysamount]
dart_monkeyshootbox=[[]*dart_monkeysamount]  

dart_monkeyhit=pygame.Rect(0,0,25,25)


dart_monkeyshop=pygame.Rect(0,0,50,50)
tack_shootershop=pygame.Rect(0,0,50,50)
boomerang_monkeyshop=pygame.Rect(0,0,50,50)

dart_monkeyshop.center=(850,125)
tack_shootershop.center=(850,225)
boomerang_monkeyshop.center=(850,325)

playarea=pygame.Rect(0,0,700,600)

start=pygame.Rect(0,0,50,50)
end=pygame.Rect(0,0,50,50)
start.center=(25,100)
end.center=(625,575)

shop=pygame.Rect(700,0,300,600)

pygame.display.update()
dartplaced=False
dart_monkeybought=False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dart_monkeyshop.collidepoint(event.pos):
                dart_monkeybought=True
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and dart_monkeybought:
            dart_monkeybought=False
            dartstayx, dartstayy=pygame.mouse.get_pos()
            dartplaced=True
        
            
    mousex, mousey=pygame.mouse.get_pos()
    
    
    if dart_monkeybought:
        if playarea.collidepoint(mousex,mousey):
            dart_monkeyplace()
    if dartplaced:
        dart_monkeyplaced()
        dartplaced=False
        
            
    background()
    pygame.display.update()

pygame.quit()
