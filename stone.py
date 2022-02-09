import pygame 
import random
import os
rock_img = pygame.image.load(os.path.join("img","rock.png"))
size = [(20,20),(30,30),(40,40),(50,50),(60,60),(70,70),[80,80]]
# 7 种石头size 
class stone(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        # self.image = pygame.Surface((30,40))
        self.image_origin = pygame.transform.scale(rock_img,random.choice(size))
        # 随机一个size的石头生成
        self.image = self.image_origin.copy()
        # 保存个原始图片，用于后续石头旋转

        #self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width*0.85/2

        self.rect.x= random.randrange(0,500-self.rect.width) 
        # 从0-500随机一个数字作为初始生成坐标
        self.rect.y = random.randrange(-180,-100) 
        # 从视窗上面看不到的地方
        self.speedx = random.randrange(-3,3)
        self.speedy = random.randrange(2,8)
        self.total_degree = 0
        self.rotate_degree = random.randrange(-3,3)


    # 石头旋转
    def rotate(self):
        self.total_degree += self.rotate_degree
        self.total_degree = self.total_degree % 360 
        #超过360度取余数，避免旋转过多
        self.image = pygame.transform.rotate(self.image_origin,self.total_degree)
        # 开始重新定位旋转的中心点
        center = self.rect.center # 存储原始的中心点
        self.rect = self.image.get_rect() # 重新画方形
        self.rect.center = center # 新方形的中心点设为原始中心点



    def update(self):
        # 石头旋转动画
        self.rotate()
        self.rect.y += self.speedy 
        # 以 speedy 的速度匀速移动y坐标，掉下来
        self.rect.x += self.speedx
        # 一旦石头超出视窗，重置坐标
        if self.rect.top > 600 or self.rect.left>500 or self.rect.right <0:
            # 这里视窗左上角为（0,0）
            self.rect.x= random.randrange(0,500-self.rect.width) 
            self.rect.y = random.randrange(-100,-40)
            self.speedx = random.randrange(-2,2)
            self.speedy = random.randrange(2,10)
             