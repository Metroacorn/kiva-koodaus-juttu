import pygame
import random
import math
pygame.init()






def pop(arvo, pallo):
    if arvo == 0:
        active_enemies.remove(pallo)
    else:
        active_enemies.remove(pallo)
        arvo -= 1

        p1 = pallo[3][:]
        p2 = pallo[3][:]

        if pallo[5] >= 1:
            pw = curway[pallo[5] - 1]
            px = pw[1] * 50 + 25
            py = pw[0] * 50 + 25
            dx = px - p2[0]
            dy = py - p2[1]
            dist = (dx**2 + dy**2) ** 0.5
            if dist > 0:
                offset = 30  
                p2[0] += offset * dx / dist
                p2[1] += offset * dy / dist
        if arvo>=10:
            for i in range(4):
                active_enemies.append([arvot[arvo][0], arvot[arvo][1], arvot[arvo][2], p1, arvot[arvo-1][-1], pallo[5], pallo[6]-1, pallo[7]**i+2])
        else:
            active_enemies.append([arvot[arvo][0], arvot[arvo][1], arvot[arvo][2], p1, arvot[arvo-1][-1], pallo[5], pallo[6]-1, pallo[7]**4])
            active_enemies.append([arvot[arvo][0], arvot[arvo][1], arvot[arvo][2], p2, arvot[arvo-1][-1], pallo[5], pallo[6]-1, pallo[7]**3])
        
        







pygame.display.set_caption("Bloons TD")
screen = pygame.display.set_mode((1000,600))
dart_monkey_shop_icon=pygame.image.load("Dart_monkey_shop_icon.png")



clock = pygame.time.Clock()
grid = [[0 for _ in range(14)] for _ in range(12)]
c_v=0
curway = []
#hp
red_hp=1
blue_hp=1
green_hp=1
yellow_hp=1
purple_hp=1
white_hp=1
zebra_hp=1
rainbow_hp=1
rock_hp=5
blue_moab_hp=100
red_moab_hp=400
green_moab_hp=2000


p_hp=100
#dmg
red_dmg=1
blue_dmg=2
green_dmg=4
yellow_dmg=8
purple_dmg=16
white_dmg=32
zebra_dmg=64
rainbow_dmg=128
rock_dmg=256
blue_moab_dmg=1024
red_moab_dmg=4000
green_moab_dmg=16000

#points
red_p=2
blue_p=6
green_p=9
yellow_p=14
purple_p=20
white_p=28
zebra_p=35
rainbow_p=49
rock_p=70
blue_moab_p=130
red_moab_p=200
green_moab_p=300
#speeds
red_s=1
blue_s=1.5
green_s=1.7
yellow_s=2.4
purple_s=3
white_s=3
zebra_s=2.5
rainbow_s=3
rock_s=3
blue_moab_s=2
red_moab_s=1.4
green_moab_s=1


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
blue.append(blue_s)
green=[]
green.append((0, 255, 0))
green.append(green_dmg)
green.append(green_hp)
green.append(green_s)
yellow=[]
yellow.append((255, 255, 0))
yellow.append(yellow_dmg)
yellow.append(yellow_hp)
yellow.append(yellow_s)
purple=[]
purple.append((128, 0, 128))
purple.append(purple_dmg)
purple.append(purple_hp)
purple.append(purple_s)
red.append((255, 0, 0))
red.append(red_dmg)
red.append(red_hp)
red.append(red_s)
white=[]
white.append((255, 255, 255))
white.append(white_dmg)
white.append(white_hp)
white.append(white_s)
zebra=[]
zebra.append((128, 128, 128))
zebra.append(zebra_dmg)
zebra.append(zebra_hp)
zebra.append(zebra_s)
rainbow=[]
rainbow.append((0, 100, 0))
rainbow.append(rainbow_dmg)
rainbow.append(rainbow_hp)
rainbow.append(rainbow_s)
rock=[]
rock.append((165, 42, 42))
rock.append(rock_dmg)
rock.append(rock_hp)
rock.append(rock_s)
blue_moab=[]
blue_moab.append((0,0,255))
blue_moab.append(blue_moab_dmg)
blue_moab.append(blue_moab_hp)
blue_moab.append(blue_moab_s)
red_moab=[]
red_moab.append((255,0,0))
red_moab.append(red_moab_dmg)
red_moab.append(red_moab_hp)
red_moab.append(red_moab_s)
green_moab=[]
green_moab.append((0,255,0))
green_moab.append(green_moab_dmg)
green_moab.append(green_moab_hp)
green_moab.append(green_moab_s)










