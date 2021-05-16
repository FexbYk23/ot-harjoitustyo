import unittest
from chip8 import Chip8
from instruction import Instruction
import instruction


def c8_exe(opcode, chip8: Chip8):
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
        c8_exe(0x6001, c8)  # v0 = 1
        c8_exe(0x7010, c8)  # v0 += 0x10
        self.assertEqual(c8.v[0], 0x11)
        c8_exe(0x70f0, c8)  # v0 += 0xf0
        self.assertEqual(c8.v[0], 1)  # overflow

    def test_exec_sub(self):
        c8 = self.chip
        c8_exe(0x6001, c8)  # v0 = 1
        c8_exe(0x6102, c8)  # v1 = 2
        c8_exe(0x8015, c8)  # v0 -= v1
        self.assertEqual(c8.v[0xF], 0)  # carry
        self.assertEqual(c8.v[0], 0xFF)  # overflow

    def test_exec_call(self):
        c8 = self.chip
        sp = c8.sp
        pc = c8.pc
        c8_exe(0x2300, c8)  # call subroutine at 0x300
        self.assertEqual(c8.pc, 0x300)
        self.assertEqual(c8.sp, sp + 2)
        self.assertEqual(c8.read_word(sp), pc)

        c8_exe(0xEE, c8)  # ret
        self.assertEqual(c8.pc, pc)
        self.assertEqual(c8.sp, sp)

    def test_exec_shr(self):
        c8 = self.chip
        c8_exe(0x6102, c8)  # v1 = 2
        c8_exe(0x81F6, c8)  # shr v1
        self.assertEqual(c8.v[1], 1)
        self.assertEqual(c8.v[15], 0)
        c8_exe(0x81F6, c8)  # shr v1
        self.assertEqual(c8.v[1], 0)
        self.assertEqual(c8.v[15], 1)

    def test_exec_shl(self):
        c8 = self.chip
        c8_exe(0x6201, c8)  # v2 = 1
        for i in range(7):
            c8_exe(0x82EE, c8)  # v2 <<= 1
            self.assertEqual(c8.v[2], 1 << (i+1))
            self.assertEqual(c8.v[15], 0)
        c8_exe(0x82EE, c8)  # v2 <<= 1
        self.assertEqual(c8.v[2], 0)
        self.assertEqual(c8.v[15], 1)

    def test_exec_bitwise(self):
        c8 = self.chip
        c8.v[0] = 5
        c8.v[1] = 3
        c8_exe(0x8011, c8) #v0 |= v1
        self.assertEqual(c8.v[0], 7)

        c8_exe(0x8012, c8) #v0 &= v1
        self.assertEqual(c8.v[0], 3)

        c8_exe(0x8003, c8) #v0 ^= v0
        self.assertEqual(c8.v[0], 0)
        self.assertEqual(c8.v[1], 3)

    def test_exec_fx33(self):
        c8 = self.chip
        c8_exe(0x60FE, c8)  # v0 = ff
        c8_exe(0xA800, c8)  # I = 0x800
        c8_exe(0xF033, c8)  # BCD
        self.assertEqual(c8.memory[0x800], 2)
        self.assertEqual(c8.memory[0x801], 5)
        self.assertEqual(c8.memory[0x802], 4)
        self.assertEqual(c8.i, 0x800)
        self.assertEqual(c8.v[0], 0xFE)
        
        c8.i = 0xFFF
        c8_exe(0xF033, c8) #BCD
        self.assertTrue(c8.halted)
        

    def test_exec_fx55(self):
        c8 = self.chip
        for i in range(14):
            c8_exe(0x6000 | (i << 8) | i+1, c8)  # v[i] = i+1

        c8_exe(0xA800, c8)  # I = 0x800
        c8_exe(0xF055, c8)  # mem[I] = v0
        self.assertEqual(c8.memory[c8.i], c8.v[0])
        self.assertEqual(c8.memory[c8.i+1], 0)

        c8_exe(0xF755, c8)
        self.assertEqual(c8.i, 0x800)
        for i in range(8):
            self.assertEqual(c8.memory[c8.i+i], c8.v[i])

    def test_exec_subn(self):
        c8 = self.chip
        c8.v[0] = 10
        c8.v[1] = 81
        c8_exe(0x8017, c8)  # v0 = v1 - v0
        self.assertEqual(c8.v[0], 81 - 10)

    def test_exec_add8(self):
        c8 = self.chip
        c8.v[0] = 10
        c8.v[1] = 130
        c8_exe(0x8014, c8) #v0 += v1
        self.assertEqual(c8.v[0], 130 + 10)
        self.assertEqual(c8.v[15], 0)
        c8_exe(0x8014, c8) #v0 += v1
        self.assertEqual(c8.v[15], 1)

