import os
import random
import sys
import time
import pygame

def image_from_url(url):
    try:
        from urllib2 import urlopen
        from cStringIO import StringIO as inout
    except ImportError:
        from urllib.request import urlopen
        from io import BytesIO as inout
    myurl = urlopen(url)
    return inout(myurl.read())

background_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/space_zpsec971d2c.png')
meteor_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/f3252a21-352d-49ca-a7ae-eac85c18b4b7_zpsd97af755.png?t=1387696943')
meteor2_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/097c706e-bb42-4400-8f79-78d805d685e5_zps629c6efa.png?t=1387696885')
Spaceship_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/a1c54686-2e35-442d-85a9-20ae135db85b_zps406f61d7.png?t=1387696835')
explosion_URL = ('http://i1315.photobucket.com/albums/t600/11roadkills/explosion_zpsbbc7bb55.png')

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

pa = False
pygame.init()
DISPLAYSURF = pygame.display.set_mode((900,700),0,32)
pygame.display.set_caption('Astroid feild')
clock = pygame.time.Clock()
u = True
d = False
t = True
spaceship_img = pygame.image.load(image_from_url(Spaceship_URL))
spaceship = pygame.transform.scale(spaceship_img, (150,90))
meteor = pygame.image.load(image_from_url(meteor_URL))
background_img = pygame.image.load(image_from_url(background_URL))
background = pygame.transform.scale(background_img, (800,800))
meteor2 = pygame.image.load(image_from_url(meteor2_URL))
myfont = pygame.font.SysFont("Lucida Console", 30)
myfont2 = pygame.font.SysFont("Lucida Console", 100)
myfont3 = pygame.font.SysFont("Lucida Console", 80)
place = [(800,298) , (800,200) , (800,80) , (800,500)]
setplace = random.choice(place)
place2 = [(800,256) , (800,90) , (800,180) , (800,500)]
setplace2 = random.choice(place)
explosion_img = pygame.image.load(image_from_url(explosion_URL))
explosion = pygame.transform.scale(explosion_img, (170,110))
level = 5
distance = 0
i = 255
f = True
label2 = myfont2.render("GAME OVER", 1, RED)
label3 = myfont3.render("Astroid Feild", 1, GREEN)
label4 = myfont.render("Play", 1, GREEN)
label5 = myfont.render("Quit", 1, GREEN)
backgroundrect = background.get_rect(topleft=(1,1))
meteorrect = meteor.get_rect(topleft=(setplace))
meteorrect2 = meteor.get_rect(topleft=(setplace2))
meteorrect3 = meteor.get_rect(topleft=(setplace))
meteorrect4 = meteor.get_rect(topleft=(setplace2))
spaceshiprect = spaceship.get_rect(topleft= (1,100))
l = True
p = False
hit = False
while True:
    DISPLAYSURF.fill(BLACK)
    key = pygame.key.get_pressed()
    if l and key[pygame.K_UP] and not hit and l:
        spaceshiprect.y -= level
    if l and key[pygame.K_DOWN] and not hit:
        spaceshiprect.y += level 
    if l and key[pygame.K_RIGHT] and not hit:
        spaceshiprect.x += level - 3
    if l and key[pygame.K_LEFT] and not hit:
        spaceshiprect.x -= level - 3


    DISPLAYSURF.blit(background, backgroundrect)
    DISPLAYSURF.blit(spaceship, spaceshiprect)
    DISPLAYSURF.blit(meteor, meteorrect)
    DISPLAYSURF.blit(meteor2, meteorrect2)
    DISPLAYSURF.blit(meteor, meteorrect3)

    if p == False:
        spaceship = pygame.transform.scale(spaceship, (300, 240))
        DISPLAYSURF.fill((119,136,153))
        DISPLAYSURF.blit(label3, (150,100))
        DISPLAYSURF.blit(spaceship, (250,200))
        pygame.draw.rect(DISPLAYSURF, BLACK, (300, 450, 200, 200,))
        DISPLAYSURF.blit(label4, (360,550))
        DISPLAYSURF.blit(label5, (360,580))
        if key[pygame.K_UP]:
            u = True
            d = False
        if u:
            pygame.draw.rect(DISPLAYSURF, GREEN, (350, 550, 85, 35,), 10)
            if key[pygame.K_RETURN]:
                spaceship = pygame.transform.scale(spaceship_img, (150,90))
                p = True
                l = True
        if key[pygame.K_DOWN]:
            d = True
            u = False
        if d:
            pygame.draw.rect(DISPLAYSURF, GREEN, (350, 580, 80, 30,), 10)
            if key[pygame.K_RETURN]:
                pygame.quit()
            
    if spaceshiprect.colliderect(meteorrect) or spaceshiprect.colliderect(meteorrect2) or spaceshiprect.colliderect(meteorrect3):
        hit = True

    if hit:
        l = False

    if l == False:
        label4 = myfont.render("Play again", 1, GREEN)
        explosionrect = explosion.get_rect(topleft=(spaceshiprect.x, spaceshiprect.y))
        DISPLAYSURF.blit(explosion, explosionrect)
        DISPLAYSURF.blit(label2, (200,200))
        DISPLAYSURF.blit(label4, (370,550))
        DISPLAYSURF.blit(label5, (430,580))
        if key[pygame.K_UP]:
            u = True
            d = False       
        if u:
            pygame.draw.rect(DISPLAYSURF, GREEN, (360, 550, 220, 30,), 10)
            if key[pygame.K_RETURN]:
                f = True
                spaceshiprect = spaceship.get_rect(topleft=(-25,298))
                level = 5
                distance = 0
            if f:
                p = True
                hit = False
                l = True
                
        if key[pygame.K_DOWN]:
            d = True
            u = False
        if d:
            pygame.draw.rect(DISPLAYSURF, GREEN, (430, 580, 80, 30,), 10)
            if key[pygame.K_RETURN]:
                pygame.quit()



        
        
    if meteorrect.x <= -25:
        place = [(800,spaceshiprect.y) , (850,80) , (800,spaceshiprect.y) , (800,298) , (950,spaceshiprect.y) , (950,80) , (900,spaceshiprect.y) , (900,298)]
        setplace = random.choice(place)
        place2 = [(800,256) , (800,spaceshiprect.y) , (850,30) , (800,spaceshiprect.y) , (950,500) , (900,spaceshiprect.y) , (900,200) , (900,spaceshiprect.y)]
        setplace2 = random.choice(place2)
        meteorrect = meteor.get_rect(topleft=(setplace))
        meteorrect2 = meteor2.get_rect(topleft=(setplace2))
        DISPLAYSURF.blit(meteor, meteorrect)
        DISPLAYSURF.blit(meteor2, meteorrect2)
        level += 1
        distance += 1
    if p:
        distanceboard = myfont.render('Distance: {} Killometers'.format(distance), 1 , GREEN)
        DISPLAYSURF.blit(distanceboard, (10,10))


    if l and not hit:
        meteorrect.x -= level
        meteorrect2.x -= level
        meteorrect3.x -= level
        
    if meteorrect3.x <= -25:
        place3 = [(1050,200) , (1050,spaceshiprect.y) , (1200,40) , (1200,spaceshiprect.y) , (1050,600) , (1080,spaceshiprect.y) , (1050,300) , (1200,spaceshiprect.y)]
        setplace3 = random.choice(place3)
        meteorrect3 = meteor.get_rect(topleft=(setplace3))
        DISPLAYSURF.blit(meteor, meteorrect3)
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
