import tkinter
import ui.mainwindow

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Chip8")
    mainwindow = ui.mainwindow.MainWindow(root)
    #mainwindow.mainloop()
    root.after(1, mainwindow.mainloop2)
    root.mainloop()
