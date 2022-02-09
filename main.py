# https://www.youtube.com/watch?v=61eX0bFAsYs&t=182s 

import pygame 
import random
import os
# from fpsCounter import FPSCounter
from player import Player
from stone import stone 
from bullet import Bullet
from expo import explotion
# 游戏的初始化 &创建视窗
pygame.init()
# 音效模组初始化
pygame.mixer.init()
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
WIDTH = 500
HIGHT = 600
running = True # indicate whether the game continou

 
clock = pygame.time.Clock()
# 创建一个object，对时间进行操控

# https://www.cuoshuo.com/blog/300913.html
# # 载入图片 - 实际上在每个file里面单独load
bg = pygame.image.load(os.path.join("img","universe.jpg")) 
player_img = pygame.image.load(os.path.join("img","spaceship.png"))
player_life_img = pygame.transform.scale(player_img,(25,19))
player_life_img.set_colorkey(BLACK) # 把黑色变成透明

#bg = pygame.image.load("space.png")
# os.path 找文件所在资料夹， 搜索“image" file, 找到里面的相关文件
# convert()把图片转化为pygame方便读取的格式

# # 爆炸动画
# expl_anim={} # 字典
# expl_anim['lg'] = [] #list
# expl_anim['sm'] = []
# for i in range(9):
#     expl_img = pygame.image.load(os.path.join("img",f"expl{i}.png")).convert()
#     expl_img.set_colorkey(BLACK) # 把黑色变成透明
#     expl_anim['lg'].append(pygame.transform.scale(expl_img,(75,75)))
#     expl_anim['sm'].append(pygame.transform.scale(expl_img,(30,30)))


# 载入音乐
explosion_sound = pygame.mixer.Sound(os.path.join("sound","explosion.wav"))
die_sound = pygame.mixer.Sound(os.path.join("sound","rumble.ogg"))
# 背景音乐load和别的不一样，直接load为music
pygame.mixer.music.load(os.path.join("sound","bgm_war.mp3"))
# 改声音大小
pygame.mixer.music.set_volume(0.4)

######################文字格式##########################3
font_name = pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,WHITE)
    # 文字定位
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface,text_rect)

#######################重新生成石头******************
def new_rock():
    r= stone()
    all_sprites.add(r)
    rocks.add(r)

######################画出生命值#######################
def draw_health(surf,hp,x,y):
    if hp<0:
        hp=0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    # 这里rect 是大写，代表矩形，而不是框起
    fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf,GREEN,fill_rect)
    pygame.draw.rect(surf,WHITE,outline_rect,2)
    # 最后一个参数2 代表draw的像素值

#########################画出命#################33
def draw_life(surf,life,img,x,y):
    for i in range(life):
        img_rect = img.get_rect()
        img_rect.x=x+30*i
        img_rect.y = y
        surf.blit(img,img_rect)

###############初始画面#####################
def draw_init():
    screen.blit(bg,(0,0))
    draw_text(screen,"star war",64,WIDTH/2, HIGHT/4)
    draw_text(screen,"← → move，space shoot~~~",22,WIDTH/2,HIGHT/2)
    draw_text(screen,"press any key to start!!",18,WIDTH/2,HIGHT*3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)  
        # progress input 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                waiting = False
                return False





#********SPRITE***********
# 创建 spirite 类别，save所有创建的东西，为了后面update 和显示
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# 单独创建额外的spirit类别，用来判断rock和bullet的轨迹和碰撞
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
# rock = stone()
# all_sprites.add(rock)
for i in range(8):
    new_rock()
score = 0 # 记录分数

pygame.mixer.music.play(-1)
# 播放bgm，参数-1代表重复播放

'''
**********SCREEN SETTING**********
'''
screen = pygame.display.set_mode((WIDTH,HIGHT)) # 创建视窗大小为500*600
# 改视窗标题
pygame.display.set_caption("打飞机")
pygame.display.set_icon(player_life_img)



'''
******************FPS Countor ******************
'''
cl=pygame.time.Clock()



"""
整个游戏就不停在loop： progress input -> update game -> render -> clock ->loop
game loop 
"""
show_init = True
while running:
    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False
        all_sprites = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        # 单独创建额外的spirit类别，用来判断rock和bullet的轨迹和碰撞
        rocks = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        # rock = stone()
        # all_sprites.add(rock)
        for i in range(8):
            new_rock()
        score = 0 # 记录分数


    clock.tick(FPS) # 在一秒内最多被执行60次 FPS 

    # progress input 
    for event in pygame.event.get():
        # pygame.event.get()回传发生的所有事件，比如键盘按键，鼠标操作，是个列表
        # 所以for loop 来go though所有的element，也就是event，来一一检查
        
        # 如果点了关闭游戏视窗，则游戏停止运行
        if event.type == pygame.QUIT:
            running = False
            '''
            ********************BULLET子弹********************
            因为子弹是随时按随时变的，所以放在game loop里，shoot写在player里
            '''
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                b = player.shoot()
                all_sprites.add(b)
                bullets.add(b)

    
    cl.tick()
    fps = cl.get_fps()
    fps_p = "FPS: %s" %int(fps)



    # update game 
    all_sprites.update()
    # 这里更新了每一次loop之后的所有内容
    # 在这里做判断，判断子弹和石头位置
    hits = pygame.sprite.groupcollide(rocks,bullets,True,True)
    # groupcollide 判断两个group是不是有碰到，
    # 后面两个input boolean 代表碰到之后要不要kill掉，ture代表碰到就消失
    for hit in hits:
        score += hit.radius
        # groupcollide return 一个dictionary，里面是碰撞到的rock和bullet
        # key 就是rock
        explosion_sound.play()
        expl = explotion(hit.rect.center,'lg')
        all_sprites.add(expl) # 加这个才能画出来
        new_rock()
        # 消失掉的石头都重新生成



    # 石头和飞机碰撞
    hits = pygame.sprite.spritecollide(player,rocks,True,pygame.sprite.collide_circle)
    # spritecollide 用来找一个sprite里面的一个group和别的sprite的碰撞
    # pygame.sprite.collide_circle 改成圆形碰撞判断
    # 需要在player和stone里增加radius属性
    # Boolean true 表示撞击之后石头删掉，false表示不删掉
    # return的是个列表 list，表示所有撞击的rock
    # 所以hit in hits 是rock class的
    for hit in hits:
        new_rock()
        player.health -= hit.radius
        expl = explotion(hit.rect.center,'sm')
        all_sprites.add(expl) # 加这个才能画出来
        if player.health <=0:
            death_expl = explotion(player.rect.center,'pl')
            all_sprites.add(death_expl)
            die_sound.play()
            player.life-=1
            player.health=100
            # running = False  
    if player.life==0 and not(death_expl.alive()):
        # 判断death 爆炸 有没有run完，return boolean值
        show_init = True


    # render 画面显示
    screen.fill(BLACK)# 屏幕被什么颜色fill，调色盘（R，G，B）颜色 (255,255,255)白
    screen.blit(bg,(0,0))
    # bilt: 画在画面上（名字，坐标）
    all_sprites.draw(screen)# 把sprite里的东西都画在画面上
    draw_text(screen,str(int(score)),18,WIDTH/2,10)
    draw_text(screen,fps_p,18,WIDTH-WIDTH/8,10)
    draw_health(screen,player.health, WIDTH/9,10)
    draw_life(screen,player.life,player_life_img,WIDTH-WIDTH/4,50)
    pygame.display.update() # 画面更新

# 退出游戏
pygame.quit()
