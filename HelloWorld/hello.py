from tkinter import *

class Hello_GUI:
  def __init__(self, master):
    self.master = master
    master.title("Hello World")

    self.label = Label(master, text="Hello World!")
    self.label.pack()
root = Tk()
helloWorld = Hello_GUI(root)
root.mainloop() 
