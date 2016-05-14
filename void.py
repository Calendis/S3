#Some basic pygame stuff
import pygame
from pygame.locals import *
from random import randint
from Ship import *
from Weapon import *
from Power import *
from Enemy import *
from Coins import *

from ShipImages import *
from GuiImages import *

from MainSoundLoader import *

from random import randint

pygame.font.init()
font_path = "fonts/PressStart2P.ttf"
font_size= 10
screen_size = (1000, 700)
font = pygame.font.Font(font_path, font_size)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Void S3")

clock = pygame.time.Clock()

def togglepause():
	global paused
	if paused == True:
		paused = False
	elif paused == False:
		paused = True


def colour_control(integer1):
	if integer1 > 255:
		integer1 = 255
	if integer1 < 0:
		integer1 = 0
	
	return integer1

def colour_control2(integer1):
	if integer1 > 255:
		integer1 = integer1 - 255
	else:
		integer1 = 0

	return integer1

def colour_control3(integer1):
	if integer1 < 512:
		integer1 = 255 - integer1
	elif integer1 >= 512:
		integer1 = integer1 - 512

	return integer1

def heatbar_metre_control(integer1):
	if integer1 > heatbarstart + barlength:
		integer1 = heatbarstart + barlength

	return integer1

def powerbar_metre_control(integer1):
	integer1 = powerbarstart + my_ship.powerleft/my_ship.powermax * barlength
	if integer1 > powerbarstart + barlength:
		integer1 = powerbarstart + barlength

	return integer1

def healthbar_metre_control(integer1):
	integer1 = healthbarstart + my_ship.hp/100 * barlength
	if integer1 > healthbarstart + barlength:
		integer1 = powerbarstart + barlength

	return integer1

def ship_loader():
	global my_ship
	my_ship = Ship(screen_size[0]/2, screen_size[1]*0.6, None, None, 3.0, broadsword_centre_image,
		False, "xpow", "ypow", "l", "r", "d", "u", "hp", "can_shoot", "elapser", "fire_delay", "overheat",
		"coolantbonus", "powerleft", "powermax")


