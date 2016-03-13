#Some basic pygame stuff
import pygame
from pygame.locals import *
from random import randint
from Ship import *
from Weapon import *
from Power import *
from ShipImages import *
from WeaponImages import *

from random import randint

screen_size = (1000, 1000)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Void S3")

clock = pygame.time.Clock()

def ship_loader():
	global my_ship
	my_ship = Ship(screen_size[0]/2, screen_size[1]*0.6, None, None, 3, broadsword_centre_image, False, False, False,"l","r","d","u")

def main():
	done = False
	stars = []
	powerups = []
	ship_loader()


	for i in range (0,1000):
		star_x = randint(0,screen_size[0])
		star_y = randint(0,screen_size[1])

		stars.append([star_x,star_y])

	while not done:
		for event in pygame.event.get():
			#Event Listeners
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
					if event.key == K_RIGHT:
						my_ship.right()
					if event.key == K_LEFT:
						my_ship.left()
					if event.key == K_DOWN:
						my_ship.down()
					if event.key == K_UP:
						my_ship.up()
					if event.key == K_SPACE:
						my_ship.firing = True
					
			if event.type == pygame.KEYUP:
				if event.key == K_RIGHT:
					my_ship.repos()
					my_ship.xspeed = 0
				if event.key == K_LEFT:
					my_ship.repos()
					my_ship.xspeed = 0
				if event.key == K_UP and my_ship.isdown == False:
					my_ship.yspeed = 0
				if event.key == K_DOWN and my_ship.isup == False:
					my_ship.yspeed = 0
				if event.key == K_SPACE:
					my_ship.firing = False

		#Game Logic Below. (Lots of game logic is stored in the classes as well.)
		for i in range(0,len(stars)):
			stars[i][1] += 3
			if stars[i][1] > screen_size[1]:
				stars[i][1] = 0

		if randint(0, 50) == 0:
			sinwavepow = SinWave(randint(0,screen_size[0]), randint(0,screen_size[1]), randint(-2,2), randint(-2,2), 
			None, None, None, None)
			powerups.append(sinwavepow)

		for power_up in powerups:
			if my_ship.x - power_up.x in range(-32, 16) and my_ship.y - power_up.y in range(-32, 23):
				my_ship.xpowerup = power_up.name
				powerups.remove(power_up)
				del(power_up)

		#Drawing Below
		screen.fill((0, 0, 0))

		for i in range(0,len(stars)):
			pygame.draw.circle(screen,(255,255,255),stars[i],0)

		my_ship.update()
		for my_weapon in weapons:
			my_weapon.update()
			if my_weapon.y < 0:
				weapons.remove(my_weapon)
				del(my_weapon)
		for power_up in powerups:
			power_up.update()

		pygame.display.flip()
		clock.tick(30)


	pygame.quit()

main()