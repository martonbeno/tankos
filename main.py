import pygame
from Object import *
from colors import *

o1 = Object(400, 400, 100, 20) #center_x, center_y, height, width
objects = [o1]



pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("tankos játék")

clock = pygame.time.Clock()

move_speed = 6
rotate_speed = 2

run = True

while run:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	buttons_pressed = pygame.key.get_pressed()

	if buttons_pressed[pygame.K_ESCAPE]:
		run = False	
	if buttons_pressed[pygame.K_UP]:
		o1.move("up", move_speed)
	if buttons_pressed[pygame.K_DOWN]:
		o1.move("down", move_speed)
	if buttons_pressed[pygame.K_RIGHT]:
		o1.rotate(rotate_speed)
	if buttons_pressed[pygame.K_LEFT]:
		o1.rotate(-rotate_speed)
	
	if buttons_pressed[pygame.K_SPACE]:
		[print(o) for o in objects]

	screen.fill((255,255,255))
	
	for o in objects:
		pygame.draw.polygon(screen, BLACK, o.get_corners())
	
	pygame.display.update()

pygame.quit()