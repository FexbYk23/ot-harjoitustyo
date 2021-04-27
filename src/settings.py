import configparser

class Settings:
    def __init__(self, filename=None):
        self.cfg = configparser.ConfigParser()
        self.load_defaults()
        if filename != None:
            self.load(filename)

    def load_values_from_cfg(self):
        s = self.cfg["Settings"]

        self.freq = int(s["frequency"])
        self.freq = min(max(self.freq, 1), 1000)
        self.keys = [s["key_{:01X}".format(i)] for i in range(16)]
        
        self.entrypoint = int(s["entrypoint"])
        self.entrypoint = min(max(self.entrypoint, 0), 0x1000 - 2)

    def load(self, filename):
        self.cfg.read(filename)
        if "Settings" in self.cfg:
            self.load_values_from_cfg()

    def save(self, filename):
        s = self.cfg["Settings"]
        s["frequency"] = str(self.freq)
        s["entrypoint"] = str(self.entrypoint)
        for i in range(16):
            s["key_{:01X}".format(i)] = self.keys[i]

        with open(filename, "w") as f:
            self.cfg.write(f)

    def load_defaults(self):
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
                "key_f":"y"}
        self.load_values_from_cfg()


    def get_frequency(self):
        return self.freq

    def get_entrypoint(self):
        return self.entrypoint

    def get_keybinds(self):
        return self.keys
