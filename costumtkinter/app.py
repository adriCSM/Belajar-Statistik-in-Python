# from tkinter import ttk
# from tkinter import filedialog
from function import *
from customtkinter import *
from tkinter import *

window=CTk()

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
# agar ukuran tidak dapat diubah
window.resizable(0,0)
window.title('AMine')
screenwidth=window.winfo_screenwidth()
screenheight=window.winfo_screenheight()
lebar=700
tinggi=500
x=int((screenwidth/2)-(lebar/2))
y=int((screenheight/2)-(tinggi/2))
window.geometry(f'{lebar}x{tinggi}+{x}+{y}')


window.columnconfigure(0,weight=1)
# window.pack(side=,expand=,fill=,padx=,ipadx=)



frame=CTkFrame(window)
frame.pack(fill="both", expand=True,padx=10,pady=10)


frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)



# Frame Title =========================
title=CTkLabel(frame,text='SCATTERPLOT',font=('roboto',20))
title.grid(row=0,column=0,sticky='ew',padx=5,pady=5,)

# # Frame Input File =========================

input_frame=LabelFrame(frame,text='Input File',font=('helvetica',10))
input_frame.grid(row=1,column=0,padx=5,pady=5,sticky='ew')

input_frame.columnconfigure(0,weight=1)
input_frame.columnconfigure(1,weight=1)
input_frame.columnconfigure(2,weight=1)
input_frame.rowconfigure(0,weight=1)
input_frame.rowconfigure(1,weight=1)
input_frame.rowconfigure(2,weight=1)
input_frame.rowconfigure(3,weight=1)
input_frame.rowconfigure(4,weight=1)


input_file=CTkEntry(input_frame,font=('helvetica',12),placeholder_text='Input your file')
input_file.grid(row=0,column=0,columnspan=2, sticky='ew')

btn_open_file=CTkButton(input_frame,text='Choose File',font=('helvetica',12), command=lambda:openfile(input_file,sheet_name))
btn_open_file.grid(row=0,column=2,sticky='ew')

sheet_label=CTkLabel(input_frame,text='Sheet',font=('helvetica',12),text_color='black')
sheet_label.grid(row=2,column=0)

sheet_name=CTkComboBox(input_frame,font=('helvetica',12),command=lambda event:change_value([x_variabel,y_variabel,input_file],event))
sheet_name.grid(row=3,column=0,sticky='ew')
# sheet_name.bind('<<ComboboxSelected>>',lambda event:change_value([sheet_name,x_variabel,y_variabel,input_file]))

xvariable_label=CTkLabel(input_frame,text='Variabel X',font=('helvetica',12),text_color='black')
xvariable_label.grid(row=2,column=1,padx=5,sticky='ew')
x_variabel=CTkComboBox(input_frame,font=('helvetica',12))
x_variabel.grid(row=3,column=1,sticky='ew')


yvariabel_label=CTkLabel(input_frame,text='Variabel Y',font=('helvetica',12),text_color='black')
yvariabel_label.grid(row=2,column=2)
y_variabel=CTkComboBox(input_frame,font=('helvetica',12))
y_variabel.grid(row=3,column=2,sticky='ew')

label_title=CTkLabel(input_frame,text='Title Scatterplot',font=('helvetica',12),text_color='black')
label_title.grid(row=4,column=0,columnspan=3)
input_title=CTkTextbox(input_frame,height=2, font=('helvetica',10))
input_title.grid(row=5,column=0,columnspan=3,rowspan=2,sticky='ew')

for widget in input_frame.winfo_children():
  widget.grid_configure(padx=5,pady=3)

# Frame Export Image======================================================
export_frame=LabelFrame(frame,text='Export File',font=('helvetica',10))
export_frame.grid(row=2,column=0,padx=5,pady=5, sticky='ew')

export_frame.columnconfigure(0,weight=1)
export_frame.columnconfigure(1,weight=1)
export_frame.columnconfigure(2,weight=1)
export_frame.rowconfigure(0,weight=1)
export_frame.rowconfigure(1,weight=1)
export_frame.rowconfigure(2,weight=1)
export_frame.rowconfigure(3,weight=1)

input_directory=CTkEntry(export_frame,font=('helvetica',12),placeholder_text='Choose your directory')
input_directory.grid(row=0,columnspan=2 ,sticky='ew')
btn_directory=CTkButton(export_frame,text='Folder',font=('helvetica',9),command=lambda:choose_directory(input_directory))
btn_directory.grid(row=0,column=2,sticky='ew')

label_dpi=CTkLabel(export_frame,text='dpi',font=('helvetica',12),text_color='black')
label_dpi.grid(row=1,column=0)
input_dpi=CTkComboBox(export_frame,font=('helvetica',12),values=['300','600'])
input_dpi.grid(row=2,column=0,rowspan=2,sticky='new')

label_filename=CTkLabel(export_frame,text='Filename',font=('helvetica',12),text_color='black')
label_filename.grid(row=1,columnspan=2,column=1)
input_filename=CTkEntry(export_frame,font=('helvetica',12))
input_filename.grid(row=2,column=1,columnspan=2,sticky='news')
label_format=CTkLabel(export_frame,text='Format( .jpg, .jpeg, .png, .svg )',font=('helvetica',10),text_color='black')
label_format.grid(row=3,columnspan=2,column=1,sticky='nw')




for widget in export_frame.winfo_children():
  widget.grid_configure(padx=5,pady=3)


data_inputan={
  'directory':input_file,
  'sheet':sheet_name,
  'x_var':x_variabel,
  'y_var':y_variabel,
  'title':input_title,
  'location':input_directory,
  'dpi':input_dpi,
  'filename':input_filename
}

# Frame button======================================================
btn_frame=LabelFrame(frame,background='#1a2124',border=False)
btn_frame.grid(row=3,column=0,padx=5 ,sticky='ew')

btn_frame.columnconfigure(0,weight=1)
btn_frame.rowconfigure(0,weight=1)


button_run=CTkButton(btn_frame,text='Export',font=('roboto',12),command=lambda:create_scatterplot(data_inputan),cursor='arrow')
button_run.grid(row=0,column=0,sticky='news',padx=5,pady=5)

# button_run.place(anchor=N)




window.mainloop()