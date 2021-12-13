import tkinter as tk
import xmlrpc.client
import json
import time
import base64

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

app = Tk()
api = xmlrpc.client.ServerProxy(
"http://test_daemon:qazsedcft123@localhost:8442/")

app.title("Clandestine")
#
# MENU_HEIGHT=525
# MENU_WIDTH=200
# TAB_HEIGHT=500
# TAB_WIDTH=600

listAddress = api.listAddresses2()
AddressBook = api.listAddressBookEntries()
inboxMessages = api.getAllInboxMessages()

jsonAddresses = json.dumps(listAddress)
getInboxMessages = json.dumps(inboxMessages)

# Button functions........................................................


def join_market():
selected_name = name_variable.get()
name = bytes(selected_name, encoding='utf-8')
passphrase = base64.b64encode(name).decode('utf-8')
BMaddress = address_variable.get()
addChan = api.joinChan(passphrase, BMaddress)
messagebox.showinfo('The Market is ready to browse', (addChan))

# This function will be used to load the default market


def show_market():
# if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
#    messagebox.showerror('Required Fields', api.getDeterministicAddress('asdfasdfqwser'.encode(),4,1))
#    return
# db.insert()
"""
market_listbox.delete(0, END)
market_listbox.insert(END, inboxMessages)
"""


def view_products():
# This function will be used to read all messages in a
# chan and display the ones that match the keyword that's given
all_listings = api.getInboxMessageById()
product_listbox.insert(END, (all_listings))


def shutdown_bitmessage():
shutdown = api.shutdown()
messagebox.showerror('Required Fields', (shutdown))


canvas = ttk.Notebook(app)
canvas.pack(expand=1, fill='both')

# Side menu bar...........................................................

menu_bar = ttk.Notebook(app)
menu_bar.pack(side='left')

# This button will be used to load the default market's listing
default_market = Button(
menu_bar, text='Load Your Clandestine Market', command=show_market)
default_market.grid(column=1, row=2, padx=20)

# Hit this button if you dont want bitmessage to run in the background.
shutdown_button = Button(
menu_bar, text='Shutdown Bitmessage', command=shutdown_bitmessage)
shutdown_button.grid(column=1, row=4, padx=20)

# Tab selection...........................................................

market_side = ttk.Notebook(app)
market_side.pack(side='right')

tab1 = ttk.Frame(market_side)
tab2 = ttk.Frame(market_side)

market_side.add(tab1, text='shop')
market_side.add(tab2, text='your markets')

# Tab 1...................................................................

lbl1 = Label(tab1, text='search for products')

product_variable = StringVar()
# searchbox
product_search = Entry(tab1, textvariable=product_variable)
product_search.grid(column=1, row=0)
lbl1.grid(row=0, column=0)
# search for a product🔍
product_search_btn = Button(tab1, text='search', command=view_products)
product_search_btn.grid(row=0, column=2)
# listbox
product_listbox = Listbox(tab1, height=20, width=50, border=0)
product_listbox.grid(row=3, column=0, rowspan=8,
columnspan=4, pady=15, padx=15)
# scrollbar
scrollbar = Scrollbar(tab1)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
product_listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=product_listbox.yview)
#

# Tab 2...................................................................
# Search for markets by keyword in the searchbox
lbl2 = Label(tab2, text='search for a new market')
lbl2.grid(row=0, column=0)
# searchbox
address_variable = StringVar()
market_searchbox = Entry(tab2, textvariable=address_variable)
market_searchbox.grid(row=0, column=1)
# Enter the name/label of the market
lbl2 = Label(tab2, text='enter the market\'s name')
lbl2.grid(row=1, column=0)
# market name
name_variable = StringVar()
name_searchbox = Entry(tab2, textvariable=name_variable)
name_searchbox.grid(row=1, column=1)
# join a new market
join_btn = Button(tab2, text='join', command=join_market)
join_btn.grid(row=0, column=2)
# listbox
market_listbox = Listbox(tab2, height=20, width=50, border=0)
market_listbox.grid(row=3, column=0, rowspan=8, columnspan=4, pady=15, padx=15)
# scrollbar
scrollbar = Scrollbar(tab2)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
market_listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=market_listbox.yview)
# add market button
view_market_button = Button(tab2, text='View Market', command=join_market)
view_market_button.grid(row=10, column=4)

app.mainloop()
