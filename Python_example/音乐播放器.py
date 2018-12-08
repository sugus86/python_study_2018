import time
import pygame
from os import path 
file=path.dirname(__file__) +'\\pianai.mp3'
print(file)
'''
with open(file,'rb') as f:
    for line in f.readlines():
        print(line)
'''
pygame.mixer.init()
print("播放音乐:偏爱.mp3")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()
