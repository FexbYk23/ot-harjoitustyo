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
            0x60, 0x01,  # v0 = 1
            0xFF, 0xFF  # undefined
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
            0xF1, 0x0A,  # v1 = keypress
        ]
        c8.load_program(program, 512)
        c8.exec_next()
        c8.exec_next()
        self.assertEqual(c8.pc, 514)
        c8.keys[10] = True
        c8.exec_next()
        self.assertEqual(c8.pc, 516)
        self.assertEqual(c8.v[1], 10)

    def test_framebuffer(self):
        c8 = chip8.Chip8()
        program = [
        0xF0, 0x29,  # I = font[0]
        0xD0, 0x08, #DRW 0 0 8
        0xD0, 0x08, #DRW 0 0 8
        0xD0, 0x08, #DRW 0 0 8
        0x00, 0xE0 #CLS
        ]
        c8.load_program(program, 512)
        self.assertFalse(c8.framebuf[0])
        c8.exec_next()
        c8.exec_next()
        self.assertTrue(c8.framebuf[0])
        self.assertEqual(c8.v[15], 0)
        c8.exec_next()
        self.assertEqual(c8.v[15], 1)
        self.assertFalse(c8.framebuf[1])
        c8.exec_next()
        c8.exec_next()
        self.assertFalse(c8.framebuf[0])

    def test_exec_outside_memory(self):
        c8 = chip8.Chip8()
        program = [
        0x1F, 0xFE  # goto 0xFFE
        ]
        c8.load_program(program, 512)
        c8.write_word(0xFFE, 0x00E0) #valid instruction
        c8.exec_next()
        self.assertEqual(c8.pc, 0xFFE)
        c8.exec_next()
        self.assertEqual(c8.pc, 0x1000)
        c8.exec_next()
        self.assertTrue(c8.halted)


    def test_timers(self):
        c8 = chip8.Chip8()
        prog = [
            0x60, 0x2,   #v0 = 2
            0xF0, 0x18,  #st = v0
            0xf0, 0x15  #dt = v0
        ]
        c8.load_program(prog, 512)
        for i in range(len(prog)//2):
            c8.exec_next()
        self.assertEqual(c8.dt, 2)
        self.assertEqual(c8.st, 2)

        c8.update_timers()
        self.assertEqual(c8.dt, 1)
        self.assertEqual(c8.st, 1)

        c8.update_timers()
        c8.update_timers()
        self.assertEqual(c8.dt, 0)
        self.assertEqual(c8.st, 0)
    
    def test_reset(self):
        c8 = chip8.Chip8()
        c8.v[2] = 9
        c8.dt = 9
        c8.st = 9
        c8.memory[600] = 1
        c8.reset(600)
        self.assertEqual(c8.pc, 600)
        self.assertEqual(c8.v[2], 0)
        self.assertEqual(c8.dt, 0)
        self.assertEqual(c8.st, 0)
        self.assertEqual(c8.memory[600], 1)

    def test_oob_rw(self):
        c8 = chip8.Chip8()
        prog = [
            0xAF, 0xFF, #I = 0xFFF
            0xFF, 0x65  #Store registers at I
        ]
        c8.load_program(prog, 400)
        c8.exec_next()
        c8.exec_next()
        self.assertTrue(c8.halted)
        
        c8.reset(400)
        self.assertFalse(c8.halted)
        c8.write_word(402, 0xFF55) #Store registers at I
        c8.exec_next()
        c8.exec_next()
        self.assertTrue(c8.halted)