red_c=[]
blue_c=[]
green_c=[]
yellow_c=[]
purple_c=[]

white_c=[]
zebra_c=[]
rainbow_c=[]
rock_c=[]

blue_moad_c=[]
red_moab_c=[]
green_moab_c=[]





for i in range(1,10000):
    if i<35:
        red_c.append(i)
    if i<70 and i>20:
        blue_c.append(i)
    if i<140 and i>60:
        green_c.append(i)
    if i<230 and i>100:
        yellow_c.append(i)
    if i<500 and i>200:
        purple_c.append(i)
    if i<700 and i>400:
        white_c.append(i)
    if i<1300 and i>700:
        zebra_c.append(i)
    if i<1400 and i>1200:
        rainbow_c.append(i)
    if i<2000 and i>1400:
        rock_c.append(i)
    if i<2200 and i>2000:
        blue_moad_c.append(i)
    if i<3000 and i>2200:
        red_moab_c.append(i)
    if i>3000:
        green_moab_c.append(i)
        
res = 1

def waves(wave_points, h_v, c_v, res):
    i = 0
    wave_list = []
    start_x = curway[0][1] * 50 + 25
    start_y = curway[0][0] * 50 + 25

    while wave_points > 2:
        ok = random.randint(1, 20 + h_v)
        i += 1

        if ok in red_c:
            wave_list.append([red[0], red[1], red[2], [start_x, start_y], red_s, 1, 0, i])
            wave_points -= red_p

        if ok in blue_c:
            wave_list.append([blue[0], blue[1], blue[2], [start_x, start_y], blue_s, 1, 1, i])
            wave_points -= blue_p

        if ok in green_c:
            wave_list.append([green[0], green[1], green[2], [start_x, start_y], green_s, 1, 2, i])
            wave_points -= green_p

        if ok in yellow_c:
            wave_list.append([yellow[0], yellow[1], yellow[2], [start_x, start_y], yellow_s, 1, 3, i])
            wave_points -= yellow_p

        if ok in purple_c:
            wave_list.append([purple[0], purple[1], purple[2], [start_x, start_y], purple_s, 1, 4, i])
            wave_points -= purple_p

        if ok in white_c:
            wave_list.append([white[0], white[1], white[2], [start_x, start_y], white_s, 1, 5, i])
            wave_points -= white_p

        if ok in zebra_c:
            wave_list.append([zebra[0], zebra[1], zebra[2], [start_x, start_y], zebra_s, 1, 6, i])
            wave_points -= zebra_p

        if ok in rainbow_c:
            wave_list.append([rainbow[0], rainbow[1], rainbow[2], [start_x, start_y], rainbow_s, 1, 7, i])
            wave_points -= rainbow_p

        if ok in rock_c:
            wave_list.append([rock[0], rock[1], rock[2]*res, [start_x, start_y], rock_s, 1, 8, i])
            wave_points -= rock_p

        if ok in blue_moad_c:
            wave_list.append([blue_moab[0], blue_moab[1], blue_moab[2]*res, [start_x, start_y], blue_moab_s, 1, 9, i])
            wave_points -= blue_moab_p

        if ok in red_moab_c:
            wave_list.append([red_moab[0], red_moab[1], red_moab[2]*res, [start_x, start_y], red_moab_s, 1, 10, i])
            wave_points -= red_moab_p

        if ok in green_moab_c:
            wave_list.append([green_moab[0], green_moab[1], green_moab[2]*res, [start_x, start_y], green_moab_s, 1, 11, i])
            wave_points -= green_moab_p
        if ok>5000:
            wave_list.append([green_moab[0], green_moab[1], green_moab[2]*res, [start_x, start_y], green_moab_s, 1, 11, i])
            wave_points -= green_moab_p

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

clump=True
dur=3000
oko=0
m=0
cooldown=40000
arvot=[red,blue,green,yellow,purple,white,zebra,rainbow,rock,blue_moab,red_moab,green_moab]

