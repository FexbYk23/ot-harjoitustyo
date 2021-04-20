import time
import tkinter as tk
import tkinter.filedialog
import chip8
import settings



class MainWindow:
    PIXEL_SIZE = 8

    def __init__(self, root):
        self.root = root

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Open Program", command=self.open_program)
        menubar.add_cascade(label="File", menu=menu1)
        
        self.cfg = settings.Settings()
        
        self.canvas = tk.Canvas(root, bg="black", height=32*self.PIXEL_SIZE, width=64*self.PIXEL_SIZE)
        self.canvas.pack()
        root.after(10, self.mainloop)
        
        self.running = False

    def open_program(self):
        self.chip8 = chip8.Chip8()
        filename = tk.filedialog.askopenfilename()
        self.chip8.load_program_file(filename, self.cfg.get_entrypoint())
        self.__update_canvas()
        self.running = True
        #self.chip8.debug_print = True
        
        self.root.bind("<KeyPress>", self.__on_keypress_event)
        self.root.bind("<KeyRelease>", self.__on_keyrelease_event)

    def __update_canvas(self):
        c = self.canvas
        PIXEL = self.PIXEL_SIZE
        c.delete("all")
        for y in range(32):
            for x in range(64):
                if self.chip8.framebuf[y*64 + x]:
                    sx = x*PIXEL
                    sy = y*PIXEL
                    c.create_rectangle(sx, sy, sx+PIXEL, sy+PIXEL, fill="white" )

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
        prev_time = 0   # time of previous timer update
        while True:
            self.root.update()
            if not self.running:
                continue
            
            self.chip8.exec_next()
            self.__update_canvas()
            
            if time.time() - prev_time > 60 / 1000:
                self.chip8.update_timers()
                prev_time = time.time()

