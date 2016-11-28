#Script for level-related dynamics, such as enemy spawning or shop items

LEVEL1 = 6
LEVEL2 = 100
LEVEL3 = 500
LEVEL4 = 1000
LEVEL5 = 3500
LEVEL6 = 4500
LEVEL7 = 5500
LEVEL8 = 6500
LEVEL9 = 7500
LEVEL10 = 9000
LEVEL11 = 10000

def scoretolevel(score):
	if score >= 10000:
		return 11
	elif score >= 9000:
		return 10
	elif score >= 7500:
		return 9
	elif score >= 6500:
		return 8
	elif score >= 5500:
		return 7
	elif score >= 4500:
		return 6
	elif score >= 3500:
		return 5
	elif score >= 1000:
		return 4
	elif score >= 500:
		return 3
	elif score >= 100:
		return 2
	elif score >= 6:
		return 1
	else:
		return 0