import pygame 
import os
from bullet import Bullet
pygame.mixer.init()
player_img = pygame.image.load(os.path.join("img","spaceship.png"))
shoot_sound = pygame.mixer.Sound(os.path.join("sound","shoot.wav"))

# 从pygame自带的class spirit继承
class Player(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        # self.image = pygame.Surface((50,40)) 
        # 表示要显示的图片，这里先用pygame平面的图片表示
        # 宽度50，高度40
        #self.image.fill((0,255,0))
        self.image = pygame.transform.scale(player_img,(50,38))
        # 导入图片，太大了，transform改小
        # self.image.set_colorkey((255,255,255))
        # 这一步用来把后面黑色底色变透明

        self.rect = self.image.get_rect() 
        self.radius = 20
        # get_rect() 为，将这个图片框起来，后面可以设置属性，
        # 比如center，top这些方位或者（x y)坐标 
        '''
        self.rect.x = 200
        self.rect.y = 200
        # 这里可以理解为，先做了一个长方形rect，然后框起来，放到视窗的200,200坐标位置
        '''
        self.rect.centerx=500/2 # width/2
        self.rect.bottom = 600 - 10 # height 
        self.speedx = 8

        self.health = 100 # 飞船血条
        self.life =3 # 命


    def update(self):
        
        # https://cloud.tencent.com/developer/article/1490196
        key_pressed = pygame.key.get_pressed() 
        # return boolean whether the keys has been pressed
        if key_pressed[pygame.K_RIGHT]: # 右方向键被按
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        # mouse = pygame.MOUSEMOTION
        # self.rect.centerx = mouse
        
        if self.rect.left<= 0:
            self.rect.left=0
        if self.rect.right>=500:
            self.rect.right=500
        
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        shoot_sound.play()
        return bullet 
    


'''
        self.rect.x+=2
        # 方块持续向右移动
        if self.rect.left > 500:
            self.rect.right = 0
            # 如果左边坐标>width，右边坐标变成0
'''