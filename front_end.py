import tkinter as tk
from tkinter import ttk

import helper_functions


def makeform(root, fields):
    entries = {}
    for field in fields:

        row = tk.Frame(root)
        lab = tk.Label(row, width=20, text= ": " + field, anchor='e')
        ent = tk.Entry(row)
        ent2 = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)

        lab.pack(side=tk.RIGHT)

        ent.pack(side=tk.LEFT,
                 expand=tk.YES,
                 fill=tk.X,
                 )
        """
        ent2.pack(side=tk.LEFT,
                 expand=tk.YES,
                 fill=tk.X,
                 )
        """
        entries[field] = ent
    return entries

def ui_simualte(e):

    helper_functions.gammaBar = float(e['gammaBar'].get())
    helper_functions.alpha = float(e['alpha'].get())
    helper_functions.beta = float(e['beta'].get())


    simulate()


#print('front_end')
from simulate import *
fields = ('gammaBar', 'alpha', 'beta')
root = tk.Tk()
root.title("ماژول پول و بانک")

tabControl = ttk.Notebook(root)

tab2 = tk.Frame(tabControl, width=400, height=400)
tabControl.add(tab2, text='ماژول جمعیت')
tabControl.pack(expand=1, fill='both')

ents = makeform(tab2, fields)


b1 = tk.Button(tab2, text='شبیه سازی',
           command=(lambda e=ents: ui_simualte(e)))

b1.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()