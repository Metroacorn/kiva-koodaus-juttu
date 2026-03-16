import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1000,600))
grid = [[0 for _ in range(14)] for _ in range(12)]

curway = []

def polku():
    
    start_pos = [2, 0]
    end_pos = [11, 12]

    path = [list(start_pos)]
    visited = set()
    visited.add((start_pos[0], start_pos[1]))
    c = list(start_pos)

    while c != end_pos:
        pm = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for d in directions:
            ny = c[0] + d[0]
            nx = c[1] + d[1]

            if 0 <= ny < 12 and 0 <= nx < 14 and (ny, nx) not in visited:
                
                bo = True
                for cy, cx in [(-1, -1), (-1, 0), (0, -1), (0, 0)]:
                    
                    by, bx = ny + cy, nx + cx
                    if 0 <= by < 11 and 0 <= bx < 13:
                        ok = []
                        for dy2 in range(2):
                            for dx2 in range(2):
                                pos = (by + dy2, bx + dx2)
                                if pos == (ny, nx) or pos in visited:
                                    ok.append(1)
                                else:
                                    ok.append(0)
                        if sum(ok) >= 4:
                            bo = False
                            break
                if bo:
                     
                    weight = 1
                    if d[0] > 0 and ny <= end_pos[0]:
                        weight = 3
                    if d[1] > 0 and nx <= end_pos[1]:
                        weight = 3
                    for _ in range(weight):
                        pm.append([ny, nx])

        if not pm:
            
            if len(path) <= 1:
                path = [list(start_pos)]
                visited = set()
                visited.add((start_pos[0], start_pos[1]))
                c = list(start_pos)
                continue
            path.pop()
            visited.add((c[0], c[1]))
            c = list(path[-1])
            continue

        next_pos = random.choice(pm)
        c = next_pos
        visited.add((c[0], c[1]))
        path.append(list(c))
        
    return path

curway=polku()
screen.fill((255, 255, 255))

def background():
    pygame.draw.rect(screen,(139, 69, 19),shop)    
    pygame.draw.rect(screen,(0,255,0),dart_monkeyshop)
    pygame.draw.rect(screen,(0,255,0),tack_shootershop)
    pygame.draw.rect(screen,(0,255,0),boomerang_monkeyshop)
    pygame.draw.rect(screen,(0,255,0),banana_farmshop)
    pygame.draw.rect(screen,(0,255,0),sniper_monkeyshop)
    

def dart_monkeyplace():
    screen.fill((255,255,255))
    background()
    
    dartx,darty = pygame.mouse.get_pos()
    
    
    pygame.draw.circle(screen,(211,211,211),(dartx,darty),dartrange)
    
    
    for i in dart_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    
    
    pygame.draw.circle(screen,(0,0,0),(dartx,darty),25)
    
    dart_monkeyhit=pygame.Rect(0,0,45,45)
    dart_monkeyhit.center=(dartx,darty)
    
    for i in dart_monkeyshit:
        pygame.draw.rect(screen,(255,0,0),i)

def dart_monkeyplaced():
    dartshoot=[dartrange,(dartstayx,dartstayy),(211,211,211)]
    
    dart_monkeyshootbox.append(dartshoot)
    
    d=[25,(dartstayx,dartstayy),(0,0,0)]
    
    dart_monkeys.append(d)
    for i in range(len(dart_monkeys)):
        dart_monkeyhit=pygame.Rect(0,0,45,45)
        dart_monkeyhit.center=(dartstayx,dartstayy)
        dart_monkeyshit.append(dart_monkeyhit)
    for i in dart_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in dart_monkeyshit:
        pygame.draw.rect(screen,(255,0,0),i)
        
    
    
    
    pygame.draw.rect(screen,(255,0,0),dart_monkeyhit)

def boomerang_monkeyplace():
    screen.fill((255,255,255))
    background()
    boomx, boomy= pygame.mouse.get_pos()
    
    pygame.draw.circle(screen,(211,211,211),(boomx,boomy),boomrange)
    
    for i in boomerang_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    pygame.draw.circle(screen,(0,0,0),(boomx,boomy),25)
    
    boomhit=pygame.Rect(0,0,45,45)
    boomhit.center=(boomx,boomy)
    
    pygame.draw.rect(screen,(255,0,0),boomhit)
    

    
    for i in boomerang_monkeyhit:
        pygame.draw.rect(screen,(255,0,0),i)
    