def main():
	done = False

	global paused
	paused = False

	stars = []
	powerups = []
	enemies = []
	swallows = []
	coins = []

	score = 0
	scoretext=font.render("Score: "+str(score), 0,(160,160,160))

	ship_loader()
	
	starcount = 1000

	global barlength
	barlength = 44
	global heatbarstart
	heatbarstart = 82
	heatmultiplier = 255/barlength
	global powerbarstart
	powerbarstart = 147
	global healthbarstart
	healthbarstart = 212

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
						my_ship.isright = True
					if event.key == K_LEFT:
						my_ship.isleft = True
					if event.key == K_DOWN:
						my_ship.isdown = True
					if event.key == K_UP:
						my_ship.isup = True
					if event.key == K_x:
						my_ship.firing = True
					if event.key == K_p:
						togglepause()
					
			if event.type == pygame.KEYUP:
				if event.key == K_RIGHT:
					my_ship.repos()
					my_ship.isright = False
				if event.key == K_LEFT:
					my_ship.repos()
					my_ship.isleft = False
				if event.key == K_UP:
					my_ship.isup = False
				if event.key == K_DOWN:
					my_ship.isdown = False
				if event.key == K_x:
					my_ship.firing = False
					if my_ship.overheat < 44:
						my_ship.can_shoot = True

		#Game Logic Below. (Lots of game logic is stored in the classes as well.

		'''Start of code that spawns in enemies'''

		if randint(0,150) == 0:
			new_sparrow = Sparrow(randint(0,screen_size[0]),-32,"xspeed","yspeed","img","imgno", "fire","hp","points","drops")
			enemies.append(new_sparrow)
		if randint(0,300) == 0:
			new_swallow = Swallow(randint(0,screen_size[0]),-32,"xspeed","yspeed","img","imgno", "fire","hp","points","drops")
			enemies.append(new_swallow)
			swallows.append(new_swallow)
		if randint(0,580) == 0:
			new_cardinal = Cardinal(randint(0,screen_size[0]),-32,"xspeed","yspeed","img","imgno", "fire","hp","points","drops")
			enemies.append(new_cardinal)

		'''End of code that spawns in enemies'''

		
		for i in range(0,len(stars)):#This for loop is for the background stars
			stars[i][1] += 3
			if stars[i][1] > screen_size[1]:
				stars[i][1] = 0

		powerupgen = randint(0,16383)
		if powerupgen in range(0,3):
			new_powerup = SinWave(randint(0,screen_size[0]), randint(0,screen_size[1]), randint(-2,2), randint(-2,2), 
			"name", "img", "powspeed", "coolant", "duration", "imgcount", "imgs")
			powerups.append(new_powerup)
		elif powerupgen in range(4,9):
			new_powerup = Super(randint(0,screen_size[0]), randint(0,screen_size[1]), randint(-2,2), randint(-2,2), 
			"name", "img", "powspeed", "coolant", "duration", "imgcount", "imgs")
			powerups.append(new_powerup)
		elif powerupgen in range(9, 11):
			new_powerup = IceI(randint(0,screen_size[0]), randint(0,screen_size[1]), randint(-2,2), randint(-2,2), 
			"name", "img", "powspeed", "coolant", "duration", "imgcount", "imgs")
			powerups.append(new_powerup)


		for power_up in powerups:#This for loop detects collisions between powerups and things
			if my_ship.x - power_up.x in range(-32, 16) and my_ship.y - power_up.y in range(-32, 23):
				power0.play()
				my_ship.xpowerup = power_up.name
				my_ship.fire_delay = power_up.pow_speed
				my_ship.coolantbonus = power_up.coolant
				my_ship.powerleft = power_up.duration
				my_ship.powermax = power_up.duration
				powerups.remove(power_up)

		for laser in weapons:#This loop detects collisions between lasers and powerups
			for power_up in powerups:
				if laser.x - power_up.x in range(-8,16) and laser.y - power_up.y in range(-16,16):
					
					for i in range(0,100):
						if randint(0,100) < 30:
							new_GoldCoin = GoldCoin(power_up.x, power_up.y, random()*randint(-2,2), random()*randint(1,2), "coinimg", "imagecount", "imgs", "value")
							coins.append(new_GoldCoin)

					explosion1.play()
					powerups.remove(power_up)
					weapons.remove(laser)

			for enemy in enemies:#This loop detects collisions between lasers and enemies
				if laser.x - enemy.x in range(-16,32) and laser.y - enemy.y in range(-24,32):
					try:
						weapons.remove(laser)
					except:
						pass
					else:
						pass
					enemy.hp -= 1
					if enemy.hp < 1:
						explosion1.play()

						for i in range(int(enemy.points/(1/enemy.drops))):
							if randint(0,enemy.points) > 1000:
								new_PlatinumCoin = PlatinumCoin(enemy.x, enemy.y, random()*randint(-2,2), random()*randint(1,2), "coinimg", "imagecount", "imgs", "value")
								coins.append(new_PlatinumCoin)
							elif randint(0,enemy.points) > 75:
								new_GoldCoin = GoldCoin(enemy.x, enemy.y, random()*randint(-2,2), random()*randint(1,2), "coinimg", "imagecount", "imgs", "value")
								coins.append(new_GoldCoin)
							elif randint(0,enemy.points) > 25:
								new_SilverCoin = SilverCoin(enemy.x, enemy.y, random()*randint(-2,2), random()*randint(1,2), "coinimg", "imagecount", "imgs", "value")
								coins.append(new_SilverCoin)
							elif randint(0,enemy.points) > 0:
								new_CopperCoin = CopperCoin(enemy.x, enemy.y, random()*randint(-2,2), random()*randint(1,2), "coinimg", "imagecount", "imgs", "value")
								coins.append(new_CopperCoin)
						
						enemies.remove(enemy)

		for swallow in swallows:#This loop allows swallows to follow your x position
			if swallow.y < my_ship.y - 16:
				if my_ship.x > swallow.x:
					swallow.moveright()
				if my_ship.x < swallow.x:
					swallow.moveleft()
				if my_ship.x == swallow.x:
					swallow.repos()

		for enemy in enemies:#This loop detects collisions between enemies and the player
			if enemy.x - my_ship.x in range(-32, 16) and enemy.y - my_ship.y in range(-32, 23):
				my_ship.hp -= enemy.hp*10
				explosion1.play()
				enemies.remove(enemy)

				if my_ship.hp < 0:
					my_ship.hp = -1
					my_ship.die()

		for coin in coins:#This loops detects collisions between coins and the player
			if int(coin.x*10) - int(my_ship.x*10) in range(0, 320) and int(coin.y*10) - int(my_ship.y*10) in range(0,320):
				#print("coin: " + str(coin.x)+", "+str(coin.y))
				#print("ship: " + str(my_ship.x)+", "+str(my_ship.y))
				points0.play()
				score += coin.value
				scoretext=font.render("Score: "+str(score), 1,(160,160,160))
				coins.remove(coin)
			


		#Drawing Below
		
		#Fills the screen with black
		screen.fill((0, 0, 0))

		#Draws the stars
		for i in range(0,len(stars)):
			pygame.draw.circle(screen,(255,255,255),stars[i],0)

		#Draws ships, enemies, and coins
		for coin in coins:
			coin.update()
			if coin.y < -20 or coin.y > 720:#This conditional removes off-screen coins. X coord is not needed because coins bounce off of the x
				coins.remove(coin)
				del(coin)

		my_ship.update()
		for my_weapon in weapons:
			my_weapon.update()
			if my_weapon.y < -20:#This conditional checks if a laser is off of the screen and deletes it
				weapons.remove(my_weapon)
				del(my_weapon)
		
		for power_up in powerups:
			power_up.update()
			if power_up.y < -20 or power_up.y > 720 or power_up.x < -20 or power_up.x > 1020:
				powerups.remove(power_up)
				del(power_up)

		for enemy in enemies:
			enemy.update()

		#Draws the HUD image
		screen.blit(hud_image,(0,screen_size[1]-100))
		
		#Draws the overheat monitor
		pygame.draw.rect(screen,(colour_control(my_ship.overheat*heatmultiplier),colour_control(colour_control3(my_ship.overheat*heatmultiplier)),colour_control(colour_control2(my_ship.overheat*heatmultiplier))),
			(heatbar_metre_control(heatbarstart+my_ship.overheat),638,1,7))

		#Draws the power remaining monitor
		pygame.draw.rect(screen,(255-colour_control(my_ship.powerleft/my_ship.powermax*255),colour_control(my_ship.powerleft/my_ship.powermax*255),0),
			(powerbar_metre_control(powerbarstart-my_ship.powerleft),638,1,7))

		#Draws the health remaining monitor
		pygame.draw.rect(screen,(255-colour_control(my_ship.hp/100*255),colour_control(my_ship.hp/100*255),0),
			(healthbar_metre_control(healthbarstart-my_ship.hp),638,1,7))

		#Draws the score
		screen.blit(scoretext, (300, 638))
		
		pygame.display.flip()
		clock.tick(40)


	pygame.quit()

main()