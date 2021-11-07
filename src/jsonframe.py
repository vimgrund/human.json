import json
import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP, W


class JsonFrame(tk.Frame):
    def __init__(self, root, json_data, toogle=True):
        tk.Frame.__init__(self, root, bg="#303030")
        self.mychildren = dict()
        start = tk.Label(self, text="{", bg="#303030", fg="#FFFFFF")
        start.grid(column=0, row=0)

        i = 1
        for key in json_data:
            blub = tk.Label(self, text=f"\"{key}\":", bg="#303030", fg="#FFFFFF")
            blub.grid(column=1, row=i, padx=3, pady=3, sticky='nw')
            value = json_data.get(key)
            frame = JsonItemFrame(self, value, not toogle)
            frame.grid(column=2, row=i, sticky=W)
            self.mychildren[key] = frame
            i += 1
        endlabel = tk.Label(self, text="}", bg="#303030", fg="#FFFFFF")
        endlabel.grid(column=0, row=i)

    def getDump(self):
        parts = list()
        for child in self.mychildren:
            parts.append(f"\"{child}\":{self.mychildren.get(child).getDump()}")
        something = "{" +str.join(",\n",parts) + "}"
        return something


class JsonItemFrame(tk.Frame):
    def __init__(self, root, value, toogle):
        tk.Frame.__init__(self, root)
        self.myValue = False
        if type(value) is int:
            self.myValue = tk.IntVar()
            self.myValue.set(value)
            frame = tk.Entry(self, textvariable=self.myValue,width=7,justify="right")
        elif type(value) is float \
                or type(value) is str:
            self.myValue = tk.StringVar()
            self.myValue.set(value)
            frame = tk.Entry(self, textvariable=self.myValue)
        elif type(value) is dict:
            frame = JsonFrame(self, value, not toogle)
            self.myValue = frame
        elif type(value) is list:
            frame = JsonArrayFrame(self, value, not toogle)
            self.myValue = frame
        # frame.grid(column=1, row=0, padx=3, pady=3)
        if toogle:
            frame.pack(side=LEFT)
        else:
            frame.pack(side=TOP)

    def getDump(self):
        result = "ERROR"
        if type(self.myValue) is tk.StringVar:
            result = f"\"{self.myValue.get()}\""
        elif type(self.myValue) is tk.IntVar:
            result = str(self.myValue.get())
        elif type(self.myValue) is JsonFrame \
            or type(self.myValue) is JsonArrayFrame:
            result = self.myValue.getDump()
        return result

class JsonArrayFrame(tk.Frame):
    def __init__(self, root, json_data, toogle):
        tk.Frame.__init__(self, root)
        self.mychildren = list()
        for value in json_data:
            frame = JsonItemFrame(self, value, not toogle)
            self.mychildren.append(frame)
            if toogle:
                frame.pack(side=LEFT)
            else:
                frame.pack(side=TOP)

    def getDump(self):
        parts = list()
        for child in self.mychildren:
            parts.append(child.getDump())
        something = "[" +str.join(",",parts) + "]"
        return something

class JsonTableFrame(tk.Frame):
    items = []

    def __init__(self, root, json_data):
        cf = tk.Frame.__init__(self, root)
        self.items = []
        i = 0
        header = tk.Frame(cf).pack()
        body = tk.Frame(cf).pack(side=BOTTOM)
        for item in json_data:
            self.items.append("something")
            tk.Entry(cf, textvariable=self.items[i]).pack(side=LEFT)
            i = i+1
