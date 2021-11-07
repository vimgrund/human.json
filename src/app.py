
import json
from tkinter.constants import BOTH, BOTTOM, TOP
from jsonframe import JsonFrame
import tkinter as tk
import sys


if len(sys.argv) != 2:
    print("pleas provide a file")
    exit()

root = tk.Tk()
filename = sys.argv[1]
with open(filename) as f:
  data = json.load(f)

json_frame = JsonFrame(root, data)
json_frame.grid(row=0)
# json_frame.pack()

def button_click():
    print(json_frame.getDump())


button = tk.Button(root, text="clickme", command=button_click)
# button.pack()
button.grid(row=1)

root.mainloop()