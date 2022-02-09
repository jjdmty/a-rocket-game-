import pygame 
import random
import os
WHITE = (255,255,255)
power_imgs = {}
power_imgs['shield'] = pygame.image.load(os.path.join("img","shield.png"))
power_imgs['gun'] = pygame.image.load(os.path.join("img","gun.png"))
power_imgs['shield'].set_colorkey(WHITE)
power_imgs['gun'].set_colorkey(WHITE)
class Power(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield','gun'])
        self.image = power_imgs[self.type]
        self.rect = self.image.get_rect()
        self.rect.center = center