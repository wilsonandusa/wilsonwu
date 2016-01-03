'''copyright Xiaosheng Wu  Python game 12/31/2015'''
import pygame, sys
from classes import *
from process import *

pygame.init()
SCREENWIDTH,SCREENHEIGHT = 767,1257
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))  #zero for the flag 32 for color
BackGround = pygame.image.load("images/bg.png") 
Header = pygame.image.load("images/Header.png")
clock = pygame.time.Clock()
FPS = 24 #frames per sec
flag = 2 #randint(0,2)  # if 1 
total_frames = 0#fivesecondinterval = FPS*5

if flag == 0:
	car1 = Car(500,750,64,32,"images/car1.png")#if flag == 0: # both car horizontal movement
	car2 = Car(300,1000,64,32,"images/car2.png")
	bus = Bus(300,300,100,34,"images/bus.png")
	copcar = Cop(SCREENWIDTH-90,SCREENHEIGHT-90,90,45,"images/cop.png")
elif flag==1:
	car1 = Car(0,700,64,32,"images/car1_down.png")#if flag = 1 # both cars vertical movement
	car2 = Car(200,350,64,32,"images/car2_down.png")
	copcar = Cop(SCREENWIDTH-90,SCREENHEIGHT-90,90,45,"images/cop.png")
	bus = Bus(300,300,100,34,"images/bus_down.png")
elif flag == 2:
	car1 = Car(200,100,64,32,"images/car1.png")#blue car vertical  red car horizontal
	car2 = Car(400,300,64,32,"images/car2_down.png")
	car3 = Car(600,500,64,32,"images/car1.png")
	car4 = Car(100,700,64,32,"images/car2_down.png")
	car5 = Car(200,900,64,32,"images/car1.png")
	car6 = Car(300,1100,64,32,"images/car2_down.png")
	car7 = Car(200,900,64,32,"images/car1.png")
	car8 = Car(300,1100,64,32,"images/car2_down.png")
	car9 = Car(200,900,64,32,"images/car1.png")
	car10 = Car(300,1100,64,32,"images/car2_down.png")
	bus1 = Bus(300,300,100,34,"images/bus.png")
	bus2 = Bus(600,300,100,34,"images/bus_down.png")
	bus3 = Bus(100,450,100,34,"images/bus_down.png")

	copcar = Cop(SCREENWIDTH-90,SCREENHEIGHT-90,90,45,"images/cop.png")
#---------------Main Program Loop------------------
while True:
	#PROCESS
	process_onecar(copcar,FPS,total_frames,flag)
	
	copProjectile.movement()
	#LOGIC
	if flag==0:
		copcar.motion(SCREENWIDTH,SCREENHEIGHT)
		Car.update_all(SCREENWIDTH,SCREENHEIGHT)
		Car.bothmovement_x(SCREENWIDTH,SCREENHEIGHT)
		Bus.bothmovement_x(SCREENWIDTH,SCREENHEIGHT)
	elif flag==1:
		copcar.motion(SCREENWIDTH,SCREENHEIGHT)
		Car.update_all(SCREENWIDTH,SCREENHEIGHT)
		Car.bothmovement_y(SCREENWIDTH,SCREENHEIGHT)
		Bus.bothmovement_y(SCREENWIDTH,SCREENHEIGHT)
	elif flag == 2:
		copcar.motion(SCREENWIDTH,SCREENHEIGHT)
		Car.update_all(SCREENWIDTH,SCREENHEIGHT)
		car1.car_motion_x(SCREENWIDTH,SCREENHEIGHT)
		car2.car_motion_y(SCREENWIDTH,SCREENHEIGHT)
		car3.car_motion_x(SCREENWIDTH,SCREENHEIGHT)
		car4.car_motion_y(SCREENWIDTH,SCREENHEIGHT)
		car5.car_motion_x(SCREENWIDTH,SCREENHEIGHT)
		car6.car_motion_y(SCREENWIDTH,SCREENHEIGHT)
		car7.car_motion_x(SCREENWIDTH,SCREENHEIGHT)
		car8.car_motion_y(SCREENWIDTH,SCREENHEIGHT)
		car9.car_motion_x(SCREENWIDTH,SCREENHEIGHT)
		car10.car_motion_y(SCREENWIDTH,SCREENHEIGHT)
		bus1.bus_motion_x(SCREENWIDTH,SCREENHEIGHT)
		bus2.bus_motion_y(SCREENWIDTH,SCREENHEIGHT)
		bus3.bus_motion_y(SCREENWIDTH,SCREENHEIGHT)
	#LOGIC
	total_frames+=1
	#DRAW
	#screen.fill([255,255,255])aaaa
	screen.blit(BackGround,(0,0))
	screen.blit(Header,(0,0))
	BaseClass.allsprites.draw(screen)
	copProjectile.List.draw(screen)
	pygame.display.flip()
	#DRAW

	clock.tick(FPS)
