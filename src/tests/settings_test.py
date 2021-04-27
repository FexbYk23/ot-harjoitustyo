import tempfile, os
import unittest
import settings

class SettingsTester(unittest.TestCase):

    def test_initial(self):
        s = settings.Settings()
        self.assertEqual(s.get_entrypoint(), 0x200)
        self.assertEqual(s.get_frequency(), 10)

    def test_save_load(self):
        d = tempfile.TemporaryDirectory()
        filename = os.path.join(d.name, "settings.cfg")

        s = settings.Settings()
        s.freq = 100
        s.save(filename)
        s.freq = 10
        s.load(filename)
        self.assertEqual(s.get_frequency(), 100)

    def test_load_constructor(self):
        d = tempfile.TemporaryDirectory()
        filename = os.path.join(d.name, "settings.cfg")
        
        a = settings.Settings()
        a.freq = 200
        a.save(filename)

        s = settings.Settings(filename)
        self.assertEqual(s.get_frequency(), 200)

