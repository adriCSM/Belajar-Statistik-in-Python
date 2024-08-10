from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from method import *

window=Tk()
# agar ukuran tidak dapat diubah
window.resizable(0,0)

window.title('AMine')
# screenwidth=window.winfo_screenwidth()
# screenheight=window.winfo_screenheight()
# lebar=450
# tinggi=300
# x=int((screenwidth/2)-(lebar/2))
# y=int((screenheight/2)-(tinggi/2))
# window.geometry(f'{lebar}x{tinggi}+{x}+{y}')



# pack(side=,expand=,fill=,padx=,ipadx=)

frame=Frame(window)
frame.pack()

# Frame Title 
title=Label(frame,text='SCATTERPLOT',font=('roboto',20),)
title.grid(row=0,column=0)

# Frame Input File
input_frame=LabelFrame(frame,text='Input File',font=('sora',10) )
input_frame.grid(row=1,column=0,padx=5,pady=5,sticky='ew')

input_file=Entry(input_frame)
input_file.grid(row=0,columnspan=2, sticky='ew')

btn_choose=Button(input_frame,text='Choose File', command=lambda:openfile(filedialog,input_file,sheet_name))
btn_choose.grid(row=0,column=2,sticky='ew')

sheet_label=Label(input_frame,text='Sheet Name')
sheet_label.grid(row=2,column=0)

sheet_name=ttk.Combobox(input_frame)
sheet_name.grid(row=3,column=0)
sheet_name.bind('<<ComboboxSelected>>',lambda event:change_value([sheet_name,x_variabel,y_variabel,input_file],event))

xvariable_label=Label(input_frame,text='Variabel X')
xvariable_label.grid(row=2,column=1)
x_variabel=ttk.Combobox(input_frame,width=16)
x_variabel.grid(row=3,column=1)


yvariabel_label=Label(input_frame,text='Variabel Y')
yvariabel_label.grid(row=2,column=2)
y_variabel=ttk.Combobox(input_frame,width=16)
y_variabel.grid(row=3,column=2)

label_title=Label(input_frame,text='Title Scatterplot')
label_title.grid(row=4,column=0,columnspan=3)
input_title=Text(input_frame,height=2, width=30,font=('sora',8))
input_title.grid(row=5,column=0,columnspan=3,rowspan=2,sticky='news')

for widget in input_frame.winfo_children():
  widget.grid_configure(padx=5,pady=2)

# Frame Export Image======================================================
export_frame=LabelFrame(frame,text='Export File',font=('sora',10))
export_frame.grid(row=2,column=0,padx=5,pady=5, sticky='ew')

input_directory=Entry(export_frame,width=50)
input_directory.grid(row=0,columnspan=2 , sticky='ew')
btn_directory=ttk.Button(export_frame,text='Location',command=lambda:choose_directory(filedialog,input_directory))
btn_directory.grid(row=0,column=2,sticky='ew')

label_dpi=Label(export_frame,text='dpi')
label_dpi.grid(row=1,column=0)
input_dpi=Entry(export_frame)
input_dpi.grid(row=2,column=0,rowspan=2,sticky='n')

label_filename=Label(export_frame,text='Filename')
label_filename.grid(row=1,columnspan=2,column=1)
input_filename=Entry(export_frame,width=40)
input_filename.grid(row=2,column=1,columnspan=2,sticky='ew')
label_filename=Label(export_frame,text='Format( .jpg, .jpeg, .png, .svg )',justify='left')
label_filename.grid(row=3,columnspan=2,column=1,sticky='ew')






for widget in export_frame.winfo_children():
  widget.grid_configure(padx=5,pady=2)




button_run=Button(frame,text='Export',activebackground='deepskyblue',activeforeground='white',bg='skyblue',command=lambda:run('ff'),cursor='arrow')
button_run.grid(row=3,column=0,sticky='news',padx=5,pady=5)
# button_run.place(anchor=N)



window.mainloop()