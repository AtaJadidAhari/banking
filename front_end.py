import tkinter as tk
from tkinter import ttk
from simulate import *
import helper_functions
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



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


    simulate(float(e['steps'].get()))


#print('front_end')

fields = ('gammaBar', 'alpha', 'beta', "steps")
root = tk.Tk()

root.geometry("500x500") #You want the size of the app to be 500x500


root.title("ماژول پول و بانک")

tabControl = ttk.Notebook(root)

tab2 = tk.Frame(tabControl)
tabControl.add(tab2, text='ماژول جمعیت')
tabControl.pack(expand=1, fill='both')

ents = makeform(tab2, fields)

T = tk.Text(tab2,  height=4, width=4)

T.insert(tk.END, "در این شبیه سازی، از اطلاعات 1200890 عامل استفاده شده است.\n همچنین تعداد 50000 خانوار اولیه در داده ها موجود بودند.")
T.pack(side=tk.BOTTOM, fill='x')
T.tag_configure("right", justify='right')
T.tag_add("right", 1.0, "end")

b1 = tk.Button(tab2, text='شبیه سازی',
           command=(lambda e=ents: ui_simualte(e)))

b1.pack(side=tk.BOTTOM, padx=1, pady=1)





############################
tab3 = tk.Frame(tabControl)
tabControl.add(tab3, text='نتایج')
tabControl.pack(expand=1, fill='both')




data1 = {'baze': ['[0,10]','[10,20]','[20,30]','[30,40]','[40,50]'],
         'Ages': [45000,42000,52000,49000,47000]
        }
df1 = DataFrame(data1,columns=['baze','Ages'])


data2 = {'Year': [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029],
         'Population': [50000,52090,53900,54500,54900,55000,54800,54600,54500,54400]
        }
df2 = DataFrame(data2,columns=['Year','Population'])


data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
        }
df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])








figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, tab3)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['baze','Ages']].groupby('baze').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Age Distribution')

figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, tab3)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year','Population']].groupby('Year').sum()
df2.plot(kind='line', ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Population')



"""
figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, tab3)
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price'])
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')

"""


root.mainloop()


