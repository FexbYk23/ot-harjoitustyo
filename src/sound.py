import math
import pygame

class SoundPlayer:
    """Luokka joka toistaa yksitaajuista ääntä
    """

    def __init__(self):
        """Alustaa pygamen mixerin ja aloittaa äänentoiston"""
        pygame.mixer.init()
        pygame.mixer.music.load("src/resources/sound.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.pause()

    def play_beep(self):
        """Jatkaa äänentoistoa"""
        pygame.mixer.music.unpause()
    
    def stop_beep(self):
        """Pysäyttää äänentoiston"""
        pygame.mixer.music.pause()
