import pygame
from Tank import Tank
from Bullet import Bullet
from Wall import *
from colors import *
from random import randint
import functions

W = 12
H = 10
cell = 50


pygame.init()
now = pygame.time.get_ticks #number of milliseconds passed from start of the game

objects = []

o1 = Tank(400, 400, born=now(), color="green") #center_x, center_y
objects.append(o1)

walls = []

for i in range(W):
	for j in range(H):
		for wallside in new_wall(i*cell, j*cell, [0,0,0,0]):
			walls.append(wallside)

for wallside in new_wall(3*cell, 3*cell, [1,0,0,1]):
	walls.append(wallside)
for wallside in new_wall(3*cell, 4*cell, [0,1,0,1]):
	walls.append(wallside)
for wallside in new_wall(2*cell, 4*cell, [1,1,1,1]):
	walls.append(wallside)
for wallside in new_wall(2*cell, 3*cell, [0,0,1,1]):
	walls.append(wallside)

objects = objects + walls

screen = pygame.display.set_mode((W*cell,H*cell))
pygame.display.set_caption("tankos játék")

bullet_speed = 10
move_speed = 6
rotate_speed = .1
max_bullets_per_tank = 5

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
	
	#kill the old --------------------
	for object in objects:
		if object.is_alive and object.born + object.lifespan < now():
			object.kill()
			objects.remove(object)
	
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
			if len([o for o in objects if o.type == "bullet" and o.tank == o1]) < max_bullets_per_tank:
				objects.append(o1.shoot(now()))
		
	
	#bullet bounce on walls------------
	for object in objects:
		if object.type is "bullet" and (object.x > W*cell or object.x < 0):
			object.bounce("horizontal")
		if object.type is "bullet" and (object.y > H*cell or object.y < 0):
			object.bounce("vertical")
			
	#collision -------------------------
	for object in objects:
		if o1.collide(object) and object.type == "bullet":
			o1.kill()
			object.kill()
			objects.remove(object)
		for wall in walls:
			if object.type is "bullet" and object.collide(wall):
				object.bounce(wall.allignment)
	
	#automatic actions ----------------
	for object in objects:
		if object.type is "bullet":
			object.bullet_move()
	
	#draw -----------------------------
	screen.fill(colors["white"])
	for object in objects:
		if object.type is "bullet":
			pygame.draw.ellipse(screen, colors[object.color], (object.x, object.y, object.height, object.width))
		else:
			pygame.draw.polygon(screen, colors[object.color], object.get_corners())
			'''tank1 = pygame.image.load(o1.image_file)
			screen.blit(tank1, (o1.x + o1.height/2, o1.y + o1.width/2))
			pygame.transform.rotate(tank1, o1.angle)'''
	
	pygame.display.update()

pygame.quit()