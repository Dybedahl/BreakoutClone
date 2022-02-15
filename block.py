import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, lives, imagepath):
        super().__init__()
        
        self.life = lives
        
        # spawns the blocks
        self.imagepath = imagepath
        self.image = pygame.image.load(self.imagepath + '_' + str(self.life)+ '.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (237/2, 106/2))
        self.rect = self.image.get_rect()
        
            
    def block_hit(self):
        
        # removes one life from the block
        self.life -= 1
        
        if self.life == 0:
            self.kill()
        
        else:
            
            # replaces the image when lost a life
            self.image = pygame.image.load(self.imagepath + '_' + str(self.life)+ '.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (237/2, 106/2))
            
            pos = self.rect.topleft
    
            self.rect = self.image.get_rect()
            self.rect.topleft = pos