def boomerang_monkeyplaced():
    boomshoot=[boomrange,(boomstayx,boomstayy),(211,211,211)]
    
    boomerang_monkeyshootbox.append(boomshoot)
    
    d=[25,(boomstayx,boomstayy),(0,0,0)]
    
    boomerang_monkeys.append(d)
    for i in range(len(boomerang_monkeys)):
        boomerang_monkeyshit=pygame.Rect(0,0,45,45)
        boomerang_monkeyshit.center=(boomstayx,boomstayy)
        boomerang_monkeyhit.append(boomerang_monkeyshit)
    
    for i in boomerang_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in boomerang_monkeyhit:
        pygame.draw.rect(screen,(255,0,0),i)

def tack_shooterplace():
    screen.fill((255,255,255))
    background()
    
    tackx,tacky = pygame.mouse.get_pos()
    
    
    pygame.draw.circle(screen,(211,211,211),(tackx,tacky),tackrange)
    
    
    for i in tack_shooters:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    
    
    pygame.draw.circle(screen,(0,0,0),(tackx,tacky),25)
    
    tack_shooterhit=pygame.Rect(0,0,45,45)
    tack_shooterhit.center=(tackx,tacky)
    
    for i in tack_shootershit:
        pygame.draw.rect(screen,(255,0,0),i)

def tack_shooterplaced():
    tackshoot=[tackrange,(tackstayx,tackstayy),(211,211,211)]
    
    tack_shootershootbox.append(tackshoot)
    
    d=[25,(tackstayx,tackstayy),(0,0,0)]
    
    tack_shooters.append(d)
    for i in range(len(tack_shooters)):
        tack_shooterhit=pygame.Rect(0,0,45,45)
        tack_shooterhit.center=(tackstayx,tackstayy)
        tack_shootershit.append(tack_shooterhit)
    for i in tack_shooters:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in tack_shootershit:
        pygame.draw.rect(screen,(255,0,0),i)
        
    
def sniper_monkeyplace():
   screen.fill((255,255,255))
   background()
    
   snipex,snipey = pygame.mouse.get_pos()
    
    
   pygame.draw.circle(screen,(211,211,211),(snipex,snipey),sniperange)
    
    
   for i in sniper_monkeys:
       pygame.draw.circle(screen,i[2],i[1],i[0])
    
    
    
   pygame.draw.circle(screen,(0,0,0),(snipex,snipey),25)
    
   sniper_monkeyhit=pygame.Rect(0,0,45,45)
   sniper_monkeyhit.center=(snipex,snipey)
    
   for i in sniper_monkeyshit:
       pygame.draw.rect(screen,(255,0,0),i)

def sniper_monkeyplaced():
    
    snipeshoot=[sniperange,(snipestayx,snipestayy),(211,211,211)]
    
    sniper_monkeyshootbox.append(snipeshoot)
    
    d=[25,(snipestayx,snipestayy),(0,0,0)]
    
    sniper_monkeys.append(d)
    for i in range(len(sniper_monkeys)):
        sniper_monkeyhit=pygame.Rect(0,0,45,45)
        sniper_monkeyhit.center=(snipestayx,snipestayy)
        sniper_monkeyshit.append(sniper_monkeyhit)
    for i in sniper_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in sniper_monkeyshit:
        pygame.draw.rect(screen,(255,0,0),i)   
   
    pygame.draw.rect(screen,(255,0,0),sniper_monkeyhit) 

def banana_farmplace():
    screen.fill((255,255,255))
    background()
     
    bananax,bananay = pygame.mouse.get_pos()
     
     
    pygame.draw.circle(screen,(211,211,211),(bananax,bananay),bananarange)
     
     
    for i in banana_farms:
        pygame.draw.circle(screen,i[2],i[1],i[0])
     
     
     
    pygame.draw.circle(screen,(0,0,0),(bananax,bananay),25)
     
    banana_farmhit=pygame.Rect(0,0,45,45)
    banana_farmhit.center=(bananax,bananay)
     
    for i in banana_farmshit:
        pygame.draw.rect(screen,(255,0,0),i)
     

