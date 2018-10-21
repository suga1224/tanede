# -*- coding: utf-8 -*-
import pygame.mixer

def sound_play(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    
if __name__ == "__main__":
    path = "sound/move.wav"
    sound_play(path)