def background():
    pygame.draw.rect(screen,(139, 69, 19),shop)    
    screen.blit(dart_monkey_shop_icon,(dart_monkeyshop))
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


def dart_monkeyplaced():
    dartshoot=[dartrange,(dartstayx,dartstayy),(211,211,211)]
    
    dart_monkeyshootbox.append(dartshoot)
    
    d=[25,(dartstayx,dartstayy),(0,0,0)]
    
    dart_monkeycooldowns.append(dartcooldown)
    
    dart_monkeys.append(d)
    for i in range(len(dart_monkeys)):
        dart_monkeyhit=pygame.Rect(0,0,45,45)
        dart_monkeyhit.center=(dartstayx,dartstayy)
        dart_monkeyshit.append(dart_monkeyhit)
    for i in dart_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
        
    
    
    


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
    

    
    

def boomerang_monkeyplaced():
    boomshoot=[boomrange,(boomstayx,boomstayy),(211,211,211)]
    
    boomerang_monkeyshootbox.append(boomshoot)
    
    d=[25,(boomstayx,boomstayy),(0,0,0)]
    
    boomerang_monkeycooldowns.append(boomcooldown)     
    
    boomerang_monkeys.append(d)
    for i in range(len(boomerang_monkeys)):
        boomerang_monkeyshit=pygame.Rect(0,0,45,45)
        boomerang_monkeyshit.center=(boomstayx,boomstayy)
        boomerang_monkeyhit.append(boomerang_monkeyshit)
    
    for i in boomerang_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])

def boomerang_monkeyshoot(i,balloonpos):
    if boomerang_monkeycooldowns[i]==0:
        boomerang_monkeycooldowns[i]=boomcooldown
    else:
        return
        
    x, y=boomerang_monkeyshootbox[i][1]
    balloonx=balloonpos[0]
    balloony=balloonpos[1]
        
            
    boomerangshoot(x,y,balloonx,balloony)


def boomerangshoot(x,y,balloonx,balloony):
    dx=balloonx-x
    dy=balloony-y
    
    distance=math.sqrt(dx**2+dy**2)
    
    if distance !=0:
        dx /= distance
        dy /= distance
    
    speed=boomerangspeed
    
    boomerangs.append([x,y,dx,dy,speed,x,y])
    comingback.append(False)
    
def in_boomerang_circle(x,balloonpos):
    Bx=balloonpos[0]
    By=balloonpos[1]
    

    
    r=x[0]
    
    Dx, Dy=x[1]
    
    return (Bx-Dx)**2 + (By-Dy)**2 <=r**2

def boomerangmax(i):
    boomx=boomerangs[i][5]
    boomy=boomerangs[i][6]
    x=boomerangs[i][0]
    y=boomerangs[i][1]
    
    dx=x-boomx
    dy=y-boomy
    
    distance=math.sqrt(dx**2+dy**2)
    
    return distance

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

def tackshootershoot(i):
     if tack_shootercooldowns[i]==0:
         tack_shootercooldowns[i]=snipecooldown
     else:
         return
         
     x, y=tack_shootershootbox[i][1]
         
             
     tackshoot(x,y)
     
def tackshoot(x,y):
    rotation=0
    tackring=[]
    while rotation<360:
        if rotation == 0:
            dx=0
            dy=-1
            tackring.append([x,y,dx,dy,tackspeed,x,y])
        elif rotation == 45:
            dx=0.7071
            dy=-0.7071
            tackring.append([x,y,dx,dy,tackspeed,x,y])
        elif rotation == 90:
            dx=1
            dy=0
            tackring.append([x,y,dx,dy,tackspeed,x,y])
        elif rotation == 135:
            dx=0.7071
            dy=0.7071
            tackring.append([x,y,dx,dy,tackspeed,x,y])
        elif rotation == 180:
            dx=0
            dy=1
            tackring.append([x,y,dx,dy,tackspeed,x,y])
        elif rotation == 225:
            dx=-0.7071
            dy=0.7071
            tackring.append([x,y,dx,dy,tackspeed,x,y])
        elif rotation == 270:
            dx=-1
            dy=0
            tackring.append([x,y,dx,dy,tackspeed,x,y])
        elif rotation == 315:
            dx=-0.7071
            dy=-0.7071
            tackring.append([x,y,dx,dy,tackspeed,x,y])
        rotation+=45
    tacks.append(tackring)
            
