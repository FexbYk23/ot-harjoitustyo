import unittest
from chip8 import Chip8
from instruction import Instruction
import instruction


def c8_exe(opcode, chip8 : Chip8):
    Instruction(opcode).execute(chip8)

class TestInstructionExec(unittest.TestCase):

    def setUp(self):
        self.chip = Chip8()

    def test_exec_ld(self):
        chip = self.chip
        Instruction(0x60ff).execute(self.chip)
        self.assertEqual(chip.v[0], 0xff)
        Instruction(0x6423).execute(self.chip)
        self.assertEqual(chip.v[4], 0x23)

    def test_exec_add(self):
        c8 = self.chip
        c8_exe(0x6001, c8)  #v0 = 1
        c8_exe(0x7010, c8)  #v0 += 0x10
        self.assertEqual(c8.v[0], 0x11)
        c8_exe(0x70f0, c8) #v0 += 0xf0
        self.assertEqual(c8.v[0], 1) #overflow

    def test_exec_sub(self):
        c8 = self.chip
        c8_exe(0x6001, c8) #v0 = 1
        c8_exe(0x6102, c8) #v1 = 2
        c8_exe(0x8015, c8) #v0 -= v1
        self.assertEqual(c8.v[0xF], 0) #carry
        self.assertEqual(c8.v[0], 0xFF) #overflow

