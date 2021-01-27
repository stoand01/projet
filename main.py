import pgzrun
import random 

krab = Actor('krab')
popey = Actor('popey')
dstroke = Actor('dstroke')
bullet = Actor('bullet')

WIDTH = 500
HEIGHT = 500
 
dstroke.midbottom = WIDTH / 2, HEIGHT - 5
krab.midbottom = (random.randint(40, WIDTH - 40), 80)
popey.midbottom = (random.randint(40, WIDTH - 40), 80)

score = 0
game_status = 0  # 0 = stop, 1 = playing
bullet_status = 0  # 0 for not fired, 1 for fired
krab_speed = 1.0
bullet_speed = 1.0

def draw():
    if game_status == 0:
        screen.draw.text("Press e", (100, 300), color="blue", fontsize=70)
    if game_status == 1:
        screen.clear()
        screen.draw.text("Score: " + str(score), (20, 20))
        dstroke.draw()
        move_krab(krab)  
        krab.draw()
        if score > 10:
            move_krab(popey)
            popey.draw()
        if bullet_status > 0:
            move_bullet()
            bullet.draw()
        detect_hits()
       
          

def update():
    checkKeys()

def checkKeys():
    global dstroke, bullet, game_status, bullet_status
    if game_status == 0:
        if keyboard.e:
            game_status = 1
    elif game_status == 1:
        if keyboard.left:
            if dstroke.x > 40:
                dstroke.x -= 5
        if keyboard.right:
            if dstroke.right < 760:
                dstroke.x += 5
        if bullet_status == 0:
            if keyboard.space:
                bullet.pos = (dstroke.x, HEIGHT - 98)
                bullet_status = 1

def move_krab(krab_name):
    global krab_speed
    krab_name.pos = (krab_name.x, krab_name.y+(1*krab_speed))
    
def move_bullet():
    global bullet_status, bullet_speed
    if bullet_status > 0:
        bullet.pos = (bullet.x, bullet.y - (2*bullet_speed))
        if bullet.y < 10:
            bullet_status = 0

def game_over(krab_name):
    global game_status
    if krab_name.y >= HEIGHT - 40:
        screen.draw.text("Game Over", (100, 300), color="red", fontsize=80)
        game_status = 1

def bullet_hit(krab_name, aggression, powerup):
    ''' Each krab can speed up with aggression and give you a '''
    ''' quicker bullet with power up '''
    global bullet_status, score, krab_speed, bullet_speed
    if bullet_status == 1 and krab_name.collidepoint(bullet.pos):
        hit_krab(krab_name)
        bullet_status = 0
        score += 1
        krab_speed += aggression
        bullet_speed += powerup

def detect_hits():
    global score, bullet_status, krab_speed, bullet_speed
    game_over(krab)
    game_over(popey)
    bullet_hit(krab, 0.125, 0.1)
    bullet_hit(popey, 0.1, 0.125)

def hit_krab(krab_name):
    krab_name.midbottom = (random.randint(40, WIDTH - 40), 80)

pgzrun.go

#https://github.com/jonwitts/PygameZero-Space/blob/master/space-invaders.py
#code cree par jonwitts