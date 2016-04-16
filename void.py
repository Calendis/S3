#Some basic pygame stuff
import pygame
from pygame.locals import *
from random import randint
from Ship import *
from Weapon import *
from Power import *
from ShipImages import *
from Enemy import *	

from random import randint

screen_size = (1000, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Void S3")

clock = pygame.time.Clock()

def ship_loader():
	global my_ship
	my_ship = Ship(screen_size[0]/2, screen_size[1]*0.6, None, None, 3, broadsword_centre_image,
		False, "xpow", "ypow", "l", "r", "d", "u", "hp", "can_shoot", "delay", "fire_speed")


def main():
	done = False
	stars = []
	powerups = []
	enemies = []
	swallows = []
	ship_loader()
	
	starcount = 1000


	for i in range (0,starcount):
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
					my_ship.can_shoot = True

		#Game Logic Below. (Lots of game logic is stored in the classes as well.

		if randint(0,100) == 0:#Spawn enemies
			new_sparrow = Sparrow(randint(0,screen_size[0]),-32,"xspeed","yspeed","img","imgno", "fire","hp")
			enemies.append(new_sparrow)
		if randint(0,300) == 0:
			new_swallow = Swallow(randint(0,screen_size[0]),-32,"xspeed","yspeed","img","imgno", "fire","hp")
			enemies.append(new_swallow)
			swallows.append(new_swallow)

		for i in range(0,len(stars)):#This for loop is for the background stars
			stars[i][1] += 3
			if stars[i][1] > screen_size[1]:
				stars[i][1] = 0

		if randint(0, 50) == 0:#This spawns in powerups
			sinwavepow = SinWave(randint(0,screen_size[0]), randint(0,screen_size[1]), randint(-2,2), randint(-2,2), 
			"name", "img", "powspeed", "imgcount", "imgs")
			powerups.append(sinwavepow)


		for power_up in powerups:#This for loop detects collisions between powerups and things
			if my_ship.x - power_up.x in range(-32, 16) and my_ship.y - power_up.y in range(-32, 23):
				my_ship.xpowerup = power_up.name
				my_ship.fire_speed = power_up.pow_speed
				powerups.remove(power_up)

		for laser in weapons:#This loop detects collisions between lasers and powerups
			for power_up in powerups:
				if laser.x - power_up.x in range(-8,16) and laser.y - power_up.y in range(-16,16):
					powerups.remove(power_up)
					weapons.remove(laser)
					laser.y = 100

			for enemy in enemies:
				if laser.x - enemy.x in range(-16,32) and laser.y - enemy.y in range(-24,32):
					try:
						weapons.remove(laser)
					except:
						pass
					else:
						pass
					enemy.hp -= 1
					if enemy.hp < 1:
						enemies.remove(enemy)

		for swallow in swallows:#This loop allows swallows to follow your x position
			if my_ship.x > swallow.x:
				swallow.moveright()
			if my_ship.x < swallow.x:
				swallow.moveleft()
			if my_ship.x == swallow.x:
				swallow.repos()


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
		for enemy in enemies:
			enemy.update()

		pygame.display.flip()
		clock.tick(40)


	pygame.quit()

main()