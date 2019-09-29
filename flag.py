import pygame

pygame.init()
size = width, heigth = 300, 300
screen = pygame.display.set_mode(size)

def draw():
    rect_color = pygame.Color('red')
    rect_width = 0
    rect_point = [[10,10], [280, 280]]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

draw()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()