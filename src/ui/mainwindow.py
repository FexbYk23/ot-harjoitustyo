import time
import tkinter as tk
import tkinter.filedialog
import chip8
import ui.dialog_manager
import settings
import ui.settings_dialog, ui.controls_dialog
from tkinter import messagebox

class MainWindow:
    PIXEL_SIZE = 8

    def __init__(self, root):
        self.root = root

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Open Program", command=self.__open_program)
        menu1.add_command(label="Settings", command=self.__open_settings)
        menu1.add_command(label="Controls", command=self.__open_controls)
        menubar.add_cascade(label="File", menu=menu1)
        
        self.cfg = settings.Settings("settings.cfg")
        
        self.canvas = tk.Canvas(root, bg="#000000", height=32*self.PIXEL_SIZE, width=64*self.PIXEL_SIZE)
        self.canvas.pack()
        
        self.dialogs = ui.dialog_manager.DialogManager()
        self.running = False

    def __open_program(self):
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

    def __update_canvas(self):
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
                    c.create_rectangle(sx, sy, sx+PIXEL, sy+PIXEL, fill=fgcolor)

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
        if not self.running:
            self.root.after(200, self.mainloop)
            return
        
        if self.chip8.halted:
            self.running = False
            messagebox.showinfo("Error", "Chip8 halted:\n"+self.chip8.halt_reason)
            self.root.after(200, self.mainloop)

        self.chip8.exec_next()
        if time.time() - self.prev_tick > 60 / 1000:
            self.chip8.update_timers()
            self.prev_tick = time.time()
            self.__update_canvas()

        self.root.after(int(1000/self.cfg.get_frequency()), self.mainloop)

    def __open_settings(self):
        if not self.dialogs.settings_open:
            self.dialogs.settings_open = True
            ui.settings_dialog.SettingsDialog(self.root, self.cfg, self.dialogs)
    
    def __open_controls(self):
        if not self.dialogs.controls_open:
            self.dialogs.controls_open = True
            ui.controls_dialog.ControlsDialog(self.root, self.cfg, self.dialogs)

