import tkinter as tk
import requests as req 
import sqlite3 as sql 

conn = sql.connect('db.sqlite3')
cursor = conn.cursor()

main = tk.Tk()
main.mainloop()