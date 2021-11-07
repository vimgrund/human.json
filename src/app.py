
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

# change file name to don't delete anyones data 
#  somefile.json -> somefile-human.json
parts = filename.split('.')
filename =str.join('.',parts[0:-1]) + "-human." + parts[-1]
root.title(filename)

json_frame = JsonFrame(root, data)
json_frame.grid(row=0)
# json_frame.pack()


def button_save_click():
    "stores json dump to disk"
    dump = json_frame.getDump()
    print(dump)
    with open(filename,"w") as f:
      jsondump = json.dumps(json.loads(dump),indent=4)
      f.write(jsondump)


button = tk.Button(root, text="save", command=button_save_click)
# button.pack()
button.grid(row=1)

root.mainloop()
