
import random


def instr_invalid(inst, chip8):
    print("invalid instruction at:", chip8.pc)


def instr_sys(inst, chip8):
    #not implemented
    pass


def instr_cls(inst, chip8):
    for i in range(len(chip8.framebuf)):
        chip8.framebuf[i] = 0


def instr_ret(inst, chip8):
    chip8.pc = chip8.read_word(chip8.sp)
    chip8.sp -= 2


def instr_jp(inst, chip8):
    chip8.pc = inst.arg1


def instr_call(inst, chip8):
    chip8.sp += 2
    chip8.write_word(chip8.sp, chip8.pc)
    chip8.pc = inst.arg1


def instr_se3(inst, chip8):
    if chip8.v[inst.arg1] == inst.arg2:
        chip8.pc += 2


def instr_sne(inst, chip8):
    if chip8.v[inst.arg1] != inst.arg2:
        chip8.pc += 2


def instr_se5(inst, chip8):
    if chip8.v[inst.arg1] == chip8.v[inst.arg2]:
        chip8.pc += 2


def instr_ld6(inst, chip8):
    chip8.v[inst.arg1] = inst.arg2


def instr_add(inst, chip8):
    chip8.v[inst.arg1] += inst.arg2
    chip8.v[inst.arg1] &= 0xFF


def instr_ld8(inst, chip8):
    chip8.v[inst.arg1] = chip8.v[inst.arg2]


def instr_or(inst, chip8):
    chip8.v[inst.arg1] |= chip8.v[inst.arg2]


def instr_and(inst, chip8):
    chip8.v[inst.arg1] &= chip8.v[inst.arg2]


def instr_xor(inst, chip8):
    chip8.v[inst.arg1] ^= chip8.v[inst.arg2]


def instr_add8(inst, chip8):
    chip8.v[inst.arg1] += chip8.v[inst.arg2]
    if chip8.v[inst.arg1] > 0xFF:
        chip8.v[0xF] = 1
        chip8.v[inst.arg1] &= 0xFF
    else:
        chip8.v[0xF] = 0


def instr_sub(inst, chip8):
    chip8.v[inst.arg1] -= chip8.v[inst.arg2]
    if chip8.v[inst.arg1] < 0:
        chip8.v[inst.arg1] &= 0xFF
        chip8.v[0xf] = 0
    else:
        chip8.v[0xf] = 1


def instr_shr(inst, chip8):
    chip8.v[0xf] = chip8.v[inst.arg1] & 1
    chip8.v[inst.arg1] >>= 1


def instr_subn(inst, chip8):
    chip8.v[inst.arg1] = chip8.v[inst.arg2] - chip8.v[inst.arg2]
    if chip8.v[inst.arg2] < 0:
        chip8.v[inst.arg2] &= 0xFF
        chip8.v[0xf] = 0
    else:
        chip8.v[0xf] = 1


def instr_shl(inst, chip8):
    chip8.v[0xf] = chip8.v[inst.arg1] >> 7
    chip8.v[inst.arg1] <<= 1


def instr_sne9(inst, chip8):
    if chip8.v[inst.arg1] != chip8.v[inst.arg2]:
        chip8.pc += 2


def instr_ld_i(inst, chip8):
    chip8.i = inst.arg1


def instr_jp_v0(inst, chip8):
    chip8.pc = chip8.v[0] + inst.arg1


def instr_rnd(inst, chip8):
    chip8.v[inst.arg1] = random.randint(0, 255) & inst.arg2


def instr_drw(inst, chip8):
    chip8.v[0xf] = 0
    for i in range(inst.arg3 + 1):  # for each row in sprite
        rowdata = chip8.memory[chip8.i + i]
        y = (chip8.v[inst.arg2] + i) % 32
        for j in range(8):
            x = (chip8.v[inst.arg1] + j) % 64
            pixel = (rowdata >> (7-j)) & 1
            if pixel and chip8.framebuf[y*64 + x] == 1:
                chip8.v[0xf] = 1
            chip8.framebuf[y*64 + x] ^= pixel


def instr_skp(inst, chip8):
    if chip8.keys[chip8.v[inst.arg1]]:
        chip8.pc += 2


def instr_sknp(inst, chip8):
    if not chip8.keys[chip8.v[inst.arg1]]:
        chip8.pc += 2


def instr_ld_dt(inst, chip8):
    chip8.dt = chip8.v[inst.arg1]


def instr_ld_key(inst, chip8):
    chip8.ld_key_reg = inst.arg1


def instr_ld_st(inst, chip8):
    chip8.st = chip8.v[inst.arg1]


def instr_add_i(inst, chip8):
    chip8.i += chip8.v[inst.arg1]
    chip8.i &= 0xFFFF


def instr_ld_f(inst, chip8):
    chip8.i = 5*chip8.v[inst.arg1]  # font address


def instr_ld_b(inst, chip8):
    a = chip8.v[inst.arg1]
    chip8.memory[chip8.i] = a // 100
    chip8.memory[chip8.i+1] = (a // 10) % 10
    chip8.memory[chip8.i+2] = a % 10


def instr_ld_ptr_i(inst, chip8):
    for i in range(inst.arg1):
        chip8.memory[chip8.i + i] = chip8.v[i]


def instr_ld_vx_i(inst, chip8):
    for i in range(inst.arg1):
        chip8.v[i] = chip8.memory[chip8.i + i]
