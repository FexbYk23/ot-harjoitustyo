import math
import pygame

class SoundPlayer:
    """Luokka joka toistaa yksitaajuista ääntä
    Attributes:
        available: boolean joka kertoo onko äänentoisto käytettävissä
    """

    def __init__(self):
        """Alustaa pygamen mixerin ja aloittaa äänentoiston"""
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("src/resources/sound.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.pause()
            self.available = True
        except:
            self.available = False

    def play_beep(self):
        """Jatkaa äänentoistoa"""
        if self.available:
            pygame.mixer.music.unpause()
    
    def stop_beep(self):
        """Pysäyttää äänentoiston"""
        if self.available:
            pygame.mixer.music.pause()
