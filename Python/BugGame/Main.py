'''copyright Xiaosheng Wu  Python game 12/31/2015'''
import pygame, sys
from classes import *


pygame.init()
WIDTH,HEIGHT = 640,360
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)  #zero for the flag 32 for color

clock = pygame.time.Clock()
FPS = 24 #frames per sec

#fivesecondinterval = FPS*5
bug = Bug(0,0,72,76,"images/bug.png")
bug2 = Bug(100,200,72,76,"images/bee.png")
bug3 = Bug(0,100,72,76,"images/bug.png")
i = 0
#---------------Main Program Loop------------------
while True:
	for event in pygame.event.get():    # all possible events to make sure the program close properly
		if event.type == pygame.QUIT:   # if hit the close button
			pygame.quit()
			sys.exit()  
	#PROCESS
	#LOGIC
	bug.motion()
	#LOGIC
	bug2.motion()
	#bug3.motion()
	#DRAW
	i+=10
	if i>255:
		i=i%255
	screen.fill((123,i,123))
	BaseClass.allsprites.draw(screen)

	pygame.display.flip()
	#DRAW

	clock.tick(FPS)
