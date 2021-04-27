import tkinter as tk
from tkinter import messagebox
import settings

class SettingsDialog:
    def __init__(self, master, settings):
        self.window = tk.Toplevel()
        self.cfg = settings

        tk.Label(self.window, text="Entrypoint:").pack()
        self.entrypoint_entry = tk.Entry(self.window)
        self.entrypoint_entry.insert(tk.END, str(self.cfg.get_entrypoint()))
        self.entrypoint_entry.pack()
        
        tk.Label(self.window, text="Frequency:").pack()
        self.freq_entry = tk.Entry(self.window)
        self.freq_entry.insert(tk.END, str(self.cfg.get_frequency()))
        self.freq_entry.pack()

        tk.Button(self.window, text="OK", command=self.__ok).pack()
        tk.Button(self.window, text="Close", command=self.__close).pack()
        
    def __close(self):
        self.window.destroy()

    def __ok(self):
        if self.validate_settings():
            self.cfg.freq = int(self.freq_entry.get())
            self.cfg.entrypoint = int(self.entrypoint_entry.get())
            self.cfg.save("settings.cfg")
            self.window.destroy()
        

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

        return True
