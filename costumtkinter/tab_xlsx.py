from function import *
from tkinter import *
from tkinter import ttk
from tkinter import font
from customtkinter import *

fnt=('helvetica',14)

def tab(name_tab):

  
  frame1=CTkFrame(name_tab)
  frame1.pack(fill='x')

  configur_grid(frame1,4,3)

  # R1=============
  label_1=CTkLabel(frame1,text='Input File',anchor='nw')
  label_1.grid(row=0,column=0,columnspan=3,sticky='ew')

  # R2=============
  input_file=CTkEntry(frame1,font=fnt,placeholder_text='Choose your file')
  input_file.grid(row=1,column=0,columnspan=2,sticky='ew')
  btn_open_file=CTkButton(frame1,text='Choose File',font=fnt, command=lambda:openfile(input_file,sheet_name))
  btn_open_file.grid(row=1,column=2,sticky='ew')

  # R3=============
  cek=name_tab.clipboard_get()

  if cek == 'tab_xlsx':
    sheet_label=CTkLabel(frame1,text='*Sheet',font=fnt,anchor='w')
    sheet_label.grid(row=2,column=0)
    sheet_name=CTkComboBox(frame1,font=fnt,command=lambda event:change_value([x_variabel,y_variabel,input_file],event),values=[''])
    sheet_name.grid(row=3,column=0,sticky='ew')
  else:
    sheet_label=CTkLabel(frame1,text='*delimited',font=fnt,anchor='w')
    sheet_label.grid(row=2,column=0)
    sheet_name=CTkComboBox(frame1,font=fnt,command=lambda event:change_value([x_variabel,y_variabel,input_file],event),values=[',','.',';',':','/','<','>'])
    sheet_name.grid(row=3,column=0,sticky='ew')


  xvariable_label=CTkLabel(frame1,text='*Variabel X',font=fnt,anchor='w')
  xvariable_label.grid(row=2,column=1,padx=5)
  yvariabel_label=CTkLabel(frame1,text='*Variabel Y',font=fnt,anchor='w')
  yvariabel_label.grid(row=2,column=2)

  # R4=============
  x_variabel=CTkComboBox(frame1,font=fnt,values=[''])
  x_variabel.grid(row=3,column=1,sticky='ew')
  y_variabel=CTkComboBox(frame1,font=fnt,values=[''])
  y_variabel.grid(row=3,column=2,sticky='ew')

  for widget in frame1.winfo_children():
    widget.grid_configure(padx=5,sticky='ew')
  
def grafik_export_frame(master):

  # grafik frame=============================================================================
  frame2=CTkFrame(master)
  frame2.pack(fill='x',padx=5,pady=5)

  configur_grid(frame2,5,3)

  # R1==============
  Label_2=CTkLabel(frame2,text='Grafik Scatterplot',font=fnt,anchor='w')
  Label_2.grid(row=0,column=0,columnspan=3,sticky='ew')

  # R2==============
  label_title=CTkLabel(frame2,text='*Title Scatterplot',font=fnt,anchor='w')
  label_title.grid(row=1,column=0)
  label_title_x=CTkLabel(frame2,text='Title x (Optional)',font=fnt,anchor='w')
  label_title_x.grid(row=1,column=1)
  label_title_y=CTkLabel(frame2,text='Title y (Optional)',font=fnt,anchor='w')
  label_title_y.grid(row=1,column=2)

  # R3==============
  input_title=CTkTextbox(frame2,height=2, font=fnt)
  input_title.grid(row=2,column=0,rowspan=2)
  input_title_x=CTkTextbox(frame2,height=2, font=fnt)
  input_title_x.grid(row=2,column=1,rowspan=2)
  input_title_y=CTkTextbox(frame2,height=2, font=fnt)
  input_title_y.grid(row=2,column=2,rowspan=2)

  # R4==============
  font_label=CTkLabel(frame2,text='Font',font=fnt,anchor='w')
  font_label.grid(row=4,column=0)
  color_label=CTkLabel(frame2,text='*Color',font=fnt,anchor='w')
  color_label.grid(row=4,column=1)

  # R5==============
  fonts=list(font.families())
  font_familiy=sorted(fonts,key=custom_sort_key)
  input_font=ttk.Combobox(frame2,values=font_familiy)
  input_font.grid(row=5,column=0)
  input_color=CTkComboBox(frame2,values=['Orange','Green'])
  input_color.grid(row=5,column=1)

  for widget in frame2.winfo_children():
    widget.grid_configure(padx=10,pady=0,sticky='ew')

# Frame Export Image======================================================
  frame3=CTkFrame(master)
  frame3.pack(fill='x',padx=5,pady=5)

  configur_grid(frame3,4,3)

  # R1==============
  label_3=CTkLabel(frame3,text='Export File',font=fnt,anchor='w')
  label_3.grid(row=0,column=0,sticky='ew')

  # R2==============
  input_directory=CTkEntry(frame3,font=fnt,placeholder_text='Choose your directory')
  input_directory.grid(row=1,column=0,columnspan=2)
  btn_directory=CTkButton(frame3,text='Folder',font=fnt,command=lambda :choose_directory(input_directory))
  btn_directory.grid(row=1,column=2)

  # R3==============
  label_dpi=CTkLabel(frame3,text='*dpi',font=fnt,anchor='w')
  label_dpi.grid(row=2,column=0)

  # R4==============
  input_dpi=CTkComboBox(frame3,font=fnt,values=['300','600'])
  input_dpi.grid(row=3,column=0)

  for widget in frame3.winfo_children():
    widget.grid_configure(padx=10,pady=0,sticky='ew')

  data_inputan={
    # 'directory':input_file,
    # 'sheet':sheet_name,
    # 'x_var':x_variabel,
    # 'y_var':y_variabel,
    'title':input_title,
    'location':input_directory,
    'dpi':input_dpi,
    'title_x':input_title_x,
    'title_y':input_title_y,
    'font':input_font,
    'color':input_color
  }

  # Frame button======================================================
  frame4=CTkFrame(master)
  frame4.pack(fill='x',expand=True,padx=5)

  button_run=CTkButton(frame4,text='Export',font=('roboto',12),command=lambda :create_scatterplot(data_inputan,),cursor='arrow')
  button_run.pack(fill='x',padx=10)