def in_tack_circle(x,balloonpos):
    Bx=balloonpos[0]
    By=balloonpos[1]
    

    
    r=x[0]
    
    Dx, Dy=x[1]
    
    return (Bx-Dx)**2 + (By-Dy)**2 <=r**2       
    
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
  
   
    pygame.draw.rect(screen,(255,0,0),sniper_monkeyhit) 

def sniper_monkeyshoot(i,balloonpos):
    

    if sniper_monkeycooldowns[i]==0:
        sniper_monkeycooldowns[i]=snipecooldown
    else:
        return
        
    x, y=sniper_monkeyshootbox[i][1]
    balloonx=balloonpos[0]
    balloony=balloonpos[1]
        
            
    snipebullet(x,y,balloonx,balloony)


def snipebullet(x,y,balloonx,balloony):
    dx=balloonx-x
    dy=balloony-y
    
    distance=math.sqrt(dx**2+dy**2)
    
    if distance !=0:
        dx /= distance
        dy /= distance
    
    speed=sniperspeed
    
    snipeds.append([x,y,dx,dy,speed])

def in_snipe_circle(x,balloonpos):

    Bx=balloonpos[0]
    By=balloonpos[1]
    

    
    r=x[0]
    
    Dx, Dy=x[1]
    
    return (Bx-Dx)**2 + (By-Dy)**2 <=r**2

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

def dart_monkeyshoot(i,balloonpos):
    

    if dart_monkeycooldowns[i]==0:
        dart_monkeycooldowns[i]=dartcooldown
    else:
        return
        
    x, y=dart_monkeyshootbox[i][1]
    balloonx=balloonpos[0]
    balloony=balloonpos[1]
        
            
    dartbullet(x,y,balloonx,balloony)


def dartbullet(x,y,balloonx,balloony):
    dx=balloonx-x
    dy=balloony-y
    
    distance=math.sqrt(dx**2+dy**2)
    
    if distance !=0:
        dx /= distance
        dy /= distance
    
    speed=dartspeed
    
    darts.append([x,y,dx,dy,speed])

def in_dart_circle(x,balloonpos):

    Bx=balloonpos[0]
    By=balloonpos[1]
    

    
    r=x[0]
    
    Dx, Dy=x[1]
    
    return (Bx-Dx)**2 + (By-Dy)**2 <=r**2
    
    
    
    
    
    
    
    
    

def draw_monkeys():
    #dartmonkey

    for i in dart_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])

        
    for i in range(len(darts)):
        pygame.draw.circle(screen, (255,0,0), (int(dart[0]), int(dart[1])),5)
    
    #boomerangmonkey

    
    for i in boomerang_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    for i in range(len(boomerangs)):
        pygame.draw.circle(screen, (255,0,0), (int(boomerang[0]), int(boomerang[1])),5)
    
    
    #tackshooter
    for n in range(len(tacks)):
        for i in range(len(tacks[n])):
            pygame.draw.circle(screen, (255,0,0), (int(tacks[n][i][0]), int(tacks[n][i][1])),5)  

    for i in tack_shooters:
        pygame.draw.circle(screen,i[2],i[1],i[0])
    
    
    #snipermonkey

    for i in sniper_monkeys:
        pygame.draw.circle(screen,i[2],i[1],i[0])
      
    for i in range(len(snipeds)):
        pygame.draw.circle(screen, (255,0,0), (int(snipeds[i][0]), int(snipeds[i][1])),5)    
    
    #bananafarm

    for i in banana_farms:
        pygame.draw.circle(screen,i[2],i[1],i[0])
     
    
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
boomerangs=[]
boomerangdistance=[]
comingback=[]
boomdistance=[]

tack_shooters=[]
tack_shootershit=[]
tack_shootershootbox=[]
tack_shootercooldowns=[]
tacks=[]

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
snipeds=[]

allhitboxes=[]

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

money=999999999

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

dartdamage=1
boomdamage=1
snipedamage=100
tackdamage=1

