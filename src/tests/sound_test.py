import unittest
import sound


class SoundTester(unittest.TestCase):
    def test_init(self):
        s = sound.SoundPlayer()
        self.assertFalse(s.enable)

    def test_waveform(self):
        s = sound.SoundPlayer()
        self.assertGreaterEqual(s.wave[0], s.wave[-1])
