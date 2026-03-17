import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
grid = [[0 for _ in range(14)] for _ in range(12)]
c_v=1
curway = []
#hp
red_hp=1
blue_hp=3
green_hp=7
yellow_hp=11
purple_hp=16
p_hp=100
#dmg
red_dmg=1
blue_dmg=4
green_dmg=8
yellow_dmg=13
purple_dmg=20
#points
red_p=2
blue_p=6
green_p=9
yellow_p=14
purple_p=20
#speeds
red_s=1
blue_s=1.5
green_s=1.7
yellow_s=2.4
purple_s=3


h_v=5
wave_points=100
spawn_queue=[]    
active_enemies=[]  
last_spawn_time=0
SPAWN_DELAY=500   
red=[]
blue=[]
blue.append((0, 0, 255))
blue.append(blue_dmg)
blue.append(blue_hp)
green=[]
green.append((0, 255, 0))
green.append(green_dmg)
green.append(green_hp)
yellow=[]
yellow.append((255, 255, 0))
yellow.append(yellow_dmg)
yellow.append(yellow_hp)
purple=[]
purple.append((128, 0, 128))
purple.append(purple_dmg)
purple.append(purple_hp)

red.append((255, 0, 0))
red.append(red_dmg)
red.append(red_hp)



red_c=[]
blue_c=[]
green_c=[]
yellow_c=[]
purple_c=[]


for i in range(1,1000):
    if i<35:
        red_c.append(i)
    if i<70 and i>20:
        blue_c.append(i)
    if i<140 and i>60:
        green_c.append(i)
    if i<230 and i>100:
        yellow_c.append(i)
    if i>200:
        purple_c.append(i)

def waves(wave_points, h_v, c_v):
    
    wave_list=[]
    start_x = curway[0][1] * 50 + 25
    start_y = curway[0][0] * 50 + 25
    while wave_points>2:
        ok=random.randint(1,20+h_v)
        if ok in red_c:
            wave_list.append([red[0],red[1],red[2],[start_x,start_y],red_s,1])
            wave_points-=red_p
        if ok in blue_c:
            wave_list.append([blue[0],blue[1],blue[2],[start_x,start_y],blue_s,1])
            wave_points-=blue_p
        if ok in green_c:
            wave_list.append([green[0],green[1],green[2],[start_x,start_y],green_s,1])
            wave_points-=green_p
        if ok in yellow_c:
            wave_list.append([yellow[0],yellow[1],yellow[2],[start_x,start_y],yellow_s,1])
            wave_points-=yellow_p
        if ok in purple_c:
            wave_list.append([purple[0],purple[1],purple[2],[start_x,start_y],purple_s,1])
            wave_points-=purple_p
        if ok > 1000:
            wave_list.append([purple[0],purple[1],purple[2],[start_x,start_y],purple_s,1])
            wave_points-=purple_p
    return wave_list
            
    
    

def polku():
    
    start_pos = [2, 0]
    end_pos = [11, 12]
    
    best_path = None
    best_length = 0
    
    for attempt in range(15):
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
                        
                        if d[0] < 0 and ny >= 1:
                            weight = 3
                        if d[1] < 0 and nx >= 1:
                            weight = 2
                        
                        if len(path) > 20:
                            if d[0] > 0 and ny <= end_pos[0]:
                                weight = 4
                            if d[1] > 0 and nx <= end_pos[1]:
                                weight = 4
                        
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
        
        if len(path) > best_length:
            best_length = len(path)
            best_path = path
    
    return best_path

curway=polku()
screen.fill((255, 255, 255))

def background():
    pygame.draw.rect(screen,(139, 69, 19),shop)    
    pygame.draw.rect(screen,(0,255,0),dart_monkeyshop)
    pygame.draw.rect(screen,(0,255,0),tack_shootershop)
    pygame.draw.rect(screen,(0,255,0),boomerang_monkeyshop)
    pygame.draw.rect(screen,(0,255,0),banana_farmshop)
    pygame.draw.rect(screen,(0,255,0),sniper_monkeyshop)
    
    moneytext=font.render(f"Money:{money}",True,(0,0,0))
    
    screen.blit(moneytext,(10,10))

    
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
    
    tack_shootercooldowns.append(tackcooldown)
    
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
    
    sniper_monkeycooldowns.append(snipecooldown)
    
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

