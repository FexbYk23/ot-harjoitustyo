
import instructions


class Instruction:
    def __init__(self, opcode):

        self.op = instructions.instr_invalid
        self.raw = opcode

        if opcode == 0xE0:
            self.op = instructions.instr_cls
            return
        elif opcode == 0xEE:
            self.op = instructions.instr_ret
            return

        top4 = opcode >> 12
        if top4 == 0:
            self.op = instructions.instr_sys
        elif top4 == 1:
            self.arg1 = opcode & 0xFFF
            self.op = instructions.instr_jp
        elif top4 == 2:
            self.arg1 = opcode & 0xFFF
            self.op = instructions.instr_call
        elif top4 == 3:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instructions.instr_se3
        elif top4 == 4:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instructions.instr_sne
        elif top4 == 5:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = (opcode >> 4) & 0xF
            self.op = instructions.instr_se5
        elif top4 == 6:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instructions.instr_ld6
        elif top4 == 7:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instructions.instr_add
        elif top4 == 8:
            bottom4 = opcode & 0xF
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = (opcode >> 4) & 0xF
            if bottom4 == 0:
                self.op = instructions.instr_ld8
            elif bottom4 == 1:
                self.op = instructions.instr_or
            elif bottom4 == 2:
                self.op = instructions.instr_and
            elif bottom4 == 3:
                self.op = instructions.instr_xor
            elif bottom4 == 4:
                self.op = instructions.instr_add8
            elif bottom4 == 5:
                self.op = instructions.instr_sub
            elif bottom4 == 6:
                self.op = instructions.instr_shr
            elif bottom4 == 7:
                self.op = instructions.instr_subn
            elif bottom4 == 0xE:
                self.op = instructions.instr_shl

        elif top4 == 9:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = (opcode >> 4) & 0xF
            self.op = instructions.instr_sne9
        elif top4 == 0xA:
            self.arg1 = opcode & 0xFFF
            self.op = instructions.instr_ld_i
        elif top4 == 0xB:
            self.arg1 = opcode & 0xFFF
            self.op = instructions.instr_jp_v0
        elif top4 == 0xC:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = opcode & 0xFF
            self.op = instructions.instr_rnd
        elif top4 == 0xD:
            self.arg1 = (opcode >> 8) & 0xF
            self.arg2 = (opcode >> 4) & 0xF
            self.arg3 = (opcode) & 0xF
            self.op = instructions.instr_drw
        elif top4 == 0xE:
            self.arg1 = (opcode >> 8) & 0xF
            if opcode & 0xFF == 0x9E:
                self.op = instructions.instr_skp
            elif opcode & 0xFF == 0xA1:
                self.op = instructions.instr_sknp

        elif top4 == 0xF:
            bot8 = opcode & 0xFF
            self.arg1 = (opcode >> 8) & 0xF
            if bot8 == 7:
                self.op = instructions.instr_ld_vx_dt
            elif bot8 == 0xA:
                self.op = instructions.instr_ld_key
            elif bot8 == 0x15:
                self.op = instructions.instr_ld_dt
            elif bot8 == 0x18:
                self.op = instructions.instr_ld_st
            elif bot8 == 0x1E:
                self.op = instructions.instr_add_i
            elif bot8 == 0x29:
                self.op = instructions.instr_ld_f
            elif bot8 == 0x33:
                self.op = instructions.instr_ld_b
            elif bot8 == 0x55:
                self.op = instructions.instr_ld_ptr_i
            elif bot8 == 0x65:
                self.op = instructions.instr_ld_vx_i

    def execute(self, chip8):
        self.op(self, chip8)
