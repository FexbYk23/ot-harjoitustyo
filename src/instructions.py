
import random


def instr_invalid(inst, chip8):
    """Ei kelpaava komento joka pysäyttää järjestelmän"""
    chip8.halted = True
    chip8.halt_reason = "invalid instruction {:04X} at 0x{:04X}".format(
        inst.raw, chip8.pc)


def instr_sys(inst, chip8):
    """Toteuttamaton komento, jonka pitäisi suorittaa koodia RCA 1802 -prosessorilla"""
    chip8.halted = True
    chip8.halt_reason = f"Unimplemented sys instruction at {chip8.pc:04X}"


def instr_cls(inst, chip8):
    """Tyhjentää ruudun"""
    for i in range(len(chip8.framebuf)):
        chip8.framebuf[i] = False


def instr_ret(inst, chip8):
    """Palaa aliohjelmasta"""
    chip8.pc = chip8.read_word(chip8.sp)
    chip8.sp -= 2


def instr_jp(inst, chip8):
    """Hyppää määrättyyn kohtaan"""
    chip8.pc = inst.arg1


def instr_call(inst, chip8):
    """Kutsuu aliohjelmaa"""
    chip8.sp += 2
    chip8.write_word(chip8.sp, chip8.pc)
    chip8.pc = inst.arg1


def instr_se3(inst, chip8):
    """Ohittaa seuraavan konekäskyn jos valitun rekisterin arvo on yhtäsuuri kuin valittu vakio"""
    if chip8.v[inst.arg1] == inst.arg2:
        chip8.pc += 2


def instr_sne(inst, chip8):
    """Ohittaa seuraavan konekäskyn jos valitun rekisterin arvo ei ole yhtäsuuri
    kuin valittu vakio"""
    if chip8.v[inst.arg1] != inst.arg2:
        chip8.pc += 2


def instr_se5(inst, chip8):
    """Ohittaa seuraavan konekäskyn jos valitun rekisterin arvo on yhtäsuuri
    kuin toisen valitun rekisterin arvo"""
    if chip8.v[inst.arg1] == chip8.v[inst.arg2]:
        chip8.pc += 2


def instr_ld6(inst, chip8):
    """Lataa määrätyn vakion määrättyyn rekisteriin"""
    chip8.v[inst.arg1] = inst.arg2


def instr_add(inst, chip8):
    """Lisää määrättyyn rekisteriin vakion
    """
    chip8.v[inst.arg1] += inst.arg2
    chip8.v[inst.arg1] &= 0xFF


def instr_ld8(inst, chip8):
    """Kopioi määrättyyn rekisteriin arvon toisesta määrätystä rekisteristä"""
    chip8.v[inst.arg1] = chip8.v[inst.arg2]


def instr_or(inst, chip8):
    chip8.v[inst.arg1] |= chip8.v[inst.arg2]


def instr_and(inst, chip8):
    chip8.v[inst.arg1] &= chip8.v[inst.arg2]


def instr_xor(inst, chip8):
    chip8.v[inst.arg1] ^= chip8.v[inst.arg2]


def instr_add8(inst, chip8):
    """Lisää määrättyyn rekisteriin toisen määrätyn rekisterin arvon
    ja asettaa rekisteriin vf tiedon ylivuodosta
    """
    chip8.v[inst.arg1] += chip8.v[inst.arg2]
    if chip8.v[inst.arg1] > 0xFF:
        chip8.v[0xF] = 1
        chip8.v[inst.arg1] &= 0xFF
    else:
        chip8.v[0xF] = 0


def instr_sub(inst, chip8):
    """Vähentää määrätystä rekisteristä toisen määrätyn rekisterin arvon
    ja asettaa rekisteriin vf tiedon alivuodosta
    """
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
    """Siirtää määrätyn rekisterin bittejä vasemmalle yhdellä.
    Tallentaa hävinneen bitin arvon rekisteriin vf
    """
    chip8.v[0xf] = chip8.v[inst.arg1] >> 7
    chip8.v[inst.arg1] <<= 1
    chip8.v[inst.arg1] &= 0xff