def banana_farmplaced():
     bananashoot=[bananarange,(bananastayx,bananastayy),(211,211,211)]
     
     banana_farmshootbox.append(bananashoot)
     
     d=[25,(bananastayx,bananastayy),(0,0,0)]
     
     banana_farmcooldowns.append(bananacooldown)
     
     banana_farms.append(d)
     for i in range(len(banana_farms)):
         banana_farmhit=pygame.Rect(0,0,45,45)
         banana_farmhit.center=(bananastayx,bananastayy)
         banana_farmshit.append(banana_farmhit)
     for i in banana_farms:
         pygame.draw.circle(screen,i[2],i[1],i[0])
     
     for i in banana_farmshit:
         pygame.draw.rect(screen,(255,0,0),i)   
    
     pygame.draw.rect(screen,(255,0,0),banana_farmhit)

def banana_farmfarm(x):
    banana_farmcooldowns[x]-=1
    if banana_farmcooldowns[x]==0:
        banana_farmcooldowns[x]=bananacooldown
        spawnbanana(x)

def spawnbanana(i):
    cx, cy=banana_farmshootbox[i][1]
    r=bananarange
    
    angle=random.uniform(0,2 * math.pi)
    
    x=cx+r*math.cos(angle)
    y=cy+r*math.sin(angle)
    
    bananahit=pygame.Rect(0,0,10,10)
    bananahit.center=(x,y)
    
    bananashit.append(bananahit)
    
    banana=[7,(x,y),(255,0,0)]
    
    bananas.append(banana)

def dart_monkeyshoot(i,balloonx,balloony):
    
    if dart_monkeycooldowns[i]==0:
        dart_monkeycooldowns[i]=dartcooldown
        
        x,y=dart_monkeyshit[i].center
            
        dartbullet(x,y,balloonx,balloony)


def dartbullet(x,y,balloonx,balloony):
    dx=balloonx-x
    dy=balloony-y
    
    distance=math.sqrt(dx**2+dy**2)
    
    if distance !=0:
        dx /= distance
        dy /= distance
    
    speed=5
    
    darts.append([x,y,dx,dy,speed])
    
    
    
    
    
    
    
    
    

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
    
    #bananafarm
    for i in range(len(banana_farms)):
        banana_farmhit=pygame.Rect(0,0,45,45)
        banana_farmhit.center=(bananastayx,bananastayy)
        banana_farmshit.append(banana_farmhit)
    for i in banana_farms:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in banana_farmshit:
        pygame.draw.rect(screen,(255,0,0),i)  
    
    for i in bananas:
        pygame.draw.circle(screen,i[2],i[1],i[0])
        
        
font=pygame.font.SysFont(None,36)

dart_monkeys=[]
dart_monkeyshit=[]
dart_monkeyshootbox=[] 
dart_monkeycooldowns=[]
darts=[]
 

boomerang_monkeys=[]
boomerang_monkeyhit=[]
boomerang_monkeyshootbox=[]
boomerang_monkeycooldowns=[]

tack_shooters=[]
tack_shootershit=[]
tack_shootershootbox=[]
tack_shootercooldowns=[]

banana_farms=[]
banana_farmshit=[]
banana_farmshootbox=[]
banana_farmcooldowns=[]
bananas=[]
bananashit=[]

sniper_monkeys=[]
sniper_monkeyshit=[]
sniper_monkeyshootbox=[]
sniper_monkeycooldowns=[]

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
spawn_queue=[]    
active_enemies=[]  
last_spawn_time=0
SPAWN_DELAY=500
start=pygame.Rect(0,0,50,50)
end=pygame.Rect(0,0,50,50)
start.center=(25,125)
end.center=(625,575)

shop=pygame.Rect(700,0,300,600)

pygame.display.update()

money=250

dartrange=125
boomrange=150
tackrange=75
sniperange=600
bananarange=50

dartcost=50
boomcost=150
tackcost=100
snipercost=500
bananacost=1000

bananacooldown=600
dartcooldown=30
boomcooldown=120
snipecooldown=180
tackcooldown=60

banana_farmbought=False
bananaplaced=False
sniper_monkeybought=False
sniperplaced=False
tack_shooterbought=False
tackplaced=False
boomerang_monkeybought=False
boomplaced=False
dartplaced=False
dart_monkeybought=False
running = True

