# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import emoji
import time

a = float(input('Quanto é 1+1? '))
if a == 2:
    acerto = True
else:
    acerto = False

if acerto == True:
    print(emoji.emojize('\033[1;34mACERTOU PARABÉNS\033[m :face_screaming_in_fear::clapping_hands:'))
    if acerto == True:
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('musica.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        input()
        pygame.mixer.stop()
else:
    print('\033[1;31mERROU PARABÉNS!\033[m')


