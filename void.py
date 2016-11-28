#Some basic pygame stuff
import shelve
import pygame
from pygame.locals import *
from random import randint
from time import time

from Ship import *
from Weapon import *
from EnemyWeapon import *
from Power import *
from Enemy import *
from Coins import *
from Formation import *
from Upgrade import *

from SpawnHelper import *

from ShipImages import *
from GuiImages import *
from Button import *

from MainSoundLoader import *

from random import randint

pygame.font.init()
font_path = "fonts/PressStart2P.ttf"
font_size= 10
screen_size = (1000, 700)
font = pygame.font.Font(font_path, font_size)
font2 = pygame.font.Font(font_path, 30)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Void S3")

clock = pygame.time.Clock()

def togglepause(paused):
	if paused == True:
		paused = False
	elif paused == False:
		paused = True

	return paused

def highscore(hs_table, score):
	if score >= hs_table:
		hs_table = shelve.open("highscores.sav")
		hs_table["highscore"] = score
		hs_table.close()


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
	if integer1 > HEATBARSTART + BARLENGTH:
		integer1 = HEATBARSTART + BARLENGTH

	return integer1

def powerbar_metre_control(integer1):
	integer1 = POWERBARSTART + my_ship.powerleft/my_ship.powermax * BARLENGTH
	if integer1 > POWERBARSTART + BARLENGTH:
		integer1 = POWERBARSTART + BARLENGTH

	return integer1

def healthbar_metre_control(integer1):
	integer1 = HEALTHBARSTART + my_ship.hp/100 * BARLENGTH
	if integer1 > HEALTHBARSTART + BARLENGTH:
		integer1 = POWERBARSTART + BARLENGTH

	return integer1

