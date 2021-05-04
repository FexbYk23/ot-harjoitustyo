
class DialogManager:
    """Luokka, joka pitää kirjaa avatuista ikkunoista, jotta käyttäjä ei voisi avata samaa ikkunaa useasti
    """

    def __init__(self):
        self.mainwindow_open = True
        self.settings_open = False
        self.controls_open = False

    def is_dialog_open(self):
        return self.settings_open or self.controls_open
