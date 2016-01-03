import pygame,sys,classes,random

def process_twocars(car1,car2):
	for event in pygame.event.get():    # all possible events to make sure the program close properly
		if event.type == pygame.QUIT:   # if hit the close button
			pygame.quit()
			sys.exit()  

	keys = pygame.key.get_pressed()  # get the key from the keyboard

	if keys[pygame.K_d]: 
		car1.image=pygame.image.load("images/car1.png")   # right
		car1.velx = 5

	elif keys[pygame.K_a]:   #left    #car 1
		car1.image=pygame.image.load("images/car1_left.png")
		car1.velx = -5

	elif keys[pygame.K_w]:   #up
		car1.image=pygame.image.load("images/car1_up.png")
		car1.vely = -5

	elif keys[pygame.K_s]:   #down
		car1.image=pygame.image.load("images/car1_down.png")
		car1.vely = 5

	elif keys[pygame.K_RIGHT]:
		car2.image=pygame.image.load("images/cop_right.png")
		car2.velx = 5

	elif keys[pygame.K_LEFT]:      #car 2
		car2.image=pygame.image.load("images/cop.png")
		car2.velx = -5

	elif keys[pygame.K_UP]:
		car2.image=pygame.image.load("images/cop_up.png")
		car2.vely = -5

	elif keys[pygame.K_DOWN]:
		car2.image=pygame.image.load("images/cop_down.png")
		car2.vely = 5


	else:
		car1.velx = 0
		car1.vely = 0
		car2.velx = 0
		car2.vely = 0

def process_onecar(cop,FPS,total_frames,flag):
	for event in pygame.event.get():    # all possible events to make sure the program close properly
		if event.type == pygame.QUIT:   # if hit the close button
			pygame.quit()
			sys.exit()  

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				classes.copProjectile.fire = not classes.copProjectile.fire

	keys = pygame.key.get_pressed()  # get the key from the keyboard
	cop.velx = 0
	cop.vely = 0

	if keys[pygame.K_RIGHT]: 

		classes.Cop.going_right = True
		classes.Cop.going_left = False
		classes.Cop.going_up = False
		classes.Cop.going_down = False

		cop.image = pygame.image.load("images/cop_right.png")   # right
		
		cop.velx = 5

	elif keys[pygame.K_LEFT]:   #left    #car 1

		classes.Cop.going_right = False
		classes.Cop.going_left = True
		classes.Cop.going_up = False
		classes.Cop.going_down = False

		cop.image = pygame.image.load("images/cop.png")
		
		cop.velx = -5

	elif keys[pygame.K_UP]:   #up

		classes.Cop.going_right = False
		classes.Cop.going_left = False
		classes.Cop.going_up = True
		classes.Cop.going_down = False

		cop.image = pygame.image.load("images/cop_up.png")
		cop.vely = -5

	elif keys[pygame.K_DOWN]:   #down

		classes.Cop.going_right = False
		classes.Cop.going_left = False
		classes.Cop.going_up = False
		classes.Cop.going_down = True

		cop.image = pygame.image.load("images/cop_down.png")

		cop.vely = 5


	if keys[pygame.K_SPACE]:
			
			if classes.Cop.going_right:
				if(classes.copProjectile.fire):
					p = classes.copProjectile(cop.rect.x+75, cop.rect.y+12.5, 90, 45, "images/ticket.png")
				else:
					p = classes.copProjectile(cop.rect.x+60, cop.rect.y+7, 50, 30, "images/stop.png")
				
				p.velx = 8

			elif classes.Cop.going_left:
				if(classes.copProjectile.fire):
					p = classes.copProjectile(cop.rect.x-30, cop.rect.y+12.5, 90, 45, "images/ticket.png")
				else:
					p = classes.copProjectile(cop.rect.x-25, cop.rect.y+7, 50, 30, "images/stop.png")
				p.velx = -8

			elif classes.Cop.going_up:
				if(classes.copProjectile.fire):
					p = classes.copProjectile(cop.rect.x+12.5, cop.rect.y-30, 90, 45, "images/ticket_up.png")
				else:
					p = classes.copProjectile(cop.rect.x-10, cop.rect.y, 50, 30, "images/stop.png")
				p.vely = -8
			else:
				if(classes.copProjectile.fire):
					p = classes.copProjectile(cop.rect.x+12.5, cop.rect.y+70, 90, 45, "images/ticket_up.png")
				else:
					p = classes.copProjectile(cop.rect.x, cop.rect.y+70, 50, 30, "images/stop.png")
				p.vely = 8

		


	spawn(FPS,total_frames,flag)
	collisions()

def spawn(FPS,total_frames,flag):

	four_second = FPS * 7 #every four seconds
	if total_frames % four_second == 0:

		r = random.randint(1,2)
		x = 1

		if r == 2:
			x = 500  # random default number
	
		if flag == 0:
			if r == 1: # red car 
				car = classes.Car(random.randint(0,600),random.randint(0,1000),64,32,"images/car1.png")
				car = classes.Car(random.randint(0,600),random.randint(0,1000),64,32,"images/car2.png")
				#bus = classes.Bus(random.randint(0,600),random.randint(0,1000),100,34,"images/bus.png")
			elif r == 2:
				car = classes.Car(random.randint(0,600),random.randint(0,1000),64,32,"images/car2.png")
				bus = classes.Bus(random.randint(0,600),random.randint(0,1000),100,34,"images/bus.png")
		elif flag == 1:
			if r == 1:
				car = classes.Car(random.randint(0,600),random.randint(0,1000),64,32,"images/car1_down.png")
				car = classes.Car(random.randint(0,600),random.randint(0,1000),64,32,"images/car2.png")
			elif r == 2:
				car = classes.Car(random.randint(0,600),random.randint(0,1000),64,32,"images/car2_down.png")
				bus = classes.Bus(random.randint(0,600),random.randint(0,1000),100,34,"images/bus_down.png")
		else:
			k=0

def collisions():

	for car in classes.Car.List:

		if pygame.sprite.spritecollide(car, classes.copProjectile.List, False):  # if true collide

			if classes.copProjectile.fire:
				car.health -= car.half_health
			else:
				car.velx = 0
				car.vely = 0

	for proj in classes.copProjectile.List:

		if pygame.sprite.spritecollide(proj, classes.Car.List, False):
			proj.rect.x = 2 * - proj.rect.width
			proj.rect.y = 2 * - proj.rect.height    # to avoid collision
			print("Hit!")
			proj.destroy()
			
	


