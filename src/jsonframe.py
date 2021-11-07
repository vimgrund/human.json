import json
import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP, W


class JsonFrame(tk.Frame):
    def __init__(self, root, json_data):
        tk.Frame.__init__(self, root, bg="#303030")
        self.mychildren = dict()
        start = tk.Label(self, text="{", bg="#303030", fg="#FFFFFF")
        start.grid(column=0, row=0)

        i = 1
        for key in json_data:
            blub = tk.Label(
                self, text=f"\"{key}\":", bg="#303030", fg="#B0B0FF")
            blub.grid(column=1, row=i, padx=3, pady=3, sticky='nw')
            value = json_data.get(key)
            frame = JsonItemFrame(self, value)
            frame.grid(column=2, row=i, sticky=W)
            self.mychildren[key] = frame
            i += 1
        endlabel = tk.Label(self, text="}", bg="#303030", fg="#FFFFFF")
        endlabel.grid(column=0, row=i)

    def getDump(self):
        parts = list()
        for child in self.mychildren:
            parts.append(f"\"{child}\":{self.mychildren.get(child).getDump()}")
        something = "{" + str.join(",\n", parts) + "}"
        return something


class JsonItemFrame(tk.Frame):
    def __init__(self, root, value):
        tk.Frame.__init__(self, root)
        self.myValue = False
        if type(value) is int:
            self.myValue = tk.IntVar()
            self.myValue.set(value)
            frame = tk.Entry(self, textvariable=self.myValue,
                             width=7, justify="right", bg="#404040", fg="#80FF80")
        elif type(value) is float:
            self.myValue = tk.DoubleVar()
            self.myValue.set(value)
            frame = tk.Entry(self, textvariable=self.myValue,
                             width=7, justify="right", bg="#404040", fg="#60FF60")
        elif type(value) is str:
            self.myValue = tk.StringVar()
            self.myValue.set(value)
            frame = tk.Frame(self, root)
            label = tk.Label(frame, text="\"", bg="#303030", fg="#FF8080")
            label.pack(side=LEFT)
            entry = tk.Entry(frame, textvariable=self.myValue,
                             bg="#404040", fg="#FF8080")
            entry.pack(side=LEFT)
            label = tk.Label(frame, text="\"", bg="#303030", fg="#FF8080")
            label.pack(side=LEFT)
        elif type(value) is dict:
            frame = JsonFrame(self, value)
            self.myValue = frame
        elif type(value) is list:
            frame = JsonArrayFrame(self, value)
            self.myValue = frame
        else:
            frame = tk.Label(self, text="null", bg="#303030", fg="#4444FF")
            self.myValue = "null" 
        frame.pack(side=LEFT)

    def getDump(self):
        result = "ERROR"
        if type(self.myValue) is tk.StringVar:
            result = f"\"{self.myValue.get()}\""
        elif type(self.myValue) is tk.IntVar \
                or type(self.myValue) is tk.DoubleVar:
            try:
                result = str(self.myValue.get())
            except:
                result = "null"
        elif type(self.myValue) is JsonFrame \
                or type(self.myValue) is JsonArrayFrame:
            result = self.myValue.getDump()
        elif type(self.myValue) is str:
            result = self.myValue
        return result


class JsonArrayFrame(tk.Frame):
    def __init__(self, root, json_data):
        tk.Frame.__init__(self, root)
        self.mychildren = list()
        self.toggle = False
        start = tk.Label(self, text="[", bg="#303030", fg="#FFFFFF")
        start.pack(side=LEFT, anchor="nw")
        button = tk.Button(self, text="t", command=self.button_toggle_click)
        button.pack(side=LEFT)

        isFirst = True
        for value in json_data:
            # if isFirst:
            #     isFirst = False
            # else:
            #     label = tk.Label(self, text=",", bg="#303030", fg="#FFFFFF")
            #     label.pack(side=LEFT)
            frame = JsonItemFrame(self, value)
            self.mychildren.append(frame)
            frame.pack(side=LEFT)
            # if toogle:
            #     frame.pack(side=LEFT)
            # else:
            #     frame.pack(side=TOP)

        endlabel = tk.Label(self, text="]", bg="#303030", fg="#FFFFFF")
        endlabel.pack(side=RIGHT)

        button = tk.Button(self, text="+", command=self.button_add_click)
        button.pack(side=RIGHT)

    def button_add_click(self):
        # label = tk.Label(self, text=",", bg="#303030", fg="#FFFFFF")
        # label.pack(side=(TOP if self.toggle else LEFT))
        frame = JsonItemFrame(self, 0)
        self.mychildren.append(frame)
        frame.pack(side=(TOP if self.toggle else LEFT))
        print("button presses")
        print(self.getDump())
    
    def button_toggle_click(self):
        self.toggle = not self.toggle
        for child in self.mychildren:
            child.pack(side=(TOP if self.toggle else LEFT))
        

    def getDump(self):
        parts = list()
        for child in self.mychildren:
            parts.append(child.getDump())
        something = "[" + str.join(",", parts) + "]"
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
