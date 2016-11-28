#Script that loads sounds for void.py
import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

explosion1 = pygame.mixer.Sound("aud/explosion1.wav")
power0 = pygame.mixer.Sound("aud/power0.wav")
points0 = pygame.mixer.Sound("aud/points0.wav")
damage0 = pygame.mixer.Sound("aud/damage0.wav")
laser0 = pygame.mixer.Sound("aud/laser0.wav")
menu0 = pygame.mixer.Sound("aud/menu0.wav")

music = pygame.mixer.music.load("aud/music.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)