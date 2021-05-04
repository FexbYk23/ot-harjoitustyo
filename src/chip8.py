import instruction


class Chip8:
    """Luokka, joka sisältää chip8 järjestelmän tarvitsemat tiedot
    """

    def __init__(self):
        self.memory = [0 for i in range(0x1000)]
        self.reset(0)

    def reset(self, entrypoint=512):
        """Alustaa kaiken paitsi muistin"""
        self.__load_font()
        self.framebuf = [False for i in range(64 * 32)]
        self.keys = [False for i in range(16)]

        # Registers
        self.v = [0 for i in range(16)]
        self.i = 0
        self.pc = entrypoint
        self.sp = 0x100

        # Timers
        self.dt = 0
        self.st = 0

        # Set to Vx on instruction Fx0A
        # If not -1, halt execution until a keypress and store it to Vx
        self.ld_key_reg = -1
        
        self.debug_print = False
        self.halted = False
        self.halt_reason = ""
    
    def __load_font(self):
        """Kopioi fonttidatan emulaattorin muistiin kohtaan 0
        """

        font = [0xf0, 0x90, 0x90, 0x90, 0xf0,  # 0
                0x20, 0x60, 0x20, 0x20, 0x70,  # 1
                0xf0, 0x10, 0xf0, 0x80, 0xf0,  # 2
                0xf0, 0x10, 0xf0, 0x10, 0xf0,  # 3
                0x90, 0x90, 0xf0, 0x10, 0x10,  # 4
                0xf0, 0x80, 0xf0, 0x10, 0xf0,  # 5
                0xf0, 0x80, 0xf0, 0x90, 0xf0,  # 6
                0xf0, 0x10, 0x20, 0x40, 0x40,  # 7
                0xf0, 0x90, 0xf0, 0x90, 0xf0,  # 8
                0xf0, 0x90, 0xf0, 0x10, 0xf0,  # 9
                0xf0, 0x90, 0xf0, 0x90, 0x90,  # A
                0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
                0xf0, 0x80, 0x80, 0x80, 0xF0,  # C
                0xe0, 0x90, 0x90, 0x90, 0xE0,  # D
                0xF0, 0x80, 0xf0, 0x80, 0xf0,  # E
                0xF0, 0x80, 0xF0, 0x80, 0x80  # F
                ]

        for i in range(len(font)):
            self.memory[i] = font[i]

    def load_program(self, program, entrypoint):
        """Lukee ohjelman listasta muistiin
        Args:
            program: lista joka sisältää ohjelman
            entrypoint: kohta muistissa, johon ohjelma kopioidaan
        """
        for i in range(len(program)):
            self.memory[entrypoint + i] = program[i]
        self.pc = entrypoint
    
    def load_program_file(self, filename, entrypoint):
        """Lukee ohjelman tiedostosta muistiin
        Args:
            filename: polku tiedostoon
            entrypoint: kohta muistissa, johon ohjelma kopioidaan
        """
        with open(filename, "rb") as f:
            program = f.read(0x1000-entrypoint)
            self.load_program(program, entrypoint)


    def write_word(self, addr, data):
        """Kirjoittaa 16 bittiä muistiin
        Args:
            addr: muistiosoite
            data: kirjoitettava arvo
        """
        if addr + 1 >= len(self.memory):
            self.halted = True
            self.halt_reason = f"Out of bounds write to {addr}"
        self.memory[addr + 1] = data & 0xFF
        self.memory[addr] = data >> 8

    def read_word(self, addr):
        """Lukee 16 bittiä muistista
        Args:
            addr: muistiosoite
        """
        if addr + 1 >= len(self.memory):
            self.halted = True
            self.halt_reason = f"Out of bounds read from {addr}"
        return self.memory[addr + 1] | (self.memory[addr] << 8)

    def exec_next(self):
        """Suorittaa seuraavan konekäskyn jos emulaattoria ei ole pysäytetty
        """
        if self.halted:
            if self.debug_print:
                print("Chip8 Halted:", self.halt_reason)
            return

        if self.ld_key_reg != -1:
            for i in range(len(self.keys)):
                if self.keys[i]:
                    self.v[self.ld_key_reg] = i
                    self.ld_key_reg = -1
                    if self.debug_print:
                        print("Chip8: Key pressed:", i, self.keys)
                    break
            
            if self.ld_key_reg != -1:
                if self.debug_print:
                    print("Chip8: Waiting for keypress", self.keys)
                return


        inst = instruction.Instruction(self.read_word(self.pc))

        if self.debug_print:
            print("PC:", self.pc, " Registers:", self.v)
            print("Opcode: ", inst.op)
            pass
        self.pc += 2
        inst.execute(self)

    def update_timers(self):
        """Päivittää järjestelmän ajastimet. Tätä funktiota pitäisi kutsua 60 kertaa sekunnissa
        """
        if self.dt > 0:
            self.dt -= 1

        if self.st > 0:
            self.st -= 1