while running and p_hp>0:
    screen.fill((255,255,255))
    clock.tick(60)
    
    if len(spawn_queue)==0 and len(active_enemies)==0:
        
        spawn_queue=waves(wave_points, h_v, c_v)
        c_v+=1
        h_v=h_v+c_v*2
        wave_points+=wave_points*0.5
    
    current_time = pygame.time.get_ticks()
    if len(spawn_queue) > 0 and current_time - last_spawn_time >= SPAWN_DELAY:
        active_enemies.append(spawn_queue.pop(0))
        last_spawn_time = current_time



    
    dartoverlap=False
    boomoverlap=False
    tackoverlap=False
    snipeoverlap=False
    bananaoverlap=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dart_monkeyshop.collidepoint(event.pos):
                if money>=dartcost:    
                    dart_monkeybought=True
                    money-=dartcost
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and dart_monkeybought:
            mousex, mousey=pygame.mouse.get_pos()
            for i in curway:
                if mousey//50==i[0] and mousex//50==i[1]:
                    dartoverlap=True
            if not dartoverlap:    
                dart_monkeybought=False
                dartstayx, dartstayy=pygame.mouse.get_pos()
                dartplaced=True
            
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boomerang_monkeyshop.collidepoint(event.pos):
                if money>=boomcost:
                    boomerang_monkeybought=True
                    money-=boomcost
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and boomerang_monkeybought:
            mousex, mousey=pygame.mouse.get_pos()
            for i in curway:
                if mousey//50==i[0] and mousex//50==i[1]:
                    boomoverlap=True
                
            if not boomoverlap:
                boomerang_monkeybought=False
                boomstayx, boomstayy=pygame.mouse.get_pos()
                boomplaced=True
                
            
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tack_shootershop.collidepoint(event.pos):
                if money>=tackcost:
                    
                    tack_shooterbought=True
                    money-=tackcost
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and tack_shooterbought:
            mousex, mousey=pygame.mouse.get_pos()
            for i in curway:
                if mousey//50==i[0] and mousex//50==i[1]:
                    tackoverlap=True
                
            if not tackoverlap:
                tack_shooterbought=False
                tackstayx, tackstayy=pygame.mouse.get_pos()
                tackplaced=True
            
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sniper_monkeyshop.collidepoint(event.pos):
                if money>=snipercost:
                    
                    sniper_monkeybought=True
                    money-=snipercost
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and sniper_monkeybought:
            mousex, mousey=pygame.mouse.get_pos()
            for i in curway:
                if mousey//50==i[0] and mousex//50==i[1]:
                    snipeoverlap=True
            
            if not snipeoverlap:
                sniper_monkeybought=False
                snipestayx, snipestayy=pygame.mouse.get_pos()
                sniperplaced=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if banana_farmshop.collidepoint(event.pos):
                if money>=bananacost:
                    
                    banana_farmbought=True
                    money-=bananacost
        if event.type == pygame.MOUSEBUTTONDOWN and playarea.collidepoint(event.pos) and banana_farmbought:
            mousex, mousey = pygame.mouse.get_pos()
            for i in curway:
                if mousey//50==i[0] and mousex//50 == i[1]:
                    bananaoverlap=True
            
            if not bananaoverlap:
                banana_farmbought=False
                bananastayx, bananastayy = pygame.mouse.get_pos()
                bananaplaced=True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(bananashit)):
                if bananashit[i-1].collidepoint(event.pos):
                    bananashit.pop(i-1)
                    bananas.pop(i-1)
                    money+=10
                    
        
            
    mousex, mousey=pygame.mouse.get_pos()
    
    
    if dart_monkeybought:
        if playarea.collidepoint(mousex,mousey):
            dart_monkeyplace()
    if dartplaced:
        dart_monkeyplaced()
        dartplaced=False
    
    for i in active_enemies:
        for n in range(len(dart_monkeys)):
            dart_monkeyshoot(n,i)
    
        
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
    
    if banana_farmbought:
        if playarea.collidepoint(mousex, mousey):
            banana_farmplace()
    
    if bananaplaced:
        banana_farmplaced()
        bananaplaced=False
    
    for i in range(len(banana_farms)):
        banana_farmfarm(i)
    
    if len(bananas)>100:
        bananas.pop(0)
        bananashit.pop(0)
    for pos in curway:
        rect = pygame.Rect(pos[1] * 50, pos[0] * 50, 50, 50)
        pygame.draw.rect(screen, (211, 211, 211), rect)
        pygame.draw.rect(screen, (200, 211, 0), rect, 1)    

    for i in active_enemies:
        pygame.draw.circle(screen, i[0], (int(i[3][0]), int(i[3][1])), 20)
    
    # Movement system
    for enemy in active_enemies[:]:
        if enemy[5] >= len(curway):
            p_hp -= enemy[1]
            active_enemies.remove(enemy)
            continue

        target = curway[enemy[5]]
        tx = target[1] * 50 + 25
        ty = target[0] * 50 + 25

        dx = tx - enemy[3][0]
        dy = ty - enemy[3][1]
        dist = (dx**2 + dy**2) ** 0.5

        if dist <= enemy[4]:
            enemy[3][0] = tx
            enemy[3][1] = ty
            enemy[5] += 1
        elif dist > 0:
            enemy[3][0] += enemy[4] * dx / dist
            enemy[3][1] += enemy[4] * dy / dist
    draw_monkeys()       
    background()
    pygame.display.update()

pygame.quit()
