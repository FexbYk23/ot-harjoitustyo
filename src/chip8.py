import instruction

class Chip8:

    def __init__(self):
        self.memory = [0 for i in range(0x1000)]
        self.framebuf = [0 for i in range(64 * 32)] 
        self.keys = [False for i in range(16)]
        self.loadFont()

        # Registers
        self.v = [0 for i in range(16)]
        self.i = 0
        self.pc = 0
        self.sp = 0

        # Timers
        self.dt = 0
        self.st = 0

        # Set to Vx on instruction Fx0A
        # If not -1, halt execution until a keypress and store it to Vx
        self.ld_key_reg = -1
    
    def loadFont(self):
        font = [0xf0, 0x90, 0x90, 0x90, 0xf0, #0
                0x20, 0x60, 0x20, 0x20, 0x70, #1
                0xf0, 0x10, 0xf0, 0x80, 0xf0, #2
                0xf0, 0x10, 0xf0, 0x10, 0xf0, #3
                0x90, 0x90, 0xf0, 0x10, 0x10, #4
                0xf0, 0x80, 0xf0, 0x10, 0xf0, #5
                0xf0, 0x80, 0xf0, 0x90, 0xf0, #6
                0xf0, 0x10, 0x20, 0x40, 0x40, #7
                0xf0, 0x90, 0xf0, 0x90, 0xf0, #8
                0xf0, 0x90, 0xf0, 0x10, 0xf0, #9
                0xf0, 0x90, 0xf0, 0x90, 0x90, #A
                0xE0, 0x90, 0xE0, 0x90, 0xE0, #B
                0xf0, 0x80, 0x80, 0x80, 0xF0, #C
                0xe0, 0x90, 0x90, 0x90, 0xE0, #D
                0xF0, 0x80, 0xf0, 0x80, 0xf0, #E
                0xF0, 0x80, 0xF0, 0x80, 0x80  #F
                ]

        for i in range(len(font)):
            self.memory[i] = font[i]

    def loadProgram(self, program, entrypoint):
        for i in range(len(program)):
            self.memory[entrypoint + i] = program[i]
        self.pc = entrypoint

    def write_word(self, addr, data):
        self.memory[addr] = data & 0xFF
        self.memory[addr + 1] = data >> 8

    def read_word(self, addr):
        return self.memory[addr] | (self.memory[addr+1] << 8)
    
    def exec_next(self):
        inst = instruction.Instruction(self.read_word(self.pc))
        self.pc += 2
        inst.execute(self)

