import tkinter as tk
import json
class aplication(tk.Frame):
  def __init__(self,master):
    super().__init__(master)
    master.geometry("300x300")
    master.title("app")
    self.pack()
    self.create_textbox()
    self.create_lbl(20,10)
  def create_lbl(self,x,y):
    lbl = tk.Label()
    lbl.place(x=x,y=y) 
    lbl["text"]="A"
  def create_textbox(self):
    textbox = tk.Entry(self)
    textbox['width']=20
    textbox.place(x=60,y=20)
root = tk.Tk()
app = aplication(root)
app.mainloop()