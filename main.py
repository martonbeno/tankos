import pygame
from Tank import Tank
from Bullet import Bullet
from colors import *

pygame.init()
now = pygame.time.get_ticks #number of milliseconds passed from start of the game

o1 = Tank(400, 400, born=now(), color="green") #center_x, center_y
objects = [o1]

W = 800
H = 600

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("tankos játék")

bullet_speed = 10
move_speed = 6
rotate_speed = .1

clock = pygame.time.Clock()
run = True

while run:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	buttons_pressed = pygame.key.get_pressed()
	
	#exit -----------------------------
	if buttons_pressed[pygame.K_ESCAPE]:
		run = False
	
	#debug ----------------------------
	if buttons_pressed[pygame.K_SPACE]:
		[print(object) for object in objects]
	
	#move -----------------------------
	if buttons_pressed[pygame.K_UP]:
		o1.move("forward", move_speed)
	if buttons_pressed[pygame.K_DOWN]:
		o1.move("backwards", move_speed)
	if buttons_pressed[pygame.K_RIGHT]:
		o1.rotate(rotate_speed)
	if buttons_pressed[pygame.K_LEFT]:
		o1.rotate(-rotate_speed)
	
	#shoot ----------------------------
	if buttons_pressed[pygame.K_a]:
		if o1.last_shot + o1.load_time < now(): # if the tank is loaded
			objects.append(o1.shoot(now()))
	
	#bullet bounce on walls--------------------
	for object in objects:
		if object.type is "bullet" and (object.x > W or object.x < 0):
			object.bounce("horizontal")
		if object.type is "bullet" and (object.y > H or object.y < 0):
			object.bounce("vertical")
	
	#automatic actions ----------------
	for object in objects:
		if object.type is "bullet":
			object.bullet_move()
	
	#draw -----------------------------
	screen.fill(colors["white"])
	for object in objects:
		if object.type is "bullet":
			pygame.draw.ellipse(screen, colors[object.color], (object.x, object.y, object.width, object.height))
		else:
			pygame.draw.polygon(screen, colors[object.color], object.get_corners())
	
	pygame.display.update()

pygame.quit()