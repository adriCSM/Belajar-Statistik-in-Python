import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from matplotlib.ticker import AutoMinorLocator,MaxNLocator
import pandas as pd
from tkinter import filedialog
from tkinter import *
from customtkinter import *

import matplotlib as mpl

def custom_sort_key(item):
  if item[0].isalpha():
    return (0,item)
  else:
    return (1,item)
  
# set grid row column
def configur_grid(frame,row,column):
  for i in range(0,row):
    frame.rowconfigure(i,weight=1)
  for i in range(0,column):
    frame.columnconfigure(i,weight=1)

  
def change_value(att,sheet):
  directory=att[2].get()
  file=read_file(directory,sheet)
  if file is not None:
    att[0].configure(values=file.columns.tolist())
    att[1].configure(values=file.columns.tolist())

  
def openfile(entry,sheet):
  file_types = [
        ("Excel Files", "*.xlsx;*.xls;*.csv"),
        # ("Text Files", "*.txt"),
        # ("PDF Files", "*.pdf"),
        # ("All Files", "*.*")
    ]
    
  directory=filedialog.askopenfilename(
    filetypes=file_types,
        title="Pilih file"
  )
  if directory != '':
    if entry.get() != '':
      entry.delete(0,1000)
      entry.insert(0,directory)
    else:
      entry.insert(0,directory)

    file=read_file(directory)
    print(file)
    # sheet_file=file.sheet_names
    # sheet.configure(values=sheet_file)
  
def read_file(directory):
  split=directory.split('.')
  if split[1].lower()=='xlsx' or split[1].lower()=='xls':
    file=pd.read_excel(directory,engine="openpyxl")
    return file
  elif split[1]=='csv':
    data=pd.read_csv(directory)
    return data

  
def read_file_sheet(directory,sheet):
  split=directory.split('.')
  if split[1].lower()=='xlsx' or split[1].lower()=='xls':
    file=pd.read_excel(directory,sheet_name=sheet,engine="calamine")
    return file
  elif split[1]=='csv':
    print(split[1])
    data=pd.read_csv(directory,sheet_name=sheet,engine="openpyxl")
    return data
  else:
    print('Aplikasi ini hanya dapat membaca format file .xlsx dan .csv')


def get_attribut_excel(input,event):
  sheet=input[0].get()
  x=input[1].config(value=['Ni','Fe'])
  y=input[2].config(value=['Ni','Fe'])
  directory=input[3].get()

  data=read_file_sheet(directory,sheet)
  if data:
    print('berhasil')
  else:
    print('gagal')


def choose_directory(entry):
  file_types=[
    ("Image Files", "*.png;*.jpg;*.jpeg;*.svg"),
  ]
  directory = filedialog.asksaveasfilename(
        filetypes=file_types,
        defaultextension=".jpg",  # Ekstensi default jika tidak ditentukan
        title="Simpan file sebagai"
    )
  if entry.get():
    entry.delete(0,1000)
    entry.insert(0,directory)
  else:
    entry.insert(0,directory)
  return True

def create_scatterplot(data):
  
  directory=data['directory'].get()
  sheet=data['sheet'].get()
  x_var=data['x_var'].get()
  y_var=data['y_var'].get()
  title=data['title'].get('1.0',END).strip() #.strip() untuk menghapus spasi di awal dan akhir teks yang diambil dari widget teks.
  location=data['location'].get()
  dpi=data['dpi'].get()
  font_style=data['font'].get()
  color_scatter=data['color'].get()
  title_x=data['title_x'].get('1.0',END).strip()
  title_y=data['title_y'].get('1.0',END).strip()
  
  if directory and  sheet  and  x_var  and  y_var  and  title  and  location and  dpi and color_scatter:
    data=read_file_sheet(directory,sheet)

    if not title_x:
        title_x=x_var
    if not title_y:
        title_y=y_var
    if not font_style:
      font_style='Times New Roman'
      mpl.rcParams['font.family'] = font_style
    if color_scatter=='Orange':
      color_scatter="darkorange"
    if color_scatter=='Green':
      color_scatter="lime"

    x=data[x_var]
    y=data[y_var] 
    # model_regresi
    line_regresi=stats.linregress(x,y)
    seris=pd.Series(line_regresi)
    regresi=seris.astype(dtype='float64')
    slope=regresi[0]
    intercept=regresi[1]
    korelasi=regresi[2]
    fit_line=slope*x+intercept
    
    # Creat Grafik
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.scatter(x,y,s=30,color=color_scatter,label=f'{x.name} vs. {y.name}',zorder=4)
    ax.plot(x,fit_line,color="black",zorder=4)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator(n=3))
    ax.tick_params(axis='both',which='minor', length=1.5, color='grey')
    ax.tick_params(axis='both',which='major', length=3, color='grey')
    ax.spines[['bottom','left']].set_edgecolor('grey')
    ax.spines[['top','right']].set_edgecolor('#DFE7DE')
    plt.grid(visible=True,color='#DFE7DE')
    plt.title(title.title(),fontsize=12)

    xlim = plt.gca().get_xlim()
    ylim = plt.gca().get_ylim()
    
    step_x=round((xlim[1]-xlim[0])/15,1)
    step_y=round((ylim[1]-ylim[0])/15,1)
    
    x_5persen=round((xlim[1]-xlim[0])*0.05,4)
    y_5persen=round((ylim[1]-ylim[0])*0.05,4)

    if xlim[0] >= 0 and xlim[1] <100:
      plt.xlim(0)
      
      xmin=list(xlim)
      xmin[0]=0
      xlim=tuple(xmin)
    if ylim[0] >= 0 and ylim[1] <100:
      plt.ylim(0)

      ymin=list(ylim)
      ymin[0]=0
      ylim=tuple(ymin)

    # Setting Interval Tick
    plt.xticks(np.arange(round(xlim[0],1), round(xlim[1]+x_5persen,1), step=step_x),fontsize=10,)
    plt.yticks(np.arange(round(ylim[0],1), round(ylim[1]+(y_5persen*3),1), step=step_y),fontsize=10,)

    new_ylim=plt.gca().get_ylim()
    new_xlim=plt.gca().get_xlim()
    y_2persen=round((new_ylim[1]-new_ylim[0])*0.02,4)
    x_1persen=round((new_xlim[1]-new_xlim[0])*0.01,4)

    # Teks Position
    plt.text(0.5, 1.09, 'SCATTERPLOT',fontsize=20,fontweight="bold", ha='center', transform=plt.gca().transAxes)
    plt.text(round(new_xlim[0]+x_1persen,4), round(new_ylim[1]-y_2persen,4), f'$y={round(intercept,2)}+{round(slope,2)}x$'+'\n'+f'$R^2={round(korelasi,6)}$',family=font_style, size=8, ha='left',va='top',bbox=dict(facecolor='white', edgecolor='black'))

    #  =================================
    plt.xlabel(title_x.title(),fontsize=14,)
    plt.ylabel(title_y.title(),fontsize=14,)
    
    
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.06), ncol=1)
    plt.tight_layout()
    plt.savefig(location,dpi=int(dpi) )

    # Atur ukuran tulisan tick label
    plt.tick_params(axis='x', labelsize=9)  # Ukuran tulisan untuk sumbu X
    plt.tick_params(axis='y', labelsize=9)  # Ukuran tulisan untuk sumbu Y

    # plt.show()
    # open Image setelah di save
    os.startfile(location)
        
     
  else:
    print('Terdapat field kosong')