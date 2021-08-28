import pandas as pd
from tkinter import *
from tkinter import ttk
from tid import datoforskjell
import os
import requests
import pathlib

path= pathlib.Path(__file__).parent / 'Timeplan.csv'

if datoforskjell():
    os.remove(path)
    url = 'https://cloud.timeedit.net/uis/web/student_u/ri10Qv5h6562ZnQY7QQ03cnXZk0Z55y7b4b505Yy768YsQdgcln7ZyQX.csv'
    r = requests.get(url, allow_redirects=True)
    with open(path, 'wb') as f:
        f.write(r.content)
root=Tk()
root.title("Kalendar")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

data = pd.read_csv(path, skiprows=3,parse_dates=True)
columns=['Startdato', 'Starttidspunkt','Rom', 'Emnekode,Emnenavn']
startdat=(data[['Startdato', 'Starttidspunkt','Rom', 'Emnekode,Emnenavn']])
print(startdat)
rows=len(startdat.axes[0])
columns = len(startdat.axes[1])
for column in range(columns):
    for row in range(rows):
        label = ttk.Label(mainframe, text=startdat.iloc[row, column], justify=LEFT).grid(column=column+1, row=row+1, sticky=W, padx=10)


def stop(event):
    root.destroy()
mainframe.bind('<Button-1>', stop)


#startdat.style.set_properties(**{'text-align': 'left'})
root.mainloop()