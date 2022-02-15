import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # spawns the player
        self.image = pygame.image.load('Assets/platform.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (326/2, 105/2))
        self.rect = self.image.get_rect()
                 
        self.rect.centerx = 1600/2
        self.rect.y = 750
        
    
    # moves the player using A and D or arrow keys
    def player_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= 15
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += 15
            
    # updates the player position
    def update(self):
        self.player_move()
