import pygame

game_display = pygame.display.set_mode((800, 600))

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
grey = (50,50,50)

statingPosition_x = 10
statingPosition_y = 20

pygame.draw.rect(game_display, grey, [5, 20, 5, 400])
pygame.draw.rect(game_display, blue, [statingPosition_x, statingPosition_y, 100, 200])
pygame.draw.rect(game_display, white, [statingPosition_x + 100, statingPosition_y, 100, 200])
pygame.draw.rect(game_display, red, [statingPosition_x + 200, statingPosition_y, 100, 200])
            
pygame.display.update()
