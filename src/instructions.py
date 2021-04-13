import Chip8
# move these to different file

def instr_sys(inst : Instruction, chip8 : Chip8):
    #not implemented
    pass

def instr_cls(inst : Instruction, chip8 : Chip8):
    for i in range(len(chip8.framebuf)):
        chip8.framebuf[i] = 0

def instr_ret(inst : Instruction, chip8 : Chip8):
    chip8.pc = chip8.memory[chip8.sp]
    chip8.sp -= 1

def instr_jp(inst : Instruction, chip8 : Chip8):
    pass
