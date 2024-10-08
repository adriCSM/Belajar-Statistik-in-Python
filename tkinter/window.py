from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from method import *

window=Tk()
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
# pack(side=,expand=,fill=,padx=,ipadx=)

frame=Frame(window)
frame.pack(fill="both", expand=True)
frame.configure(background='#1a2124')

frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)



# Frame Title =========================
title=Label(frame,text='SCATTERPLOT',font=('roboto',20),background='#1a2124',foreground='white')
title.grid(row=0,column=0,sticky='ew',padx=5,pady=5,)

# Frame Input File =========================
input_frame=LabelFrame(frame,text='Input File',font=('sora',12),background='#1a2124',foreground='white')
input_frame.grid(row=1,column=0,padx=5,pady=5,sticky='ew')

input_frame.columnconfigure(0,weight=1)
input_frame.columnconfigure(1,weight=1)
input_frame.columnconfigure(2,weight=1)
input_frame.rowconfigure(0,weight=1)
input_frame.rowconfigure(1,weight=1)
input_frame.rowconfigure(2,weight=1)
input_frame.rowconfigure(3,weight=1)
input_frame.rowconfigure(4,weight=1)


input_file=Entry(input_frame,font=('sora',12))
input_file.grid(row=0,column=0,columnspan=2, sticky='ew')

btn_choose=Button(input_frame,text='Choose File',font=('sora',9), command=lambda:openfile(input_file,sheet_name))
btn_choose.grid(row=0,column=2,sticky='ew')

sheet_label=Label(input_frame,text='Sheet',font=('sora',12),bg='#1a2124',fg='white')
sheet_label.grid(row=2,column=0)

sheet_name=ttk.Combobox(input_frame,font=('sora',12))
sheet_name.grid(row=3,column=0,sticky='ew')
sheet_name.bind('<<ComboboxSelected>>',lambda event:change_value([sheet_name,x_variabel,y_variabel,input_file],event))

xvariable_label=Label(input_frame,text='Variabel X',font=('sora',12),bg='#1a2124',fg='white')
xvariable_label.grid(row=2,column=1,padx=5,sticky='ew')
x_variabel=ttk.Combobox(input_frame,font=('sora',12))
x_variabel.grid(row=3,column=1,sticky='ew')


yvariabel_label=Label(input_frame,text='Variabel Y',font=('sora',12),bg='#1a2124',fg='white')
yvariabel_label.grid(row=2,column=2)
y_variabel=ttk.Combobox(input_frame,font=('sora',12))
y_variabel.grid(row=3,column=2,sticky='ew')

label_title=Label(input_frame,text='Title Scatterplot',font=('sora',12),bg='#1a2124',fg='white')
label_title.grid(row=4,column=0,columnspan=3)
input_title=Text(input_frame,height=2, font=('sora',10))
input_title.grid(row=5,column=0,columnspan=3,rowspan=2,sticky='ew')

for widget in input_frame.winfo_children():
  widget.grid_configure(padx=5,pady=3)

# Frame Export Image======================================================
export_frame=LabelFrame(frame,text='Export File',font=('sora',12),background='#1a2124',foreground='white')
export_frame.grid(row=2,column=0,padx=5,pady=5, sticky='ew')

export_frame.columnconfigure(0,weight=1)
export_frame.columnconfigure(1,weight=1)
export_frame.columnconfigure(2,weight=1)
export_frame.rowconfigure(0,weight=1)
export_frame.rowconfigure(1,weight=1)
export_frame.rowconfigure(2,weight=1)
export_frame.rowconfigure(3,weight=1)

input_directory=Entry(export_frame,font=('sora',12))
input_directory.grid(row=0,columnspan=2 ,sticky='ew')
btn_directory=Button(export_frame,text='Location',font=('sora',9),command=lambda:choose_directory(input_directory))
btn_directory.grid(row=0,column=2,sticky='ew')

label_dpi=Label(export_frame,text='dpi',font=('sora',12),bg='#1a2124',fg='white')
label_dpi.grid(row=1,column=0)
input_dpi=ttk.Combobox(export_frame,font=('sora',12),values=['300','600'])
input_dpi.grid(row=2,column=0,rowspan=2,sticky='new')

label_filename=Label(export_frame,text='Filename',font=('sora',12),bg='#1a2124',fg='white')
label_filename.grid(row=1,columnspan=2,column=1)
input_filename=Entry(export_frame,font=('sora',12))
input_filename.grid(row=2,column=1,columnspan=2,sticky='news')
label_format=Label(export_frame,text='Format( .jpg, .jpeg, .png, .svg )',font=('sora',10),bg='#1a2124',fg='white')
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

button_run=Button(btn_frame,text='Export',font=('roboto',12),activebackground='deepskyblue',activeforeground='white',bg='skyblue',command=lambda:create_scatterplot(data_inputan),cursor='arrow')
button_run.grid(row=0,column=0,sticky='news',padx=5,pady=5)
# button_run.place(anchor=N)



window.mainloop()