import math
import pyaudio


class SoundPlayer:
    """Luokka joka toistaa yksitaajuista ääntä, ei toimi tällä hetkellä oikein
    Attributes:
        enable: boolean, joka kertoo toistetaanko ääntä vai ei
        pyaudio: PyAudio olio
        stream: pyaudio stream olio
        empty_wave: tyhjä ääni, jota toistetaan kun enable on epätosi
        wave: toistettava ääni
    """

    def __init__(self):
        self.enable = False
        self.pyaudio = pyaudio.PyAudio()
        self.stream = None

        #Todo: Fix
        freq = 440
        SAMPLES = 1024
        RATE = 60 * 1024
        self.empty_wave = bytes([0 for i in range(SAMPLES)])
        self.wave = bytes([int(128+127/2*math.sin(20*i*math.pi/1024))
                          for i in range(SAMPLES)])
        self.debug_save()

        self.stream = self.pyaudio.open(format=pyaudio.paUInt8, channels=1, rate=RATE,
                                        output=True, frames_per_buffer=SAMPLES, stream_callback=self.pyaudio_cb)

    def debug_save(self):
        if self.wave[0] < self.wave[-1]:
            print("wave is still incorrect", self.wave[0], self.wave[1])
        with open("tune", "wb") as f:
            f.write(self.wave)

    def play_beep(self):
        self.enable = True

    def stop_beep(self):
        self.enable = False

    def pyaudio_cb(self, input_data, frame, time_info, status):
        if self.enable:
            return (self.wave, pyaudio.paContinue)
        return (self.empty_wave, pyaudio.paContinue)
