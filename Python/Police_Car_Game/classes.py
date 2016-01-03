import pygame,math
from random import randint

class BaseClass(pygame.sprite.Sprite):
	allsprites = pygame.sprite.Group()  #
	def __init__(self,x,y,width,height,image_string):#inherite from above pygame class
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self)
		self.image = pygame.image.load(image_string)
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = width
		self.height = height
		self.X=randint(0,767)
		self.Y=randint(0,1257)

	def destroy(self,className):
		className.List.remove(self)
		BaseClass.allsprites.remove(self)
		del self
#--------------------------------Cop------------------------------------------------
class Cop(BaseClass):
	"""docstring for Cop"""
	List = pygame.sprite.Group()
	going_right = True

	def __init__(self,x,y,width,height,image_string):
		BaseClass.__init__(self,x,y,width,height,image_string)
		Cop.List.add(self)  # allsprites
		self.velx = 0
		self.vely = 0

	def motion(self,SCREENWIDTH,SCREENHEIGHT):
		predicted_location_x = self.rect.x + self.velx
		predicted_location_y = self.rect.y + self.vely

		if predicted_location_x<0:
			self.velx = 0
		elif predicted_location_x+self.width>SCREENWIDTH:
			self.velx = 0

		elif predicted_location_y<0:
			self.vely = 0
		elif predicted_location_y+self.width>SCREENHEIGHT:
			self.vely = 0

		
		self.rect.x += self.velx
		self.rect.y += self.vely

#--------------------------------Car------------------------------------------------
class Car(BaseClass):
	List = pygame.sprite.Group()
	def __init__(self,x,y,width,height,image_string):
		BaseClass.__init__(self,x,y,width,height,image_string)
		Car.List.add(self) 
		self.health = 100
		self.half_health = self.health/2
		self.velx = randint(2,3)
		self.vely = randint(2,3)
		self.amplitude,self.period = randint(5,8),randint(7,8)/100.0
	
	@staticmethod
	def update_all(SCREENWIDTH,SCREENHEIGHT):
		#print("update_all")
		for car in Car.List:
			if car.health<=0:
				car.destroy(Car)



	def car_motion_x(self,SCREENWIDTH,SCREENHEIGHT):

		#timer = pygame.time.get_ticks()
		#end = timer + 2000

				if self.rect.x + self.width>SCREENWIDTH or self.rect.x<0:
					self.image = pygame.transform.flip(self.image,True,False)#horizontal flip
					self.velx = -self.velx

				if self.rect.y + self.width>SCREENHEIGHT or self.rect.y<0:
					self.image = pygame.transform.flip(self.image,False,True)#vertical flip
					self.vely = -self.vely

				self.rect.x += self.velx
				self.rect.y = self.amplitude*math.sin(self.period*self.rect.x)+self.Y
	
	def car_motion_y(self,SCREENWIDTH,SCREENHEIGHT):

		#timer = pygame.time.get_ticks()
		#end = timer + 2000
				if self.rect.x + self.width>SCREENWIDTH or self.rect.x<0:
					self.image = pygame.transform.flip(self.image,True,False)#horizontal flip
					self.velx = -self.velx

				if self.rect.y + self.width>SCREENHEIGHT or self.rect.y<0:
					self.image = pygame.transform.flip(self.image,False,True)#vertical flip
					self.vely = -self.vely

				self.rect.y += self.vely
				self.rect.x = self.amplitude*math.sin(self.period*self.rect.y)+self.X\
	
	@staticmethod
	def bothmovement_x(SCREENWIDTH,SCREENHEIGHT):
		
		for car in Car.List:
					car.car_motion_x(SCREENWIDTH,SCREENHEIGHT)
	@staticmethod
	def bothmovement_y(SCREENWIDTH,SCREENHEIGHT):
		
		for car in Car.List:
					car.car_motion_y(SCREENWIDTH,SCREENHEIGHT)

#--------------------------------BUS------------------------------------------------
class Bus(BaseClass):
	List = pygame.sprite.Group()
	def __init__(self,x,y,width,height,image_string):
		BaseClass.__init__(self,x,y,width,height,image_string)
		Bus.List.add(self) 
		self.velx = 3
		self.vely = 3

	def bus_motion_x(self,SCREENWIDTH,SCREENHEIGHT):

		#timer = pygame.time.get_ticks()
		#end = timer + 2000

				if self.rect.x + self.width>SCREENWIDTH or self.rect.x<0:
					self.image = pygame.transform.flip(self.image,True,False)#horizontal flip
					self.velx = -self.velx

				if self.rect.y + self.width>SCREENHEIGHT or self.rect.y<0:
					self.image = pygame.transform.flip(self.image,False,True)#vertical flip
					self.vely = -self.vely

				self.rect.y += 0
				self.rect.x += self.velx
	
	def bus_motion_y(self,SCREENWIDTH,SCREENHEIGHT):

		#timer = pygame.time.get_ticks()
		#end = timer + 2000
				if self.rect.x + self.width>SCREENWIDTH or self.rect.x<0:
					self.image = pygame.transform.flip(self.image,True,False)#horizontal flip
					self.velx = -self.velx

				if self.rect.y + self.width>SCREENHEIGHT or self.rect.y<0:
					self.image = pygame.transform.flip(self.image,False,True)#vertical flip
					self.vely = -self.vely

				self.rect.y += self.vely
				self.rect.x += 0

	@staticmethod
	def bothmovement_x(SCREENWIDTH,SCREENHEIGHT):
		
		for bus in Bus.List:
					bus.bus_motion_x(SCREENWIDTH,SCREENHEIGHT)
	@staticmethod
	def bothmovement_y(SCREENWIDTH,SCREENHEIGHT):
		
		for bus in Bus.List:
					bus.bus_motion_y(SCREENWIDTH,SCREENHEIGHT)

	'''@staticmethod
	def randommovement(SCREENWIDTH,SCREENHEIGHT,total_frames):
		flag = total_frames%2
		for car in Car.List:
					car.car_motion_y(SCREENWIDTH,SCREENHEIGHT)'''

#-------------------------------Cop Projectile------------------------------------------------
class copProjectile(pygame.sprite.Sprite):

	List = pygame.sprite.Group()
	normal_list = []
	fire = True

	def __init__(self, x, y, width, height, image_string):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_string)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.width = width
		self.height = height

		try:
			last_element = copProjectile.normal_list[-1] # the last element
			difference_x = abs(self.rect.x - last_element.rect.x) # detect overlapping fire
			difference_y = abs(self.rect.y - last_element.rect.y)
			if difference_x < self.width and  difference_y < self.height:
				return 

		except Exception:
			pass

		copProjectile.normal_list.append(self)
		copProjectile.List.add(self)

		self.velx = 0
		self.vely = 0

	def movement():
		for projectile in copProjectile.List:
			projectile.rect.x += projectile.velx
			projectile.rect.y += projectile.vely

	def destroy(self):
		copProjectile.List.remove(self)
		copProjectile.normal_list.remove(self)
		del self
