import unittest
import settings

class SettingsTester(unittest.TestCase):

    def test_initial(self):
        s = settings.Settings()
        self.assertEqual(s.get_entrypoint(), 0x200)
        self.assertEqual(s.get_frequency(), 10)
