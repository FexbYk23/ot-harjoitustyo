import configparser

class Settings:
    def __init__(self, filename=None):
        self.cfg = configparser.ConfigParser()
        if filename != None:
            load(filename)
        if not "Settings" in self.cfg:
            self.load_default_settings()
        self.load_values_from_cfg()

    def load_values_from_cfg(self):
        self.freq = int(self.cfg["Settings"]["frequency"])
        self.keys = [self.cfg["Settings"]["key_{:01X}".format(i)] for i in range(16)]
        
        self.entrypoint = int(self.cfg["Settings"]["entrypoint"])

    def load(self, filename):
        self.cfg.read(filename)

    def save(self, filename):
        with open(filename, "w") as f:
            self.cfg.write(f)

    def load_default_settings(self):
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


    def get_frequency(self):
        return self.freq

    def get_entrypoint(self):
        return self.entrypoint

    def get_keybinds(self):
        return self.keys
