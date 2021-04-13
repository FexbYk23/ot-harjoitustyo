from chip8 import Chip8
import random


class Instruction:
    def __init__(self, opcode):
        
        self.op = instr_invalid

        if opcode == 0xE0:
            self.op = instr_cls
            return
        elif opcode == 0xEE:
            self.op = instr_ret
            return
        

        top4 = opcode >> 12
        if top4 == 0:
            self.op = instr_sys
        elif top4 == 1:
            self.arg1 = opcode & 0xFFF
            self.op = instr_jp
        elif top4 == 2:
            self.arg1 = opcode & 0xFFF
            self.op = instr_call
        elif top4 == 3:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instr_se3
        elif top4 == 4:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instr_sne
        elif top4 == 5:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = (opcode >> 4) & 0xF
            self.op = instr_se5
        elif top4 == 6:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instr_ld6
        elif top4 == 7:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instr_add
        elif top4 == 8:
            bottom4 = opcode & 0xF
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = (opcode >> 4) & 0xF
            if bottom4 == 0:
                self.op = instr_ld8
            elif bottom4 == 1:
                self.op = instr_or
            elif bottom4 == 2:
                self.op = instr_and
            elif bottom4 == 3:
                self.op = instr_xor
            elif bottom4 == 4:
                self.op = instr_add8
            elif bottom4 == 5:
                self.op = instr_sub
            elif bottom4 == 6:
                self.op = instr_shr
            elif bottom4 == 7:
                self.op = instr_subn
            elif bottom4 == 0xE:
                self.op = instr_shl

        elif top4 == 9:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = (opcode >> 4) & 0xF
            self.op = instr_sne9
        elif top4 == 0xA:
            self.arg1 = opcode & 0xFFF
            self.op = instr_ld_i
        elif top4 == 0xB:
            self.arg1 = opcode & 0xFFF
            self.op = instr_jp_v0
        elif top4 == 0xC:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instr_rnd
        elif top4 == 0xD:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = (opcode >> 4) & 0xF
            self.arg3 = (opcode) & 0xF
            self.op = instr_drw
        elif top4 == 0xE:
            self.arg1 = (opcode >> 8) & 0xF
            if opcode & 0xFF == 0x9E:
                self.op = instr_skp
            elif opcode & 0xFF == 0xA1:
                self.op = instr_sknp

        elif top4 == 0xF:
            bot8 = opcode & 0xFF
            self.arg1 = (opcode >> 8) & 0xF
            if bot8 == 7:
                self.op = instr_ld_dt
            elif bot8 == 0x15:
                self.op = instr_ld_key
            elif bot8 == 0x18:
                self.op = instr_ld_st
            elif bot8 == 0x1E:
                self.op = instr_add_i
            elif bot8 == 0x29:
                self.op = instr_ld_f
            elif bot8 == 0x33:
                self.op = instr_ld_b
            elif bot8 == 0x55:
                self.op = instr_ld_ptr_i
            elif bot8 == 0x65:
                self.op = instr_ld_vx_i


    def execute(self, chip8 : Chip8):
        self.op(self, chip8)





def instr_invalid(inst : Instruction, chip8 : Chip8):
    print("invalid instruction at:",chip8.pc)

def instr_sys(inst : Instruction, chip8 : Chip8):
    #not implemented
    pass

def instr_cls(inst : Instruction, chip8 : Chip8):
    for i in range(len(chip8.framebuf)):
        chip8.framebuf[i] = 0

def instr_ret(inst : Instruction, chip8 : Chip8):
    chip8.pc = chip8.read_word(chip8.sp)
    chip8.sp -= 2

def instr_jp(inst : Instruction, chip8 : Chip8):
    chip8.pc = inst.arg1
    
def instr_call(inst : Instruction, chip8 : Chip8):    
    chip8.sp += 2
    chip8.write_word(chip8.sp, chip8.pc)
    chip8.pc = inst.arg1

def instr_se3(inst : Instruction, chip8 : Chip8):
    if chip8.v[inst.arg1] == inst.arg2:
        chip8.pc += 2

def instr_sne(inst : Instruction, chip8 : Chip8): 
    if chip8.v[inst.arg1] != inst.arg2:
        chip8.pc += 2

def instr_se5(inst : Instruction, chip8 : Chip8): 
    if chip8.v[inst.arg1] == chip8.v[inst.arg2]:
        chip8.pc += 2


def instr_ld6(inst : Instruction, chip8 : Chip8):
    chip8.v[inst.arg1] = inst.arg2

def instr_add(inst : Instruction, chip8 : Chip8):
    chip8.v[inst.arg1] += inst.arg2
    chip8.v[inst.arg1] &= 0xFF

def instr_ld8(inst : Instruction, chip8 : Chip8): 
    chip8.v[inst.arg1] = chip8.v[inst.arg2]

