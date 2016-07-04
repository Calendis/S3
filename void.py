#Some basic pygame stuff
import shelve
import pygame
from pygame.locals import *
from random import randint
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

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Void S3")

clock = pygame.time.Clock()

def togglepause():
	global paused
	if paused == True:
		paused = False
	elif paused == False:
		paused = True

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
	my_ship = Ship(screen_size[0]/2, screen_size[1]*0.6, None, None, 3.0, 0, "shipimgs",
		False, "none", "ypow", "l", "r", "d", "u", "hp", "can_shoot", "elapser", "fire_delay", "overheat",
		"coolantbonus", "powerleft", "powermax", "upgrades", Stream, "backfire")

def main():
	done = False
	menuscreen = True

	global paused
	paused = False

	level0boss = False

	stars = []
	powerups = []
	upgrades = []
	enemies = []
	swallows = []
	crows = []
	coins = []
	enemyweapons = []
	buttons = []

	play_button = PlayButton(100, 200, "images", "img_count", "hovered")
	buttons.append(play_button)

	score = 0
	try:
		hs_table = shelve.open("highscores.sav")
		hs_table = hs_table["highscore"]
		#print("The high score is "+str(hs_table))
	except:
		#print("No highscores.")
		hs_table = 0

	scoretext=font.render("Score: "+str(score), 0,(160,160,160))
	highscoretext = font.render("High Score: "+str(hs_table), 0,(255,0,0))

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

	while menuscreen and not done:
		for event in pygame.event.get():
			#Event Listeners
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
			#print(len(buttons))
			button.update()

		screen.blit(logo_image,(screen_size[0]/2-374/2,10))

		pygame.display.flip()
		clock.tick(40)
		

	while not done and not menuscreen:
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
						if my_ship.y < 562:
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

		if score > LEVEL8:

			if randint(0,9000) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,580) == 0:
				new_formation = DoubleCrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)
					crows.append(new_formation_enemy)

			if randint(0,800) == 0:
				new_formation = AdvancedWing("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == SwallowMKII:
						swallows.append(new_formation_enemy)

			if randint(0,550) == 0:
				new_formation = SingleCardinal("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,1600) == 0:
				new_formation = AdvancedLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,1000) == 0:
				new_formation = SingleHawk("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,7800) == 0:
				new_formation = BatteringRam("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,1000) == 0:
				new_formation = SupremeLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == SwallowMKII:
						swallows.append(new_formation_enemy)
					elif new_formation_enemy.__class__ == Crow:
						crows.append(new_formation_enemy)

		elif score > LEVEL7:

			if randint(0,4500) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,580) == 0:
				new_formation = DoubleCrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)
					crows.append(new_formation_enemy)

			if randint(0,1000) == 0:
				new_formation = AdvancedWing("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == SwallowMKII:
						swallows.append(new_formation_enemy)

			if randint(0,600) == 0:
				new_formation = SingleCardinal("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,600) == 0:
				new_formation = AdvancedLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,1500) == 0:
				new_formation = SingleHawk("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,8000) == 0:
				new_formation = BatteringRam("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

		elif score > LEVEL6:

			if randint(0,1800) == 0:
				new_formation = AdvancedWing("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == SwallowMKII:
						swallows.append(new_formation_enemy)

			if randint(0,3600) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,3600) == 0:
				new_formation = BasicLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,600) == 0:
				new_formation = DoubleCrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)
					crows.append(new_formation_enemy)

			if randint(0,2500) == 0:
				new_formation = BlueSquad("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Crow:
						crows.append(new_formation_enemy)

			if randint(0,600) == 0:
				new_formation = SingleCardinal("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,700) == 0:
				new_formation = AdvancedLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,1500) == 0:
				new_formation = SingleHawk("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

		elif score > LEVEL5:

			if randint(0,6000) == 0:
				new_formation = AdvancedWing("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == SwallowMKII:
						swallows.append(new_formation_enemy)

			if randint(0,1200) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,2500) == 0:
				new_formation = BasicLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,800) == 0:
				new_formation = DoubleCrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)
					crows.append(new_formation_enemy)

			if randint(0,1300) == 0:
				new_formation = BlueSquad("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Crow:
						crows.append(new_formation_enemy)

			if randint(0,800) == 0:
				new_formation = SingleCardinal("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,700) == 0:
				new_formation = AdvancedLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,1800) == 0:
				new_formation = SingleHawk("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

		elif score > LEVEL4:

			if randint(0,1000) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,500) == 0:
				new_formation = BasicLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,1000) == 0:
				new_formation = DoubleCrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)
					crows.append(new_formation_enemy)

			if randint(0,1800) == 0:
				new_formation = BlueSquad("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Crow:
						crows.append(new_formation_enemy)

			if randint(0,1200) == 0:
				new_formation = SingleCardinal("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,1500) == 0:
				new_formation = AdvancedLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

		elif score > LEVEL3:
			
			if randint(0,1000) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,300) == 0:
				new_formation = BasicLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,550) == 0:
				new_formation = DoubleCrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)
					crows.append(new_formation_enemy)

			if randint(0,800) == 0:
				new_formation = BlueSquad("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Crow:
						crows.append(new_formation_enemy)

		elif score > LEVEL2:
			if randint(0,1000) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,400) == 0:
				new_formation = BasicLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

			if randint(0,600) == 0:
				new_formation = DoubleCrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)
					crows.append(new_formation_enemy)


		elif score > LEVEL1:
			if randint(0,1000) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

			if randint(0,400) == 0:
				new_formation = BasicLine("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

					if new_formation_enemy.__class__ == Swallow:
						swallows.append(new_formation_enemy)

		else:
			if randint(0,200) == 0:
				new_formation = SingleSparrow("types", "xoffset", "yoffset", "pos")
				for i in range(len(new_formation.types)):
					new_formation_enemy = new_formation.types[i](new_formation.pos+new_formation.xoffset[i]*i, -64+new_formation.yoffset[i], "xspeed","yspeed","img","imgno","fire","hp","formation","points","drops")
					enemies.append(new_formation_enemy)

		'''End of code that spawns in enemies'''

		
		for i in range(0,len(stars)):#This for loop is for the background stars
			stars[i][1] += 3
			if stars[i][1] > screen_size[1]:
				stars[i][1] = 0

		powerupgen = randint(0,16383)#Spawns in powerups
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


		upgradegen = randint(0,40000)#Spawns in upgrades
		if upgradegen in range(0,5):
			new_upgrade = Damage0(randint(0,screen_size[0]),randint(0,screen_size[1]),randint(-2,2),randint(-2,2),
			"name","images","imgplc")
			upgrades.append(new_upgrade)
		elif upgradegen in range(6,10):
			new_upgrade = Backfire(randint(0,screen_size[0]),randint(0,screen_size[1]),randint(-2,2),randint(-2,2),
			"name","images","imgplc")
			upgrades.append(new_upgrade)



		for power_up in powerups:#This for loop detects collisions between powerups and things
			if int(my_ship.x*10 - power_up.x*10) in range(-320, 160) and int(my_ship.y*10 - power_up.y*10) in range(-320, 230):
				power0.play()
				my_ship.xpowerup = power_up.name
				my_ship.fire_delay = power_up.pow_speed
				my_ship.coolantbonus = power_up.coolant
				my_ship.powerleft = power_up.duration
				my_ship.powermax = power_up.duration
				powerups.remove(power_up)

		for upgrade in upgrades:#This loop detects collisions between upgrades and things
			if int(my_ship.x*10 - upgrade.x*10) in range(-320, 160) and int(my_ship.y*10 - upgrade.y*10) in range(-320, 230):
				power0.play()
				my_ship.upgrades.append(upgrade.name)
				upgrades.remove(upgrade)

		for laser in weapons:#This loop detects collisions between lasers and powerups
			for power_up in powerups:
				if laser.x - power_up.x in range(-8,16) and laser.y - power_up.y in range(-16,16):
					
					for i in range(0,100):
						if randint(0,600) < 30:
							new_GoldCoin = GoldCoin(power_up.x, power_up.y, random()*randint(-2,2), random()*randint(1,2), "coinimg", "imagecount", "imgs", "value")
							coins.append(new_GoldCoin)

					explosion1.play()
					powerups.remove(power_up)
					weapons.remove(laser)

			for enemy in enemies:#This loop detects collisions between lasers and enemies
				if int(laser.x*10) - int(enemy.x*10) in range(-160,320) and int(laser.y*10) - int(enemy.y*10) in range(-240,320):
					try:
						weapons.remove(laser)
					except:
						pass
					else:
						pass
					enemy.hp -= laser.damage
					damage0.play()
					if enemy.hp < 1:
						explosion1.play()

						for i in range(int(enemy.points/(1/enemy.drops)+enemy.formation)):
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
						
						try:
							swallows.remove(enemy)
						except:
							pass
						else:
							pass

						try:
							crows.remove(enemy)
						except:
							pass
						else:
							pass

						enemies.remove(enemy)
						del(enemy)

		for swallow in swallows:#This loop allows swallows to follow your x position
			if swallow.y < my_ship.y - 16:
				if my_ship.x > swallow.x:
					swallow.moveright()
				if my_ship.x < swallow.x:
					swallow.moveleft()
				if my_ship.x == swallow.x:
					swallow.repos()

		for enemy in enemies:#This loop detects collisions between enemies and the player
			
			#if int(coin.x*10) - int(my_ship.x*10) in range(0, 320) and int(coin.y*10) - int(my_ship.y*10) in range(0,320):
			
			if int(enemy.x*10) - int(my_ship.x*10) in range(-320, 320) and int(enemy.y*10) - int(my_ship.y*10) in range(-320, 320):
				my_ship.hp -= enemy.hp*5
				enemy.hp -= my_ship.hp*5
				if enemy.hp < 0:
					explosion1.play()
					enemies.remove(enemy)
				else:
					damage0.play()
				
				try:
					crows.remove(enemy)
				except:
					pass
				else:
					pass

				try:
					swallows.remove(enemy)
				except:
					pass
				else:
					pass
				
				del(enemy)

				if my_ship.hp < 0:
					#Game over
					my_ship.hp = -1
					my_ship.die()
					highscore(hs_table, score)

		for new_crow in crows:#This loop allows crows to fire
			if new_crow.y < my_ship.y:
				if randint(0, 20) == 0:
					new_enemyweapon = StreamG("speed", "weaponimg", new_crow.x, new_crow.y, "damage")
					laser0.play()
					enemyweapons.append(new_enemyweapon)

		for coin in coins:#This loops detects collisions between coins and the player
			
			#terrible coin magnet
			'''
			if int(coin.x*10) - int(my_ship.x*10) in range(0, 425) and int(coin.y*10) - int(my_ship.y*10) in range(0,380):
				coin.x -= (coin.x - my_ship.x)/20
			if int(coin.x*10) - int(my_ship.x*10) in range(-269, 0) and int(coin.y*10) - int(my_ship.y*10) in range(0,380):
				coin.x -= (coin.x-28 - my_ship.x)/20
				'''

			if int(coin.x*10) - int(my_ship.x*10) in range(0, 320) and int(coin.y*10) - int(my_ship.y*10) in range(0,320):
				#print("coin: " + str(coin.x)+", "+str(coin.y))
				#print("ship: " + str(my_ship.x)+", "+str(my_ship.y))
				points0.play()
				score += coin.value
				if hs_table < score:
					hs_table = score
					highscoretext = font.render("High Score: "+str(hs_table), 0,(255,0,0))
				scoretext=font.render("Score: "+str(score), 1,(160,160,160))
				coins.remove(coin)

		#Drawing Below
		
		#Fills the screen with black
		screen.fill((0, 0, 0))

		#Draws the stars
		for i in range(0,len(stars)):
			pygame.draw.circle(screen,(255,255,255),stars[i],0)

		for coin in coins:#draws coins
			coin.update()
			if coin.y < -20 or coin.y > 720 or coin.x < -20 or coin.x > 1020:#This conditional removes off-screen coins
				coins.remove(coin)
				del(coin)

		my_ship.update()#draws the ship

		for my_weapon in weapons:#Draws weapons
			my_weapon.update()
			if my_weapon.y < -20 or my_weapon.y > 1000:#This conditional checks if a laser is off of the screen and deletes it
				weapons.remove(my_weapon)
				del(my_weapon)

		for new_enemyweapon in enemyweapons:#draws enemy weapons and allows them to hit you
			new_enemyweapon.update()
			if int(new_enemyweapon.x*10) - int(my_ship.x*10) in range(0,240) and int(new_enemyweapon.y*10) - int(my_ship.y*10) in range(0,240):
				my_ship.hp -= new_enemyweapon.damage
				damage0.play()
				enemyweapons.remove(new_enemyweapon)
				if my_ship.hp < 0:
					my_ship.die()
					highscore(hs_table, score)
			if new_enemyweapon.y > 700:
				enemyweapons.remove(new_enemyweapon)
		
		for power_up in powerups:#Draws powerups
			power_up.update()
			if power_up.y < -20 or power_up.y > 720 or power_up.x < -20 or power_up.x > 1020:
				powerups.remove(power_up)
				del(power_up)

		for enemy in enemies:#draws enemies
			enemy.update()

		for upgrade in upgrades:#draws upgrades
			upgrade.update()
			if upgrade.y < -20 or upgrade.y > 720 or upgrade.x < -20 or upgrade.x > 1020:
				upgrades.remove(upgrade)
				del(upgrade)

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

		#Draws the high score
		screen.blit(highscoretext, (550,638))
		
		pygame.display.flip()
		clock.tick(40)


	pygame.quit()

main()