def instr_sne9(inst, chip8):
    if chip8.v[inst.arg1] != chip8.v[inst.arg2]:
        chip8.pc += 2


def instr_ld_i(inst, chip8):
    chip8.i = inst.arg1


def instr_jp_v0(inst, chip8):
    chip8.pc = chip8.v[0] + inst.arg1


def instr_rnd(inst, chip8):
    """Tallentaa määrättyyn rekisteriin satunnaisluvun
    """
    chip8.v[inst.arg1] = random.randint(0, 255) & inst.arg2


def instr_drw(inst, chip8):
    chip8.v[0xf] = 0
    for i in range(inst.arg3):  # for each row in sprite
        rowdata = chip8.memory[chip8.i + i]
        _y = (chip8.v[inst.arg2] + i) % 32
        for j in range(8):
            _x = (chip8.v[inst.arg1] + j) % 64
            pixel = ((rowdata >> (7-j)) & 1)
            if pixel and chip8.framebuf[_y*64 + _x]:
                chip8.v[0xf] = 1
            chip8.framebuf[_y*64 + _x] ^= pixel


def instr_skp(inst, chip8):
    """Ohittaa seuraavan komennon jos määrätyn rekisterin
    määräämä nappi on painettuna"""
    if chip8.keys[chip8.v[inst.arg1]]:
        chip8.pc += 2


def instr_sknp(inst, chip8):
    """Ohittaa sueraavan komennon jos määrätyn rekisterin
    määräämä nappi ei ole painettuna"""
    if not chip8.keys[chip8.v[inst.arg1]]:
        chip8.pc += 2


def instr_ld_vx_dt(inst, chip8):
    """Kopioi määrättyyn rekisteriin viiveajastimen arvon"""
    chip8.v[inst.arg1] = chip8.dt


def instr_ld_dt(inst, chip8):
    """Kopioi viiveajastimeen määrätyn rekisterin arvon"""
    chip8.dt = chip8.v[inst.arg1]


def instr_ld_key(inst, chip8):
    """Pysäyttää suorituksen kunnes jotain nappia on painettu
    ja tallentaa painetun napin määrättyyn rekisteriin
    """
    chip8.ld_key_reg = inst.arg1


def instr_ld_st(inst, chip8):
    """Kopioi ääniajastimeen määrätyn rekisterin arvon
    """
    chip8.st = chip8.v[inst.arg1]


def instr_add_i(inst, chip8):
    """Lisää I-rekisteriin määrätyn rekisterin arvon"""
    chip8.i += chip8.v[inst.arg1]
    chip8.i &= 0xFFFF


def instr_ld_f(inst, chip8):
    """Tallentaa i rekisteriin määrätyn rekisterin sisältämän merkin osoitteen
    järjestelmän sisäisessä fontissa (Olettaen että fontii alkaa kohdasta 0 muistissa).
    """
    chip8.i = 5*chip8.v[inst.arg1]  # font address


def instr_ld_b(inst, chip8):
    """Tallentaa määrätyn rekisterin arvon BCD-koodattuna I-rekisterin määräämään paikkaan
    """
    _a = chip8.v[inst.arg1]
    chip8.memory[chip8.i] = _a // 100
    chip8.memory[chip8.i+1] = (_a // 10) % 10
    chip8.memory[chip8.i+2] = _a % 10


def instr_ld_ptr_i(inst, chip8):
    """Kopioi I-rekisterin määräämään osoitteeseen määrättyjen rekisterien arvot"""
    for i in range(inst.arg1 + 1):
        chip8.memory[chip8.i + i] = chip8.v[i]


def instr_ld_vx_i(inst, chip8):
    """Kopioi määrättyihin rekistereihin I-rekisterin määräämästä osoitteesta arvoja
    """
    for i in range(inst.arg1 + 1):
        chip8.v[i] = chip8.memory[chip8.i + i]
