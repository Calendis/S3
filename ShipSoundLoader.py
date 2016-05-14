#Script that loads sounds for the player's ship
import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

explosion0 = pygame.mixer.Sound("aud/explosion0.wav")
laser1 = pygame.mixer.Sound("aud/laser1.wav")