import unittest
import chip8

class Chip8Tester(unittest.TestCase):

    def test_load_program(self):
        c8 = chip8.Chip8()
        c8.load_program([245, 1, 2, 3], 600)
        self.assertEqual(c8.memory[600], 245)
        self.assertEqual(c8.memory[601], 1)
        self.assertEqual(c8.pc, 600)

    def test_exec_next(self):
        c8 = chip8.Chip8()
        
        program = [
                0x60, 0x01,  #v0 = 1
                0xFF, 0xFF  #undefined
                ]

        c8.load_program(program, 512)
        c8.exec_next()
        self.assertEqual(c8.v[0], 1)
        self.assertEqual(c8.pc, 514)
        self.assertFalse(c8.halted)
        c8.exec_next()
        self.assertTrue(c8.halted)
        c8.exec_next()
        self.assertEqual(c8.pc, 516)
        c8.exec_next()
        self.assertEqual(c8.pc, 516)

    def test_ld_key_reg(self):
        c8 = chip8.Chip8()
        program = [
                0xF1, 0x0A, #v1 = keypress
                ]
        c8.load_program(program, 512)
        c8.exec_next()
        c8.exec_next()
        self.assertEqual(c8.pc, 514)
        c8.keys[10] = True
        c8.exec_next()
        self.assertEqual(c8.pc, 516)
        self.assertEqual(c8.v[1], 10)
        

