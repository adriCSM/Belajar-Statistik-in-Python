# from tkinter import ttk
# from tkinter import filedialog
from function import *
from customtkinter import *
from tkinter import *
from tab_xlsx import *

window=CTk()

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
# agar ukuran tidak dapat diubah
window.resizable(0,0)
window.title('AMine')
screenwidth=window.winfo_screenwidth()
screenheight=window.winfo_screenheight()
lebar=700
tinggi=570
x=int((screenwidth/2)-(lebar/2))
y=int((screenheight/2)-(tinggi/2))
window.geometry(f'{lebar}x{tinggi}+{x}+{y}')

# Title =========================
title=CTkLabel(window,text='SCATTERPLOT',font=('roboto',20),anchor='n')
title.pack(fill='x')

# Tab view
tab_view=CTkTabview(window,anchor='nw',corner_radius=20,height=50)
tab_view.pack(fill='x',expand=False,ipady=0,pady=0)

def cek(event):
  print(event)


tab_xlsx=tab_view.add('xlsx')
tab_csv=tab_view.add('csv')





# frame grafik dan export
grafik_export_frame(window)


# Tab xlsx
tab(tab_xlsx)
tab(tab_csv)

# # # Frame Input File =========================



window.mainloop()