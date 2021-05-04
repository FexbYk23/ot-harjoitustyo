import configparser

def is_valid_color(color):
    """Määrittää onko color html muodossa oleva väri
    
    Args:
        color: merkkijono
    """
    if not isinstance(color, str):
        return False
    if len(color) != 7 or color[0] != "#":
        return False
    for i in range(1, 7):
        if not color[i] in "0123456789abcdefABCDEF":
            return False
    return True

class Settings:
    """Asetuksien säilyttämistä, lukemista ja tallentamista hoitava luokka

    Attributes:
        cfg: ConfigParser olio
        freq: emulaattorin suoritusnopeus
        keys: näppäinasetukset
        entrypoint: emulaattorin ohjelman latausosoite
        bgcolor: emulaattorin kuvan taustaväri
        fgcolor: emulaattorin kuvan etuväri
        mute: boolean joka kertoo onko äänet mykistetty
    """

    def __init__(self, filename=None):
        self.cfg = configparser.ConfigParser()
        self.load_defaults()
        if filename != None:
            self.load(filename)

    def load_values_from_cfg(self):
        """Lukee configparserin sisältämät arvot muuttujiin"""
        s = self.cfg["Settings"]

        self.freq = int(s["frequency"])
        self.freq = min(max(self.freq, 1), 1000)
        self.keys = [s["key_{:01X}".format(i)] for i in range(16)]
        
        self.entrypoint = int(s["entrypoint"])
        self.entrypoint = min(max(self.entrypoint, 0), 0x1000 - 2)
        
        self.fgcolor = s["fgcolor"]
        if not is_valid_color(self.fgcolor):
            self.fgcolor = "#ffffff"
        
        self.bgcolor = s["bgcolor"]
        if not is_valid_color(self.bgcolor):
            self.bgcolor = "#000000"

        self.mute = s.getboolean("mute_sound")
        

    def load(self, filename):
        """Lukee asetukset tiedostosta"""
        self.cfg.read(filename)
        if "Settings" in self.cfg:
            self.load_values_from_cfg()

    def save(self, filename):
        """Tallentaa asetukset tiedostoon"""
        s = self.cfg["Settings"]
        s["frequency"] = str(self.freq)
        s["entrypoint"] = str(self.entrypoint)
        s["fgcolor"] = self.fgcolor
        s["bgcolor"] = self.bgcolor
        for i in range(16):
            s["key_{:01X}".format(i)] = self.keys[i]
        
        s["mute_sound"] = str(self.mute)

        with open(filename, "w") as f:
            self.cfg.write(f)

    def load_defaults(self):
        """Lukee oletusasetukset"""
        self.cfg["Settings"] = {"frequency":10, "entrypoint":0x200,
                "key_0":"0",
                "key_1":"1",
                "key_2":"2",
                "key_3":"3", 
                "key_4":"4", 
                "key_5":"5",
                "key_6":"6",
                "key_7":"7",
                "key_8":"8",
                "key_9":"9",
                "key_a":"q",
                "key_b":"w",
                "key_c":"e",
                "key_d":"r",
                "key_e":"t", 
                "key_f":"y",
                "fgcolor":"#ffffff",
                "bgcolor":"#000000",
                "mute_sound":"False"}
        self.load_values_from_cfg()


    def get_frequency(self):
        return self.freq

    def get_entrypoint(self):
        return self.entrypoint

    def get_keybinds(self):
        return self.keys

    def get_fgcolor(self):
        return self.fgcolor

    def get_bgcolor(self):
        return self.bgcolor

    def get_mute(self):
        return self.mute
