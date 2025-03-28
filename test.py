import tkinter as tk
from tkinter import ttk
import json 
with open("drink.json") as f:
  items=list(json.load(f).keys())
  
root = tk.Tk()
root.title("コンボボックスの基本")
root.geometry("300x300")
combo = ttk.Combobox(root, values=items)
combo.pack(pady=10)

root.mainloop()