def instr_or(inst : Instruction, chip8 : Chip8): 
    chip8.v[inst.arg1] |= chip8.v[inst.arg2]

def instr_and(inst : Instruction, chip8 : Chip8): 
    chip8.v[inst.arg1] &= chip8.v[inst.arg2]

def instr_xor(inst : Instruction, chip8 : Chip8): 
    chip8.v[inst.arg1] ^= chip8.v[inst.arg2]

def instr_add8(inst : Instruction, chip8 : Chip8): 
    chip8.v[inst.arg1] += chip8.v[inst.arg2]
    if chip8.v[inst.arg1] > 0xFF:
        chip8.v[0xF] = 1
        chip8.v[inst.arg1] &= 0xFF
    else:
        chip8.v[0xF] = 0


def instr_sub(inst : Instruction, chip8 : Chip8): 
    chip8.v[inst.arg1] -= chip8.v[inst.arg2] 
    if chip8.v[inst.arg1] < 0:
        chip8.v[inst.arg1] &= 0xFF
        chip8.v[0xf] = 0
    else:
        chip8.v[0xf] = 1
    

def instr_shr(inst : Instruction, chip8 : Chip8): 
    chip8.v[0xf] = chip8.v[inst.arg1] & 1
    chip8.v[inst.arg1] >>= 1

def instr_subn(inst : Instruction, chip8 : Chip8): 
    chip8.v[inst.arg1] = chip8.v[inst.arg2] - chip8.v[inst.arg2]
    if chip8.v[inst.arg2] < 0:
        chip8.v[inst.arg2] &= 0xFF
        chip8.v[0xf] = 0
    else:
        chip8.v[0xf] = 1
    

def instr_shl(inst : Instruction, chip8 : Chip8): 
    chip8.v[0xf] = chip8.v[inst.arg1] >> 7
    chip8.v[inst.arg1] <<= 1


def instr_sne9(inst : Instruction, chip8 : Chip8): 
    if chip8.v[inst.arg1] != chip8.v[inst.arg2]:
        chip8.pc += 2

def instr_ld_i(inst : Instruction, chip8 : Chip8): 
    chip8.i = inst.arg1

def instr_jp_v0(inst : Instruction, chip8 : Chip8): 
    chip8.pc = chip8.v[0] + inst.arg1

def instr_rnd(inst : Instruction, chip8 : Chip8): 
    chip8.v[inst.arg1] = random.randint(0, 255) & inst.arg2

def instr_drw(inst : Instruction, chip8 : Chip8): 
    addr = chip8.i
    n = inst.arg3
    x = chip8.v[inst.arg1]
    y = chip8.v[inst.arg2]
    start = y*64 + x
    chip8.v[0xf] = 0
    for i in range(n):
        for j in range(8):
            frameAddr = (start + i*8 + j) % len(chip8.framebuf)
            bit = (chip8.memory[addr+i] >> j) & 1
            if bit == 1 and chip8.framebuf[frameAddr] == 1:
                chip8.v[0xf] = 1
            chip8.framebuf[frameAddr] ^= bit
    

def instr_skp(inst : Instruction, chip8 : Chip8): 
    if chip8.keys[chip8.v[inst.arg1]]:
        chip8.pc += 2

def instr_sknp(inst : Instruction, chip8 : Chip8): 
    if not chip8.keys[chip8.v[inst.arg1]]:
        chip8.pc += 2

def instr_ld_dt(inst : Instruction, chip8 : Chip8): 
    chip8.dt = chip8.v[inst.arg1]

def instr_ld_key(inst : Instruction, chip8 : Chip8): 
    chip8.ld_key_reg = inst.arg1

def instr_ld_st(inst : Instruction, chip8 : Chip8): 
    chip8.st = chip8.v[inst.arg1]

def instr_add_i(inst : Instruction, chip8 : Chip8): 
    chip8.i += chip8.v[inst.arg1]
    chip8.i &= 0xFFFF

def instr_ld_f(inst : Instruction, chip8 : Chip8): 
    chip8.i = 5*chip8.v[inst.arg1]  # font address

def instr_ld_b(inst : Instruction, chip8 : Chip8): 
    a = chip8.v[inst.arg1]
    chip8.memory[chip8.i] = a // 100
    chip8.memory[chip8.i+1] = (a // 10) % 10
    chip8.memory[chip8.i+2] = a % 10

def instr_ld_ptr_i(inst : Instruction, chip8 : Chip8): 
    for i in range(inst.arg1):
        chip8.memory[chip8.i + i] = chip8.v[i]

def instr_ld_vx_i(inst : Instruction, chip8 : Chip8): 
    for i in range(inst.arg1):
        chip8.v[i] = chip8.memory[chip8.i + i]
 

