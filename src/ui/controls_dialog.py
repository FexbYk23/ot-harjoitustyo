import tkinter as tk
from tkinter import messagebox
import settings
import ui.dialog_manager

class ControlsDialog:
    def __init__(self, master, settings, dialogs):
        self.window = tk.Toplevel()
        self.cfg = settings
        self.dialogs = dialogs
        self.key_entries = []

        for i in range(16):
            tk.Label(self.window, text=f"Key {i:01X}:").grid(row=i, column=0, padx=(10, 0))
            entry = tk.Entry(self.window)
            entry.insert(tk.END, self.cfg.get_keybinds()[i])
            entry.grid(row=i, column=1, padx=(0, 10))
            self.key_entries.append(entry)

        tk.Button(self.window, text="OK", command=self.__ok).grid(columnspan=2, row=16, column=0)


    def __ok(self):
        for i in range(16):
            self.cfg.get_keybinds()[i] = self.key_entries[i].get()
        self.cfg.save("settings.cfg")
        self.dialogs.controls_open = False
        self.window.destroy()

