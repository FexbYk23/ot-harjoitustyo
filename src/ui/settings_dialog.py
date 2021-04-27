import tkinter as tk
from tkinter import messagebox
import settings
import ui.dialog_manager



class SettingsDialog:
    def __init__(self, master, settings, dialogs):
        self.window = tk.Toplevel()
        self.cfg = settings
        self.dialogs = dialogs

        tk.Label(self.window, text="Entrypoint:").pack()
        self.entrypoint_entry = self.__create_entry(str(self.cfg.get_entrypoint()))
        
        tk.Label(self.window, text="Emulation speed (Hz):").pack()
        self.freq_entry = self.__create_entry(str(self.cfg.get_frequency()))

        tk.Label(self.window, text="Foreground color:").pack()
        self.fgcolor_entry = self.__create_entry(self.cfg.get_fgcolor())

        tk.Label(self.window, text="Background color:").pack()
        self.bgcolor_entry = self.__create_entry(self.cfg.get_bgcolor())


        tk.Button(self.window, text="OK", command=self.__ok).pack()
        tk.Button(self.window, text="Cancel", command=self.__close).pack()
    
    def __create_entry(self, initial_value):
        e = tk.Entry(self.window)
        e.insert(tk.END, initial_value)
        e.pack(padx=10, pady=(0, 10))
        return e

    def __close(self):
        self.window.destroy()
        self.dialogs.settings_open = False

    def __ok(self):
        if self.validate_settings():
            self.cfg.freq = int(self.freq_entry.get())
            self.cfg.entrypoint = int(self.entrypoint_entry.get())
            self.cfg.fgcolor = self.fgcolor_entry.get()
            self.cfg.bgcolor = self.bgcolor_entry.get()
            self.cfg.save("settings.cfg")
            self.window.destroy()
            self.dialogs.settings_open = False

    def validate_settings(self):
        try:
            if not 0 < int(self.freq_entry.get()) <= 1000:
                messagebox.showinfo("Error", "Frequency must be between 1 and 1000")
                return False
        except ValueError:
            messagebox.showinfo("Error", "Frequency must be an integer.")
            return False

        try:
            int(self.entrypoint_entry.get())
        except ValueError:
            messagebox.showinfo("Error", "Entrypoint must be an integer.")
            return False
        
        if not settings.is_valid_color(self.fgcolor_entry.get()):
            messagebox.showinfo("Error", "Foreground color is not a valid color")
            return False
        if not settings.is_valid_color(self.bgcolor_entry.get()):
            messagebox.showinfo("Error", "Background color is not a calid color")
            return False

        return True
