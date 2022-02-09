import pygame 
class Bullet(pygame.sprite.Sprite): 
    def __init__(self,x,y): 
        # 因为子弹坐标和飞船有关，所以init的时候input飞船坐标xy
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((10,20))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.centerx= x 
        self.rect.bottom = y
        self.speedy = -10 # 向正上方发射

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <0:
            # 超出视窗
            self.kill() # 移除掉所有群组里面这个子弹的存在

