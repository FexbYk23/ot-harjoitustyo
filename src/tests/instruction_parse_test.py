from chip8 import Chip8
from instruction import Instruction
import instruction
import instructions
import unittest


class TestInstruction(unittest.TestCase):
    def test_parse_sys(self):
        self.assertEqual(Instruction(0).op, instructions.instr_sys)
        self.assertEqual(Instruction(0xFFF).op, instructions.instr_sys)

    def test_parse_cls(self):
        self.assertEqual(Instruction(0x00E0).op, instructions.instr_cls)

    def test_parse_jp(self):
        self.assertEqual(Instruction(0x1000).op, instructions.instr_jp)
        self.assertEqual(Instruction(0x1FFF).op, instructions.instr_jp)

    def test_parse_ret(self):
        self.assertEqual(Instruction(0x00EE).op, instructions.instr_ret)

    def test_parse_call(self):
        self.assertEqual(Instruction(0x2000).op, instructions.instr_call)
        self.assertEqual(Instruction(0x2FFF).op, instructions.instr_call)

    def test_parse_se3(self):
        self.assertEqual(Instruction(0x3000).op, instructions.instr_se3)

    def test_parse_sne(self):
        self.assertEqual(Instruction(0x4000).op, instructions.instr_sne)

    def test_parse_se5(self):
        self.assertEqual(Instruction(0x5000).op, instructions.instr_se5)

    def test_parse_ld6(self):
        self.assertEqual(Instruction(0x6000).op, instructions.instr_ld6)

    def test_parse_add(self):
        self.assertEqual(Instruction(0x7000).op, instructions.instr_add)

    def test_parse_ld8(self):
        self.assertEqual(Instruction(0x8000).op, instructions.instr_ld8)

    def test_parse_or(self):
        self.assertEqual(Instruction(0x8001).op, instructions.instr_or)

    def test_parse_and(self):
        self.assertEqual(Instruction(0x8002).op, instructions.instr_and)

    def test_parse_xor(self):
        self.assertEqual(Instruction(0x8003).op, instructions.instr_xor)

    def test_parse_add8(self):
        self.assertEqual(Instruction(0x8004).op, instructions.instr_add8)

    def test_parse_sub(self):
        self.assertEqual(Instruction(0x8005).op, instructions.instr_sub)

    def test_parse_shr(self):
        self.assertEqual(Instruction(0x8006).op, instructions.instr_shr)

    def test_parse_subn(self):
        self.assertEqual(Instruction(0x8007).op, instructions.instr_subn)

    def test_parse_shl(self):
        self.assertEqual(Instruction(0x800E).op, instructions.instr_shl)

    def test_parse_sne9(self):
        self.assertEqual(Instruction(0x9000).op, instructions.instr_sne9)

    def test_parse_ld_i(self):
        self.assertEqual(Instruction(0xA000).op, instructions.instr_ld_i)

    def test_parse_jp_v0(self):
        self.assertEqual(Instruction(0xB000).op, instructions.instr_jp_v0)

    def test_parse_rnd(self):
        self.assertEqual(Instruction(0xC000).op, instructions.instr_rnd)

    def test_parse_drw(self):
        self.assertEqual(Instruction(0xD000).op, instructions.instr_drw)

    def test_parse_skp(self):
        self.assertEqual(Instruction(0xE09E).op, instructions.instr_skp)
        self.assertEqual(Instruction(0xE09F).op, instructions.instr_invalid)

    def test_parse_sknp(self):
        self.assertEqual(Instruction(0xE0A1).op, instructions.instr_sknp)
        self.assertEqual(Instruction(0xE0AF).op, instructions.instr_invalid)

    def test_parse_ld_vx_dt(self):
        self.assertEqual(Instruction(0xF007).op, instructions.instr_ld_vx_dt)

    def test_parse_ld_key(self):
        self.assertEqual(Instruction(0xF00A).op, instructions.instr_ld_key)

    def test_parse_ld_dt(self):
        self.assertEqual(Instruction(0xF015).op, instructions.instr_ld_dt)

    def test_parse_ld_st(self):
        self.assertEqual(Instruction(0xF018).op, instructions.instr_ld_st)

    def test_parse_add_i(self):
        self.assertEqual(Instruction(0xF01E).op, instructions.instr_add_i)

    def test_parse_ld_f(self):
        self.assertEqual(Instruction(0xF029).op, instructions.instr_ld_f)

    def test_parse_ld_b(self):
        self.assertEqual(Instruction(0xF033).op, instructions.instr_ld_b)

    def test_parse_ld_ptr_i(self):
        self.assertEqual(Instruction(0xF055).op, instructions.instr_ld_ptr_i)

    def test_parse_ld_vx_i(self):
        self.assertEqual(Instruction(0xF065).op, instructions.instr_ld_vx_i)
