#Script that loads sounds for void.py
import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

explosion1 = pygame.mixer.Sound("aud/explosion1.wav")
power0 = pygame.mixer.Sound("aud/power0.wav")
points0 = pygame.mixer.Sound("aud/points0.wav")