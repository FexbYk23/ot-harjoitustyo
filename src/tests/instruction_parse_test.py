from chip8 import Chip8
from instruction import Instruction
import instruction
import unittest

class TestInstruction(unittest.TestCase):
    def test_parse_sys(self):
        self.assertEqual(Instruction(0).op, instruction.instr_sys)
        self.assertEqual(Instruction(0xFFF).op, instruction.instr_sys)
    
    def test_parse_cls(self):
        self.assertEqual(Instruction(0x00E0).op, instruction.instr_cls)

    def test_parse_jp(self):
        self.assertEqual(Instruction(0x1000).op, instruction.instr_jp)
        self.assertEqual(Instruction(0x1FFF).op, instruction.instr_jp)

    def test_parse_ret(self):
        self.assertEqual(Instruction(0x00EE).op, instruction.instr_ret)

    def test_parse_call(self):
        self.assertEqual(Instruction(0x2000).op, instruction.instr_call)
        self.assertEqual(Instruction(0x2FFF).op, instruction.instr_call)
	
    def test_parse_se3(self):
        self.assertEqual(Instruction(0x3000).op, instruction.instr_se3)

    def test_parse_sne(self):
        self.assertEqual(Instruction(0x4000).op, instruction.instr_sne)
    
    def test_parse_se5(self):
        self.assertEqual(Instruction(0x5000).op, instruction.instr_se5)
        
    def test_parse_ld6(self):
        self.assertEqual(Instruction(0x6000).op, instruction.instr_ld6)
    
    def test_parse_add(self):
        self.assertEqual(Instruction(0x7000).op, instruction.instr_add)
    
    def test_parse_ld8(self):
        self.assertEqual(Instruction(0x8000).op, instruction.instr_ld8)
        
        
    def test_parse_or(self):
        self.assertEqual(Instruction(0x8001).op, instruction.instr_or)
        
    def test_parse_and(self):
        self.assertEqual(Instruction(0x8002).op, instruction.instr_and)
    
    def test_parse_xor(self):
        self.assertEqual(Instruction(0x8003).op, instruction.instr_xor)
        
    def test_parse_add8(self):
        self.assertEqual(Instruction(0x8004).op, instruction.instr_add8)
    
    def test_parse_sub(self):
        self.assertEqual(Instruction(0x8005).op, instruction.instr_sub)

    def test_parse_shr(self):
        self.assertEqual(Instruction(0x8006).op, instruction.instr_shr)

    def test_parse_subn(self):
        self.assertEqual(Instruction(0x8007).op, instruction.instr_subn)
        
    def test_parse_shl(self):
        self.assertEqual(Instruction(0x800E).op, instruction.instr_shl)
        
    def test_parse_sne9(self):
        self.assertEqual(Instruction(0x9000).op, instruction.instr_sne9)
    
    def test_parse_ld_i(self):
        self.assertEqual(Instruction(0xA000).op, instruction.instr_ld_i)
    
    def test_parse_jp_v0(self):
        self.assertEqual(Instruction(0xB000).op, instruction.instr_jp_v0)
    
    def test_parse_rnd(self):
        self.assertEqual(Instruction(0xC000).op, instruction.instr_rnd)
    
    def test_parse_drw(self):
        self.assertEqual(Instruction(0xD000).op, instruction.instr_drw)
        
    def test_parse_skp(self):
        self.assertEqual(Instruction(0xE09E).op, instruction.instr_skp)
        self.assertEqual(Instruction(0xE09F).op, instruction.instr_invalid)
        
    def test_parse_sknp(self):
        self.assertEqual(Instruction(0xE0A1).op, instruction.instr_sknp)
        self.assertEqual(Instruction(0xE0AF).op, instruction.instr_invalid)
        

    def test_parse_ld_dt(self):
        self.assertEqual(Instruction(0xF007).op, instruction.instr_ld_dt)
    
    def test_parse_ld_key(self):
        self.assertEqual(Instruction(0xF015).op, instruction.instr_ld_key)

    def test_parse_ld_st(self):
        self.assertEqual(Instruction(0xF018).op, instruction.instr_ld_st)

    def test_parse_add_i(self):
        self.assertEqual(Instruction(0xF01E).op, instruction.instr_add_i)

    def test_parse_ld_f(self):
        self.assertEqual(Instruction(0xF029).op, instruction.instr_ld_f)

    def test_parse_ld_b(self):
        self.assertEqual(Instruction(0xF033).op, instruction.instr_ld_b)

    def test_parse_ld_ptr_i(self):
        self.assertEqual(Instruction(0xF055).op, instruction.instr_ld_ptr_i)

    def test_parse_ld_vx_i(self):
        self.assertEqual(Instruction(0xF065).op, instruction.instr_ld_vx_i)
