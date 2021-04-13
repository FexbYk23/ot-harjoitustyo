import chip8

def printRegs(c8):
    print("PC:", c8.pc, "Registers:", c8.v)


if len(sys.argv) != 2:
    exit("USAGE: chip8 program")


with open(sys.argv[1], "rb") as f:
    program = f.read()

c8 = chip8.Chip8()
c8.loadProgram(program)

printRegs()
c8.exec_next()
printRegs()

