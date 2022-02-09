import pygame
import os
# 爆炸动画
BLACK = (0,0,0)
expl_anim={} # 字典
expl_anim['lg'] = [] #list
expl_anim['sm'] = []
expl_anim['pl'] = []
for i in range(9):
    expl_img = pygame.image.load(os.path.join("img",f"expl{i}.png"))
    expl_img.set_colorkey(BLACK) # 把黑色变成透明
    expl_anim['lg'].append(pygame.transform.scale(expl_img,(75,75)))
    expl_anim['sm'].append(pygame.transform.scale(expl_img,(30,30)))
    player_expl_img = pygame.image.load(os.path.join("img",f"player_expl{i}.png"))
    player_expl_img.set_colorkey(BLACK) # 把黑色变成透明
    expl_anim['pl'].append(player_expl_img)

class explotion(pygame.sprite.Sprite): 
    def __init__(self,center,size): 
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = expl_anim[self.size][0] # 大爆炸or小包装，第0张图
        self.rect = self.image.get_rect()
        self.rect.center= center
        self.frame = 0 # 更新到第几张图片
        self.last_update = pygame.time.get_ticks()
        # return 从init到现在经过的毫秒数
        self.frame_rate = 50
        # 设置每张图片间隔毫秒数


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame ==len(expl_anim[self.size]):
                self.kill()
            else:
                self.image = expl_anim[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center