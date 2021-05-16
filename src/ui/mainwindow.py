import time
import tkinter as tk
import tkinter.filedialog
import chip8
import ui.dialog_manager
import settings
import ui.settings_dialog
import ui.controls_dialog
from tkinter import messagebox
import sound_player


class MainWindow:
    """Ohjelman pääikkuna
    Attributes:
        root: tkinter
        chip8: Chip8 olio
        cfg: asetukset
        canvas: tkinter.Canvas johon piirretään emulaattorin kuva
        dialogs: Pitää kirjaa avatuista ikkunoista
        running: boolean, joka kertoo suorittaako emulaattori ohjelmaa
        paused: boolean, joka kertoo onko emulaattori pysäytetty pause napista
        music: äänentoistoon käytettävä SoundPlayer olio
        prev_tick: edellinen ajanhetki jolloin chip8 ajastimet on päivitetty
        __menu1: "File" valikko
    """
    PIXEL_SIZE = 8

    def __init__(self, root):
        self.root = root
        self.cfg = settings.Settings("settings.cfg")

        self.__create_menu()

        self.canvas = tk.Canvas(root, bg=self.cfg.get_bgcolor(
        ), height=32*self.PIXEL_SIZE, width=64*self.PIXEL_SIZE)
        self.canvas.pack()

        self.dialogs = ui.dialog_manager.DialogManager()
        self.running = False
        self.paused = False

        self.music = sound_player.SoundPlayer()
        if not self.music.available:
            messagebox.showinfo("Warning","Sound playback is not available.")

        self.chip8 = None

    def __create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Open Program", command=self.__open_program)
        menu1.add_command(
            label="Reset", command=self.__reset, state=tk.DISABLED)
        menu1.add_command(
            label="Pause", command=self.__pause, state=tk.DISABLED)
        menu1.add_command(label="Settings", command=self.__open_settings)
        menu1.add_command(label="Controls", command=self.__open_controls)
        menubar.add_cascade(label="File", menu=menu1)
        self.__menu1 = menu1

    def __open_program(self):
        """Avaa käyttöliittymän josta käyttäjä voi valita suoritettavan ohjelman sisältävän tiedoston. Aloittaa ohjelman suorittamisen, jos tiedosto valitaan.
        """
        filename = tk.filedialog.askopenfilename()
        if not isinstance(filename, str):
            return
        self.chip8 = chip8.Chip8()
        self.chip8.load_program_file(filename, self.cfg.get_entrypoint())
        self.__update_canvas()
        self.running = True
        self.prev_tick = time.time()

        self.root.bind("<KeyPress>", self.__on_keypress_event)
        self.root.bind("<KeyRelease>", self.__on_keyrelease_event)
        self.__enable_pause_reset()

    def __update_canvas(self):
        """Piirtää canvasiin chip8:n senhetkisen kuvan
        """
        fgcolor = self.cfg.get_fgcolor()
        c = self.canvas
        c.configure(bg=self.cfg.get_bgcolor())
        PIXEL = self.PIXEL_SIZE
        c.delete("all")
        for y in range(32):
            for x in range(64):
                if self.chip8.framebuf[y*64 + x]:
                    sx = x*PIXEL
                    sy = y*PIXEL
                    c.create_rectangle(
                        sx, sy, sx+PIXEL, sy+PIXEL, fill=fgcolor)

    def __update_keys_from_event(self, key, pressed):
        bindings = self.cfg.get_keybinds()
        for i in range(16):
            if bindings[i] == key:
                self.chip8.keys[i] = pressed

    def __on_keypress_event(self, e):
        self.__update_keys_from_event(e.keysym, True)

    def __on_keyrelease_event(self, e):
        self.__update_keys_from_event(e.keysym, False)

    def mainloop(self):
        """Päivittää emulaattorin kuvan, äänen, ajastimet ja suorittaa konekäskyjä"""
        if not self.running or self.paused:
            self.root.after(200, self.mainloop)
            return

        if self.chip8.halted:
            self.running = False
            messagebox.showinfo(
                "Error", "Chip8 halted:\n"+self.chip8.halt_reason)
            self.root.after(200, self.mainloop)

        self.chip8.exec_next()
        if time.time() - self.prev_tick > 60 / 1000:
            self.chip8.update_timers()
            self.prev_tick = time.time()
            self.__update_canvas()
            if self.chip8.st != 0 and not self.cfg.get_mute():
                self.music.play_beep()
            else:
                self.music.stop_beep()

        self.root.after(int(1000 / self.cfg.get_frequency()), self.mainloop)

    def __open_settings(self):
        """Avaa asetusvalikon"""
        if not self.dialogs.settings_open:
            self.dialogs.settings_open = True
            ui.settings_dialog.SettingsDialog(
                self.root, self.cfg, self.dialogs)

    def __open_controls(self):
        """Avaa näppäinasetukset"""
        if not self.dialogs.controls_open:
            self.dialogs.controls_open = True
            ui.controls_dialog.ControlsDialog(
                self.root, self.cfg, self.dialogs)

    def __reset(self):
        """Aloittaa emulaation alusta"""
        if self.chip8 != None:
            self.running = True
            self.chip8.reset(self.cfg.get_entrypoint())

    def __pause(self):
        """Pysäyttää/jatkaa emulaatiota"""
        self.paused = not self.paused

    def __enable_pause_reset(self):
        """Aktivoi pause ja reset valinnat"""
        self.__menu1.entryconfig(1, state=tk.NORMAL)
        self.__menu1.entryconfig(2, state=tk.NORMAL)