def main():
	done = False
	menuscreen = True

	powerup_time_elapser = time()
	upgrade_time_elapser = time()
	crow_elapser = time()

	paused = False
	shopping = False

	shop_appeared = False

	global allsprites
	allsprites = []

	stars = []

	swallows = []
	crows = []

	buttons = []

	play_button = PlayButton(100, 200)
	buttons.append(play_button)

	score = 0
	try:
		hs_table = shelve.open("highscores.sav")
		hs_table = hs_table["highscore"]
	except:
		hs_table = 0

	scoretext = font.render("Score: "+str(score), 0,(160,160,160))
	highscoretext = font.render("High Score: "+str(hs_table), 0,(100,200,200))

	pausedtext = font2.render("Game Paused", 0,(255,255,255))

	gameovertext = font2.render("Game Over", 0,(255,255,255))

	global my_ship
	my_ship = Ship(screen_size[0]/2, screen_size[1]*0.6, 3.0, "none", "none", Stream)

	allsprites.append(my_ship)

	STARCOUNT = 1000

	global BARLENGTH
	BARLENGTH = 44
	global HEATBARSTART
	HEATBARSTART = 82
	HEATMULTIPLIER = 255/BARLENGTH
	global POWERBARSTART
	POWERBARSTART = 147
	global HEALTHBARSTART
	HEALTHBARSTART = 212

	POWERUP_TYPES = [SinWave, Super, IceI]
	UPGRADE_TYPES = [Damage0, Backfire]

	SHOW_HITBOXES = False

	for i in range (0,STARCOUNT):
		star_x = randint(0,screen_size[0])
		star_y = randint(0,screen_size[1])

		stars.append([star_x,star_y])

	while menuscreen and not paused and not done:
		for event in pygame.event.get():
			#Input Handling
			if event.type == pygame.QUIT:
				done = True
			if event.type == MOUSEBUTTONDOWN:
				for button in buttons:
					if button.hovered == True:
						button.when_clicked()

						if button.__class__ == PlayButton:
							menuscreen = False

		#Drawing below
		screen.fill((0,0,0))

		for button in buttons:
			button.update()

		screen.blit(logo_image,(screen_size[0]/2-374/2,10))

		pygame.display.flip()
		clock.tick(40)


	while True and not done:


		while not done and not menuscreen and not paused and not shopping:
			for event in pygame.event.get():
				#Input handling
				if event.type == pygame.QUIT:
					done = True
				if event.type == pygame.KEYDOWN:
						if event.key == K_RIGHT:
							if my_ship.x < 1000-32:
								my_ship.isright = True
								my_ship.hb_follow()
						if event.key == K_LEFT:
							my_ship.isleft = True
							my_ship.hb_follow()
						if event.key == K_DOWN:
							if my_ship.y < 564:
								my_ship.isdown = True
								my_ship.hb_follow()
						if event.key == K_UP:
							if my_ship.y >= 4:
								my_ship.isup = True
								my_ship.hb_follow()

						if event.key == K_x:
							my_ship.firing = True

						if event.key == K_p:
							paused = togglepause(paused)

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
							pass#my_ship.can_shoot = True

			#Game Logic Below. Lots of game logic is stored in the classes as well.

			for i in range(len(weapons)):
				try:
					allsprites.append(weapons[i])
					weapons.remove(weapons[i])
				except:
					pass
				else:
					pass


			'''Start of code that spawns in enemies'''

			if score > LEVEL8:

				if randint(0,9000) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						allsprites.append(new_formation_enemy)

				if randint(0,580) == 0:
					new_formation = DoubleCrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						crows.append(new_formation_enemy)
						allsprites.append(new_formation_enemy)

				if randint(0,800) == 0:
					new_formation = AdvancedWing()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == SwallowMKII:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,550) == 0:
					new_formation = SingleCardinal()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						allsprites.append(new_formation_enemy)

				if randint(0,1600) == 0:
					new_formation = AdvancedLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)
						allsprites.append(new_formation_enemy)

				if randint(0,1000) == 0:
					new_formation = SingleHawk()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						allsprites.append(new_formation_enemy)

				if randint(0,7800) == 0:
					new_formation = BatteringRam()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						allsprites.append(new_formation_enemy)

				if randint(0,1000) == 0:
					new_formation = SupremeLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == SwallowMKII:
							swallows.append(new_formation_enemy)
						elif new_formation_enemy.__class__ == Crow:
							crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

			elif score > LEVEL7:

				if randint(0,4500) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						allsprites.append(new_formation_enemy)

				if randint(0,580) == 0:
					new_formation = DoubleCrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						crows.append(new_formation_enemy)
						allsprites.append(new_formation_enemy)

				if randint(0,1000) == 0:
					new_formation = AdvancedWing()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == SwallowMKII:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,600) == 0:
					new_formation = SingleCardinal()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,600) == 0:
					new_formation = AdvancedLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)


						allsprites.append(new_formation_enemy)

				if randint(0,1500) == 0:
					new_formation = SingleHawk()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,8000) == 0:
					new_formation = BatteringRam()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

			elif score > LEVEL6:

				if randint(0,1800) == 0:
					new_formation = AdvancedWing()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == SwallowMKII:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,3600) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,3600) == 0:
					new_formation = BasicLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,600) == 0:
					new_formation = DoubleCrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,2500) == 0:
					new_formation = BlueSquad()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Crow:
							crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,600) == 0:
					new_formation = SingleCardinal()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,700) == 0:
					new_formation = AdvancedLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,1500) == 0:
					new_formation = SingleHawk()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

			elif score > LEVEL5:

				if randint(0,6000) == 0:
					new_formation = AdvancedWing()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == SwallowMKII:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,1200) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,2500) == 0:
					new_formation = BasicLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,800) == 0:
					new_formation = DoubleCrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,1300) == 0:
					new_formation = BlueSquad()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Crow:
							crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,800) == 0:
					new_formation = SingleCardinal()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,700) == 0:
					new_formation = AdvancedLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,1800) == 0:
					new_formation = SingleHawk()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

			elif score > LEVEL4:

				if randint(0,1000) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,500) == 0:
					new_formation = BasicLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,1000) == 0:
					new_formation = DoubleCrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,1800) == 0:
					new_formation = BlueSquad()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Crow:
							crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,1200) == 0:
					new_formation = SingleCardinal()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,1500) == 0:
					new_formation = AdvancedLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

			elif score > LEVEL3 and shop_appeared == True:

				if randint(0,1000) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,300) == 0:
					new_formation = BasicLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,550) == 0:
					new_formation = DoubleCrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,800) == 0:
					new_formation = BlueSquad()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Crow:
							crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

			elif score > LEVEL3 and shop_appeared == False:
				#new_shop = Shop(0, -200)
				#allsprites.append(new_shop)
				shop_appeared = "neither"

			elif score > LEVEL2:
				if randint(0,1000) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,400) == 0:
					new_formation = BasicLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)

				if randint(0,600) == 0:
					new_formation = DoubleCrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						crows.append(new_formation_enemy)

						allsprites.append(new_formation_enemy)


			elif score > LEVEL1:
				if randint(0,1000) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

				if randint(0,400) == 0:
					new_formation = BasicLine()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])

						allsprites.append(new_formation_enemy)

						if new_formation_enemy.__class__ == Swallow:
							swallows.append(new_formation_enemy)

			else:
				if randint(0,200) == 0:
					new_formation = SingleSparrow()
					for i in range(len(new_formation.types)):
						new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i])
						allsprites.append(new_formation_enemy)

			'''End of code that spawns in enemies'''


			for i in range(0,len(stars)):#This for loop is for the background stars
				stars[i][1] += 1
				if stars[i][1] > screen_size[1]:
					stars[i][1] = 0


			if time() - powerup_time_elapser >= 60:#Spawns in a random power-up every minute
				new_powerup = POWERUP_TYPES[randint(0,len(POWERUP_TYPES)-1)](randint(0,screen_size[0]), randint(0,screen_size[1]), randint(-2,2), randint(-2,2))
				allsprites.append(new_powerup)
				powerup_time_elapser = time()


			if time() - upgrade_time_elapser >= 120:
				new_upgrade = UPGRADE_TYPES[randint(0,len(UPGRADE_TYPES)-1)](randint(0,screen_size[0]),randint(0,screen_size[1]),randint(-2,2),randint(-2,2))
				allsprites.append(new_upgrade)
				upgrade_time_elapser = time()


			for laser in allsprites:#This loop detects collisions between lasers and things
				if laser.generictype == "MyWeapon":
					for other_object in allsprites:
						if other_object.generictype == "PowerUp":
							if pygame.Rect.colliderect(laser.hitbox, other_object.hitbox) == 1:

								for i in range(0,100):
									if randint(0,600) < 30:
										new_GoldCoin = GoldCoin(other_object.x, other_object.y, random()*randint(-2,2), random()*randint(1,2))
										allsprites.append(new_GoldCoin)

								explosion1.play()
								allsprites.remove(other_object)
								try:
									allsprites.remove(laser)
								except:
									pass
								else:
									pass

						elif other_object.generictype == "Enemy":
							if pygame.Rect.colliderect(laser.hitbox, other_object.hitbox) == 1:
								try:
									allsprites.remove(laser)
								except:
									pass
								else:
									pass
								other_object.hp -= laser.damage
								damage0.play()
								if other_object.hp < 0:
									explosion1.play()

									for i in range(int(other_object.points/(1/other_object.drops)+other_object.formation)):
										if randint(0,other_object.points) > 1000:
											new_PlatinumCoin = PlatinumCoin(other_object.x, other_object.y, random()*randint(-2,2), random()*randint(1,2))
											allsprites.append(new_PlatinumCoin)

										elif randint(0,other_object.points) > 75:
											new_GoldCoin = GoldCoin(other_object.x, other_object.y, random()*randint(-2,2), random()*randint(1,2))
											allsprites.append(new_GoldCoin)

										elif randint(0,other_object.points) > 25:
											new_SilverCoin = SilverCoin(other_object.x, other_object.y, random()*randint(-2,2), random()*randint(1,2))
											allsprites.append(new_SilverCoin)

										elif randint(0,other_object.points) > 0:
											new_CopperCoin = CopperCoin(other_object.x, other_object.y, random()*randint(-2,2), random()*randint(1,2))
											allsprites.append(new_CopperCoin)

									try:
										swallows.remove(other_object)
									except:
										pass
									else:
										pass

									try:
										crows.remove(other_object)
									except:
										pass
									else:
										pass

									allsprites.remove(other_object)
									del(other_object)


			for swallow in swallows:#This loop allows swallows to follow your x position
				if swallow.y < my_ship.y - 16:
					if my_ship.x > swallow.x:
						swallow.moveright()
					if my_ship.x < swallow.x:
						swallow.moveleft()
					if my_ship.x == swallow.x:
						swallow.repos()

			for new_crow in crows:#This loop allows crows to fire
				if new_crow.y < my_ship.y:
					if time() - new_crow.time_elapser >= 0.5 and round(new_crow.y) % 3 == 0:
						new_enemyweapon = StreamG(new_crow.x, new_crow.y)
						laser0.play()
						allsprites.append(new_enemyweapon)
						new_crow.time_elapser = time()

			for coin in allsprites:#This loops detects collisions between coins and the player
				if coin.generictype == "Coin":
					if pygame.Rect.colliderect(coin.hitbox, my_ship.hitbox) == 1:
						points0.play()
						score += coin.value
						if hs_table < score:
							hs_table = score
							highscoretext = font.render("High Score: "+str(hs_table), 0,(255,0,0))
						scoretext=font.render("Score: "+str(score), 1,(160,160,160))
						allsprites.remove(coin)


			#Drawing Below

			#Fills the screen with black
			screen.fill((0, 0, 0))

			#Draws the stars
			for i in range(0,len(stars)):
				#pygame.draw.line(screen, (255,255,255), (stars[i][0], stars[i][1]), (stars[i][0], stars[i][1]))
				pygame.draw.circle(screen,(255,255,255),stars[i],0)

			for sprite in allsprites:#Draws and updates all game sprites
				sprite.update()
				sprite.hb_follow()

				if SHOW_HITBOXES == True:
					pygame.draw.line(screen, (255,0,0), (sprite.hitbox.x, sprite.hitbox.y), (sprite.hitbox.x+sprite.hitbox.width, sprite.hitbox.y))
					pygame.draw.line(screen, (255,0,0), (sprite.hitbox.x+sprite.hitbox.width, sprite.hitbox.y), (sprite.hitbox.x+sprite.hitbox.width, sprite.hitbox.y+sprite.hitbox.height))
					pygame.draw.line(screen, (255,0,0), (sprite.hitbox.x+sprite.hitbox.width, sprite.hitbox.y+sprite.hitbox.height), (sprite.hitbox.x, sprite.hitbox.y+sprite.hitbox.height))
					pygame.draw.line(screen, (255,0,0), (sprite.hitbox.x, sprite.hitbox.y+sprite.hitbox.height), (sprite.hitbox.x, sprite.hitbox.y))


				if sprite.generictype == "Coin":#coins
					if sprite.y < -20 or sprite.y > 720 or sprite.x < -20 or sprite.x > 1020:#This conditional removes off-screen coins
						allsprites.remove(sprite)
						del(sprite)

				elif sprite.generictype == "MyWeapon":#weapons
					if sprite.y < -20 or sprite.y > 1000:#This conditional checks if a laser is off of the screen and deletes it
						allsprites.remove(sprite)
						del(sprite)

				elif sprite.generictype == "EnemyWeapon":#Draws enemy weapons
					if pygame.Rect.colliderect(sprite.hitbox, my_ship.hitbox) == 1:
						allsprites.remove(sprite)
						my_ship.hp -= sprite.damage
						damage0.play()
						if my_ship.hp < 0:
							my_ship.die()
							highscore(hs_table, score)
					if sprite.y > 700:
						allsprites.remove(sprite)

				elif sprite.generictype == "PowerUp":
					if sprite.y < -20 or sprite.y > 720 or sprite.x < -20 or sprite.x > 1020:
						allsprites.remove(sprite)
						del(sprite)

					if pygame.Rect.colliderect(sprite.hitbox, my_ship.hitbox) == 1:
						power0.play()
						my_ship.xpowerup = sprite.name
						my_ship.fire_delay = sprite.pow_speed
						my_ship.coolantbonus = sprite.coolant
						my_ship.powerleft = sprite.duration
						my_ship.powermax = sprite.duration
						allsprites.remove(sprite)

				elif sprite.generictype == "Upgrade":
					if sprite.y < -20 or sprite.y > 720 or sprite.x < -20 or sprite.x > 1020:
						allsprites.remove(sprite)
						del(sprite)

					if pygame.Rect.colliderect(sprite.hitbox, my_ship.hitbox) == 1:
						power0.play()
						my_ship.upgrades.append(sprite.name)
						allsprites.remove(sprite)

				elif sprite.generictype == "Enemy":
					if pygame.Rect.colliderect(sprite.hitbox, my_ship.hitbox) == 1:
						my_ship.hp -= sprite.hp*5
						sprite.hp -= my_ship.hp*5
						if sprite.hp < 0:
							explosion1.play()
							allsprites.remove(sprite)
						else:
							damage0.play()

						try:
							crows.remove(sprite)
						except:
							pass
						else:
							pass

						try:
							swallows.remove(sprite)
						except:
							pass
						else:
							pass

						del(sprite)

						if my_ship.hp < 0:
							#Game over
							my_ship.hp = -1.3
							my_ship.die()
							highscore(hs_table, score)

				elif sprite.generictype == "Shop":
					if pygame.Rect.colliderect(sprite.hitbox, my_ship.hitbox) == 1:
						shopping = True

						#shop_appeared = True


			#Draws the HUD image
			screen.blit(hud_image,(0,screen_size[1]-100))

			#Draws the overheat monitor
			pygame.draw.rect(screen,(colour_control(my_ship.overheat*HEATMULTIPLIER),colour_control(colour_control3(my_ship.overheat*HEATMULTIPLIER)),colour_control(colour_control2(my_ship.overheat*HEATMULTIPLIER))),
				(heatbar_metre_control(HEATBARSTART+my_ship.overheat),638,1,7))

			#Draws the power remaining monitor
			pygame.draw.rect(screen,(255-colour_control(my_ship.powerleft/my_ship.powermax*255),colour_control(my_ship.powerleft/my_ship.powermax*255),0),
				(powerbar_metre_control(POWERBARSTART-my_ship.powerleft),638,1,7))

			#Draws the health remaining monitor
			pygame.draw.rect(screen,(255-colour_control(my_ship.hp/100*255),colour_control(my_ship.hp/100*255),0),
				(healthbar_metre_control(HEALTHBARSTART-my_ship.hp),638,1,7))

			#Draws the score
			screen.blit(scoretext, (300, 638))

			#Draws the high score
			screen.blit(highscoretext, (550,638))

			#Draws game over if game is over
			if my_ship.hp == -1.3:
				screen.blit(gameovertext, (screen_size[0]/2-300, screen_size[1]/2))

			pygame.display.flip()
			clock.tick(40)

		while not done and not menuscreen and paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				if event.type == pygame.KEYDOWN:
					if event.key == K_p:
						paused = togglepause(paused)

			#screen.fill((0,0,0))
			screen.blit(pausedtext, (screen_size[0]/2-200, screen_size[1]/2-70))
			pygame.display.flip()
			clock.tick(40)

		while shopping and not done and not paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					pass
					for shopitem in shopitems:
						pass

			screen.fill((100,100,100))
	
	if done:
		print("Quitting...")
		pygame.quit()

main()