def draw_monkeys():
    #dartmonkey
    for i in range(len(dart_monkeys)):
        dart_monkeyhit=pygame.Rect(0,0,45,45)
        dart_monkeyhit.center=(dartstayx,dartstayy)
        dart_monkeyshit.append(dart_monkeyhit)
    for i in dart_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in dart_monkeyshit:
        pygame.draw.rect(screen,(255,0,0),i)
    
    #boomerangmonkey
    for i in range(len(boomerang_monkeys)):
        boomerang_monkeyshit=pygame.Rect(0,0,45,45)
        boomerang_monkeyshit.center=(boomstayx,boomstayy)
        boomerang_monkeyhit.append(boomerang_monkeyshit)
    
    for i in boomerang_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in boomerang_monkeyhit:
        pygame.draw.rect(screen,(255,0,0),i)
    
    #tackshooter
    for i in range(len(tack_shooters)):
        tack_shooterhit=pygame.Rect(0,0,45,45)
        tack_shooterhit.center=(tackstayx,tackstayy)
        tack_shootershit.append(tack_shooterhit)
    for i in tack_shooters:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in tack_shootershit:
        pygame.draw.rect(screen,(255,0,0),i)
    
    #snipermonkey
    for i in range(len(sniper_monkeys)):
        sniper_monkeyhit=pygame.Rect(0,0,45,45)
        sniper_monkeyhit.center=(snipestayx,snipestayy)
        sniper_monkeyshit.append(sniper_monkeyhit)
    for i in sniper_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in sniper_monkeyshit:
        pygame.draw.rect(screen,(255,0,0),i)   

    
dart_monkeys=[]
dart_monkeyshit=[]
dart_monkeyshootbox=[]  

boomerang_monkeys=[]
boomerang_monkeyhit=[]
boomerang_monkeyshootbox=[]

tack_shooters=[]
tack_shootershit=[]
tack_shootershootbox=[]

banana_farms=[]
banana_farmshit=[]

sniper_monkeys=[]
sniper_monkeyshit=[]
sniper_monkeyshootbox=[]

dart_monkeyhit=pygame.Rect(0,0,25,25)


dart_monkeyshop=pygame.Rect(0,0,50,50)
tack_shootershop=pygame.Rect(0,0,50,50)
boomerang_monkeyshop=pygame.Rect(0,0,50,50)
banana_farmshop=pygame.Rect(0,0,50,50)
sniper_monkeyshop=pygame.Rect(0,0,50,50)

dart_monkeyshop.center=(800,125)
tack_shootershop.center=(800,225)
boomerang_monkeyshop.center=(800,325)
banana_farmshop.center=(900,125)
sniper_monkeyshop.center=(900,225)

playarea=pygame.Rect(0,0,700,600)

start=pygame.Rect(0,0,50,50)
end=pygame.Rect(0,0,50,50)
start.center=(25,125)
end.center=(625,575)

shop=pygame.Rect(700,0,300,600)

pygame.display.update()

dartrange=125
boomrange=150
tackrange=75
sniperange=600
bananarange=50

sniper_monkeybought=False
sniperplaced=False
tack_shooterbought=False
tackplaced=False
boomerang_monkeybought=False
boomplaced=False
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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boomerang_monkeyshop.collidepoint(event.pos):
                boomerang_monkeybought=True
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and boomerang_monkeybought:
            boomerang_monkeybought=False
            boomstayx, boomstayy=pygame.mouse.get_pos()
            boomplaced=True
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tack_shootershop.collidepoint(event.pos):
                tack_shooterbought=True
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and tack_shooterbought:
            tack_shooterbought=False
            tackstayx, tackstayy=pygame.mouse.get_pos()
            tackplaced=True
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sniper_monkeyshop.collidepoint(event.pos):
                sniper_monkeybought=True
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and sniper_monkeybought:
            sniper_monkeybought=False
            snipestayx, snipestayy=pygame.mouse.get_pos()
            sniperplaced=True
        
            
    mousex, mousey=pygame.mouse.get_pos()
    
    
    if dart_monkeybought:
        if playarea.collidepoint(mousex,mousey):
            dart_monkeyplace()
    if dartplaced:
        dart_monkeyplaced()
        dartplaced=False
        
    if boomerang_monkeybought:
        if playarea.collidepoint(mousex,mousey):
            boomerang_monkeyplace()
    if boomplaced:
        boomerang_monkeyplaced()
        boomplaced=False
    
    if tack_shooterbought:
        if playarea.collidepoint(mousex,mousey):
            tack_shooterplace()
    if tackplaced:
        tack_shooterplaced()
        tackplaced=False
    
    if sniper_monkeybought:
        if playarea.collidepoint(mousex,mousey):
            sniper_monkeyplace()
    
    if sniperplaced:
        sniper_monkeyplaced()
        sniperplaced=False
    for pos in curway:
        rect = pygame.Rect(pos[1] * 50, pos[0] * 50, 50, 50)
        pygame.draw.rect(screen, (211, 211, 211), rect)
        pygame.draw.rect(screen, (200, 211, 0), rect, 1)    
    draw_monkeys()       
    background()
    pygame.display.update()

pygame.quit()
