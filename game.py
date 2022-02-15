#!/usr/bin/env python

import pygame
import math
from player import Player
from ball import Ball
from block import Block

SCREEN_X = 1600
SCREEN_Y = 900
BG_FNAME = open("Assets/background.jpeg")
pygame.display.set_caption("Breakout Shenanigans")

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
font = pygame.font.Font('Assets/HOMOARAK.TTF', 32)

# screen for the game
surface = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
background = pygame.image.load(BG_FNAME)

# texts for aesthetics
text_start = font.render('Press SPACE to start', True, (59, 212, 137), None)
text_restart = font.render(' press "R" to restart', True, (59, 212, 137), None)
text_game_over = font.render('Game Over', True, (59, 212, 137), None)
text_game_win = font.render('Winner winner chicken dinner', True, (59, 212, 137), None)

text_startRect = text_start.get_rect()
text_restartRect = text_restart.get_rect()
text_game_overRect = text_game_over.get_rect()
text_game_winRect = text_game_win.get_rect()

text_startRect.center = (SCREEN_X/2, SCREEN_Y/2)
text_restartRect.center = (SCREEN_X/2, SCREEN_Y/2+45)
text_game_overRect.center = (SCREEN_X/2, SCREEN_Y/2)
text_game_winRect.center = (SCREEN_X/2, SCREEN_Y/2)


def game():
    
    # group for sprites used
    all_objects = pygame.sprite.Group()

    # player group
    player = Player()

    # ball group
    ball = Ball()

    # blocks group
    blocks = pygame.sprite.Group()
    for i in range(13):
        block = Block(3, 'Assets/block3')
        block.rect.x = 40 + i* 115
        block.rect.y = 60
        all_objects.add(block)
        blocks.add(block)

    for i in range(13):
        block = Block(2, 'Assets/block2')
        block.rect.x = 40 + i* 115
        block.rect.y = 110
        all_objects.add(block)
        blocks.add(block)

    for i in range(13):
        block = Block(1, 'Assets/block1')
        block.rect.x = 40 + i* 115
        block.rect.y = 160
        all_objects.add(block)
        blocks.add(block)

    # adds objects to the all_objects group
    all_objects.add(player)
    all_objects.add(blocks)
    all_objects.add(ball)

    # parameters for game code
    close_game = False
    game_over = False
    game_start = False
    game_win = False

    # game loop
    while not close_game:
        events = pygame.event.get()
        
        # checks if the game should close
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                close_game = True
                exit()
        
        # background
        clock.tick(60)
        surface.blit(background, (0, 0))
        
        if game_start and not game_over:
                
            # prevents the player from moving outside the borders
            if player.rect.left <= 0:
                player.rect.left = 0
            if player.rect.right >= SCREEN_X:
                player.rect.right = SCREEN_X
            
            # ball collision with borders
            if ball.rect.right >= SCREEN_X:
                ball.velocity[0] = -abs(ball.velocity[0])
            if ball.rect.left <= 0:
                ball.velocity[0] = abs(ball.velocity[0])
            if ball.rect.top <= 0:
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.bottom >= SCREEN_Y:
                game_over = True
                
            # ball collision with player
            if pygame.sprite.collide_mask(ball, player):
                ball.rect.x -= ball.velocity[0]
                ball.rect.y -= ball.velocity[1]
                ball.paddle_bounce(player.rect)
            
            # ball collision with block
            block_collision = pygame.sprite.spritecollide(ball, blocks, False)
            for block in block_collision:
                block.block_hit()
                ball.block_bounce(block.rect)
                if block.life == 0:
                    blocks.remove(block)
            
            # checks if there are any blocks left
            if len(blocks) == 0:
                game_win = True
                game_over = True
            
            # updates all sprites
            all_objects.update()
        
        # if the condition for game won is true runs text and restarts if R is pressed
        elif game_win:
            
            surface.blit(text_game_win, text_game_winRect)
            surface.blit(text_restart, text_restartRect)
            
            restart = pygame.key.get_pressed()
            if restart[pygame.K_r]:
                game()

        # if the condition for game over is true runs text and restarts if R is pressed
        elif game_over:
            
            surface.blit(text_game_over, text_game_overRect)
            surface.blit(text_restart, text_restartRect)
            
            restart = pygame.key.get_pressed()
            if restart[pygame.K_r]:
                game()
        
        # runs the start text if the game isn't started
        else:
            surface.blit(text_start, text_startRect)
        
            space = pygame.key.get_pressed()
            if space[pygame.K_SPACE]:
                game_start = True
            
        # draws the sprites
        all_objects.draw(surface)
        
        # screen
        pygame.display.flip()
        
# calls for game function and runs everything
if __name__ == "__main__":
    game()