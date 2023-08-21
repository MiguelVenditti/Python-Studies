import pygame
pygame.init()
pygame.mixer.music.load('gregoriano.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()