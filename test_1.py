import tkinter as tk
from tkinter import *
from tkinter import ttk

app = Tk()

MENU_HEIGHT=525
MENU_WIDTH=200
TAB_HEIGHT=500
TAB_WIDTH=600

app.title("Clandestine")

canvas = ttk.Notebook(app)
canvas.pack(expand=1, fill='both')

#Side menu bar..........................................................................................................

menu_bar = ttk.Notebook(app, height=MENU_HEIGHT, width=MENU_WIDTH)
menu_bar.pack(side='left')

#Tab side..........................................................................................................

market_side = ttk.Notebook(app, height=TAB_HEIGHT, width=TAB_WIDTH)
market_side.pack(side='right')

tab1 = ttk.Frame(market_side)
tab2 = ttk.Frame(market_side)

market_side.add(tab1, text='market')
market_side.add(tab2, text='add a market')

#Tab 1..........................................................................................................

lbl1 = Label(tab1, text='search for items')

product_variable = StringVar()
#searchbox
product_search = Entry(tab1, textvariable=product_variable)
product_search.grid(column=1, row=0)
lbl1.grid(column=0, row=0)
# listbox
product_list = Listbox(tab1, height=20, width=50, border=0)
product_list.grid(row=3, column=0, rowspan=8, columnspan=4, pady=15, padx=15)
# scrollbar
scrollbar = Scrollbar(tab1)
scrollbar.grid(row=3, column=4)

#Tab 2..........................................................................................................

lbl2 = Label(tab2, text='search for markets to add')

market_variable = StringVar()
# searchbox
market_search = Entry(tab2, textvariable=market_variable)
market_search.grid(column=1, row=0)
lbl2.grid(column=0, row=0)
# listbox
market_list = Listbox(tab2, height=20, width=50, border=0)
market_list.grid(row=3, column=0, rowspan=8, columnspan=4, pady=15, padx=15)
# scrollbar
scrollbar = Scrollbar(tab2)
scrollbar.grid(row=3, column=4)

app.mainloop()