dartspeed=5
boomerangspeed=5
tackspeed=5
sniperspeed=40

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
    
    allhitboxes.clear()
    allhitboxes.append(dart_monkeyshit)
    allhitboxes.append(boomerang_monkeyhit)
    allhitboxes.append(sniper_monkeyshit)
    allhitboxes.append(tack_shootershit)
    allhitboxes.append(banana_farmshit)
    
    screen.fill((255,255,255))
    clock.tick(60)
    
    if len(spawn_queue)==0 and len(active_enemies)==0:
        
        spawn_queue=waves(wave_points, h_v, c_v,res)
        c_v+=1
        h_v=h_v+c_v*3
        wave_points+=wave_points*0.1
        if c_v>20:
            res+=(1+c_v//20)
    
    current_time = pygame.time.get_ticks()
    if len(spawn_queue) > 0 and current_time - last_spawn_time >= SPAWN_DELAY:
        if clump == False: 
            start_x = curway[0][1] * 50 + 25
            start_y = curway[0][0] * 50 + 25 
            new_balloon = [cb[0], cb[1], cb[2], [start_x, start_y], cb[4], 1, cb[6], cb[7]]
            active_enemies.append(new_balloon)
            if current_time-oko>dur:
                oko=current_time
                SPAWN_DELAY=250
                dur=random.randint(1000,10000)
                clump=True
        else:
            active_enemies.append(spawn_queue.pop(0))
            last_spawn_time = current_time
            if c_v > 5:
                cl = random.randint(1, 40)
                if cl == 5 and clump == True and current_time-m>cooldown:
                    SPAWN_DELAY = 50
                    clump = False 
                    last = active_enemies[-1]
                    cb = [last[0], last[1], last[2], None, last[4], last[5], last[6], last[7]] 
                    cooldown=random.randint(20000,400000)
        
    if clump==True:
        oko=current_time


    
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
            for i in allhitboxes:
                for n in i:
                    if n.collidepoint(event.pos):
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
            for i in allhitboxes:
                for n in i:
                    if n.collidepoint(event.pos):
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
            for i in allhitboxes:
                for n in i:
                    if n.collidepoint(event.pos):
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
            
            for i in allhitboxes:
                for n in i:
                    if n.collidepoint(event.pos):
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
            
            for i in allhitboxes:
                for n in i:
                    if n.collidepoint(event.pos):
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
    
    for i in range(len(dart_monkeycooldowns)):
        if dart_monkeycooldowns[i]>0:
            dart_monkeycooldowns[i]-=1
    for i in range(len(dart_monkeyshootbox)):
        for n in active_enemies:
            if in_dart_circle(dart_monkeyshootbox[i],n[3]):
                dart_monkeyshoot(i,n[3])
                break
    
            
    
    
    for dart in darts:
        dart[0] += dart[2] * dart[4]
        dart[1] += dart[3] * dart[4]
        
    for dart in darts:
        if dart[0]>1000 or dart[0]<0:
            if dart[1]>600 or dart[1]<0:
                darts.remove(dart)
            
    

    for i in active_enemies:
        hit=pygame.Rect(0,0,50,50)
        hit.center=(i[3])



        for dart in darts[:]:
            if hit.collidepoint(dart[0],dart[1]):
                i[2]-=dartdamage
                darts.remove(dart)
                break
            



    for i in active_enemies:
        if i[2]<=0:
            if c_v>9:
                ll=random.randint(1,c_v)
                if ll==1:
                    money+=1
            else:
                money+=1
            pop(i[6], i)
    if boomerang_monkeybought:
        if playarea.collidepoint(mousex,mousey):
            boomerang_monkeyplace()
    if boomplaced:
        boomerang_monkeyplaced()
        boomplaced=False
        
    for i in range(len(boomerang_monkeycooldowns)):
        if boomerang_monkeycooldowns[i]>0:
            boomerang_monkeycooldowns[i]-=1
    
    for i in range(len(boomerang_monkeyshootbox)):
        for n in active_enemies:
            if in_dart_circle(boomerang_monkeyshootbox[i],n[3]):
                boomerang_monkeyshoot(i,n[3])
                break
    
    for i in range(len(boomerangs)-1,-1,-1):
        if boomerangs[i][0]==boomerangs[i][5]:
            if boomerangs[i][1]==boomerangs[i][6]:
                if comingback[i]:
                    boomerangs.pop(i)
                    comingback.pop(i)
            
    for i in range(len(comingback)):
        if not comingback[i]:
            boomerangs[i][0] += boomerangs[i][2] * boomerangs[i][4]
            boomerangs[i][1] += boomerangs[i][3] * boomerangs[i][4]
        else:
            boomerangs[i][0] -= boomerangs[i][2] * boomerangs[i][4]
            boomerangs[i][1] -= boomerangs[i][3] * boomerangs[i][4]
        
        
    for i in range(len(comingback)):
        if boomerangmax(i)>boomrange:
            comingback.pop(i)
            comingback.insert(i,True)
    
    for i in range(len(boomerangs)-1,-1,-1):
        if boomerangs[i][0]>1000 or boomerangs[i][0]<0:
            if boomerangs[i][1]>600 or boomerangs[i][1]<0:
                boomerangs.pop(i)
                comingback.pop(i)
            
    

    for i in active_enemies:
        hit=pygame.Rect(0,0,50,50)
        hit.center=(i[3])



        for boomerang in boomerangs[:]:
            if hit.collidepoint(boomerang[0],boomerang[1]):
                i[2]-=boomdamage
                
            
    
    if tack_shooterbought:
        if playarea.collidepoint(mousex,mousey):
            tack_shooterplace()
    if tackplaced:
        tack_shooterplaced()
        tackplaced=False
      
    for i in range(len(tack_shootercooldowns)):
        if tack_shootercooldowns[i]>0:
            tack_shootercooldowns[i]-=1
    for i in range(len(tack_shootershootbox)):
        for n in active_enemies:
            if in_tack_circle(tack_shootershootbox[i],n[3]):
                tackshootershoot(i)
                break
    for n in tacks:
        for i in n:
            i[0] += i[2] * i[4]
            i[1] += i[3] * i[4]
    for i in range(len(tacks)-1,-1,-1):
        n=tacks[i]
        dx=n[0][5]-n[0][0]
        dy=n[0][6]-n[0][1]
                
        if dx**2 + dy**2 >= tackrange**2:
            tacks.pop(i)
    
    
    for n in active_enemies:
        hit=pygame.Rect(0,0,50,50)
        hit.center=(n[3])



        for a in tacks[:]:
            for i in a:
                if hit.collidepoint(i[0],i[1]):
                    n[2]-=tackdamage
                    
                

    
    
    if sniper_monkeybought:
        if playarea.collidepoint(mousex,mousey):
            sniper_monkeyplace()
    
    if sniperplaced:
        sniper_monkeyplaced()
        sniperplaced=False
    
    for i in range(len(sniper_monkeycooldowns)):
        if sniper_monkeycooldowns[i]>0:
            sniper_monkeycooldowns[i]-=1
    for i in range(len(sniper_monkeyshootbox)):
        for n in active_enemies:
            if in_snipe_circle(sniper_monkeyshootbox[i],n[3]):
                sniper_monkeyshoot(i,n[3])
                break
    
            
    
    
    for i in snipeds:
        i[0] += i[2] * i[4]
        i[1] += i[3] * i[4]
        
    for i in snipeds:
        if i[0]>1000 or i[0]<0:
            if i[1]>600 or i[1]<0:
                snipeds.remove(i)
            
    

    for n in active_enemies:
        hit=pygame.Rect(0,0,50,50)
        hit.center=(n[3])



        for i in snipeds[:]:
            if hit.collidepoint(i[0],i[1]):
                n[2]-=snipedamage
                snipeds.remove(i)
                break
    
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
        if i[6]<9:
            pygame.draw.circle(screen, i[0], (int(i[3][0]), int(i[3][1])), 20)
        if i[6]==10:
            pygame.draw.circle(screen, i[0], (int(i[3][0]), int(i[3][1])), 35)
        if i[6]==11:
            pygame.draw.circle(screen, i[0], (int(i[3][0]), int(i[3][1])), 45)
        if i[6]==12:
            pygame.draw.circle(screen, i[0], (int(i[3][0]), int(i[3][1])), 60)
     
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
    wave_text = font.render(f"Wave: {c_v}", True, (0, 0, 0))
    hp_text = font.render(f"HP: {p_hp}", True, (0, 0, 0))
    screen.blit(wave_text, (590, 10))
    screen.blit(hp_text, (500, 10))      
    background()
    pygame.display.update()


pygame.quit()
