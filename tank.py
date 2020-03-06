import pygame
import random as rd
from math import cos, sin, asin, sqrt, pi

pygame.init()

width = 600
height = 600

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("TANKOS")

class tank(object):
	def __init__(self, x, y, angle, color):
		self.x = x
		self.y = y
		self.angle = angle
		self.w = 30
		self.l = 50
		self.v = 5
		self.color = color
		self.d = sqrt(self.w**2 + self.l**2)
		self.gamma = asin(self.w/self.d)
		
	def display(self):
		d = self.d
		angle = self.angle
		gamma = self.gamma
		y = self.y
		x = self.x
		A = (x + (d/2)*cos(angle+gamma), y + (d/2)*sin(angle+gamma))
		B = (x + (d/2)*cos(angle-gamma), y + (d/2)*sin(angle-gamma))
		C = (x + (d/2)*cos(angle+gamma-pi), y + (d/2)*sin(angle+gamma-pi))
		D = (x + (d/2)*cos(angle-gamma+pi), y + (d/2)*sin(angle-gamma+pi))
		pygame.draw.polygon(win, self.color, [A,B,C,D])
	
	def rotate(self, alpha):
		self.angle += alpha
		
	def move(self, dir):
		self.x += 0.3*dir*cos(self.angle)
		self.y += 0.3*dir*sin(self.angle)
		
run = True
green = tank(rd.uniform(50,width-50), rd.uniform(50, height-50), rd.uniform(0, 2*pi), (0,255,0))
red = tank(rd.uniform(50,width-50), rd.uniform(50, height-50), rd.uniform(0, 2*pi), (255,0,0))

while run:
	
	win.fill((255,255,255))
	
	for event in pygame.event.get(): #event = anything user does
		if event.type == pygame.QUIT: #if I hit X it closes
			run = False
				
	keys = pygame.key.get_pressed()
	
	# green controls
	if keys[pygame.K_LEFT]:
		green.rotate(-4/10E2)
	if keys[pygame.K_RIGHT]:
		green.rotate(4/10E2)
	if keys[pygame.K_UP]:
		green.move(1)
	if keys[pygame.K_DOWN]:
		green.move(-1)
	
	# red controls
	if keys[pygame.K_a]:
		red.rotate(-4/10E2)
	if keys[pygame.K_d]:
		red.rotate(4/10E2)
	if keys[pygame.K_w]:
		red.move(1)
	if keys[pygame.K_s]:
		red.move(-1)
	
	green.display()
	red.display()
	
	pygame.display.update()
	
pygame.quit()