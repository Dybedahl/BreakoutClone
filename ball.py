import pygame, random
from precode import intersect_rectangle_circle


class Ball(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        
        self.image = pygame.image.load('Assets/ball.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
                    
        self.rect.centerx = 1600/2
        self.rect.y = 550
        
        # add velocity to ball
        self.velocity = pygame.Vector2(0.5, 0.5)
        self.velocity = self.velocity.normalize()
        self.speed = 10.0
        

    def update(self):
        self.rect.x += self.velocity[0] * self.speed
        self.rect.y += self.velocity[1] * self.speed
        
        
    def paddle_bounce(self, collision_rect):
        
        # lets the paddle semi-control the ball
        self.velocity = intersect_rectangle_circle(collision_rect, collision_rect.width, collision_rect.height, pygame.Vector2(self.rect.centerx, self.rect.centery), self.rect.width/2, self.velocity)
        self.velocity.x = (((self.rect.centerx - collision_rect.left)/collision_rect.width)-0.5)*2
        self.velocity = self.velocity.normalize()
    
    def block_bounce(self, collision_rect):
        
        # using the precode calulate angel of bounce
        self.velocity = intersect_rectangle_circle(collision_rect, collision_rect.width, collision_rect.height, pygame.Vector2(self.rect.centerx, self.rect.centery), self.rect.width/2, self.velocity)
