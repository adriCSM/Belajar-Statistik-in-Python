import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from matplotlib.ticker import AutoMinorLocator
import pandas as pd
from tkinter import filedialog
from tkinter import *
from customtkinter import *

def run(teks,*args):
  print(teks)
  
def change_value(att,sheet):
  directory=att[2].get()
  file=read_file(directory,sheet)
  if file is not None:
    att[0].configure(values=file.columns.tolist())
    att[1].configure(values=file.columns.tolist())

  

def openfile(entry,sheet):
  directory=filedialog.askopenfilename()
  if directory != '':
    if entry.get() != '':
      entry.delete(0,1000)
      entry.insert(0,directory)
    else:
      entry.insert(0,directory)
    file=pd.ExcelFile(directory,engine="openpyxl")
    sheet_file=file.sheet_names
    sheet.configure(values=sheet_file)
  

def get_attribut_excel(input,event):
  sheet=input[0].get()
  x=input[1].config(value=['Ni','Fe'])
  y=input[2].config(value=['Ni','Fe'])
  directory=input[3].get()

  data=read_file(directory,sheet)
  if data:
    print('berhasil')
  else:
    print('gagal')

def read_file(directory,sheet):
  
  split=directory.split('.')
  if split[1].lower()=='xlsx' or split[1].lower()=='xls':
    file=pd.read_excel(directory,sheet_name=sheet,engine="calamine")
    return file
  elif split[1]=='csv':
    file=pd.read_csv(directory,sheet_name=sheet,engine="calamine")
    return file
  else:
    print('Aplikasi ini hanya dapat membaca format file .xlsx dan .csv')

def choose_directory(entry):
  directory=filedialog.askdirectory()
  if entry.get() != '':
    entry.delete(0,1000)
    entry.insert(0,directory)
  else:
    entry.insert(0,directory)
    

def create_scatterplot(data,color='darkorange'):
  directory=data['directory'].get()
  sheet=data['sheet'].get()
  x_var=data['x_var'].get()
  y_var=data['y_var'].get()
  title=data['title'].get('1.0',END)
  location=data['location'].get()
  dpi=data['dpi'].get()
  filename=data['filename'].get()

  if directory != '' and sheet != '' and x_var != '' and y_var != '' and title != '' and location!= '' and dpi != '' and filename:
    data=read_file(directory,sheet)
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
    ax.scatter(x,y,s=30,color=color,label=f'{x.name} vs. {y.name}',zorder=4)
    ax.plot(x,fit_line,color="black",zorder=4)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator(n=3))
    ax.tick_params(axis='both',which='minor', length=1.5, color='grey')
    ax.tick_params(axis='both',which='major', length=3, color='grey')
    ax.spines[['bottom','left']].set_edgecolor('grey')
    ax.spines[['top','right']].set_edgecolor('#DFE7DE')
    plt.grid(visible=True,color='#DFE7DE')
    plt.title(title.capitalize(),fontsize=12,fontfamily='Times New Roman')
    plt.text(0.5, 1.09, 'SCATTERPLOT',fontsize=20,fontfamily='Times New Roman',fontweight="bold", ha='center', transform=plt.gca().transAxes)
    plt.text(0.02, y.max()+0.05, f'$y={round(intercept,2)}+{round(slope,2)}x$'+'\n'+f'$R^2={round(korelasi,6)}$',family='Times New Roman', size=8, ha='left',va='top',bbox=dict(facecolor='white', edgecolor='black'))
    # =================================
    plt.xlim(left=0)
    plt.xlabel(x.name.capitalize(),fontsize=14,fontfamily='Times New Roman',)
    plt.ylabel(y.name.capitalize(),fontsize=14,fontfamily='Times New Roman')

    if x.max() <= 5:
      plt.xticks(np.arange(0, x.max()+0.1, step=0.1),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+0.1, step=0.1),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 10:
      plt.xticks(np.arange(0, x.max()+1, step=1),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+1, step=1),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 50:
      plt.xticks(np.arange(0, x.max()+5, step=5),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+5, step=5),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 100:
      plt.xticks(np.arange(0, x.max()+10, step=10),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+10, step=10),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 1000:
      plt.xticks(np.arange(0, x.max()+100, step=100),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+100, step=100),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 5000:
      plt.xticks(np.arange(0, x.max()+500, step=500),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+500, step=500),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 10000:
      plt.xticks(np.arange(0, x.max()+1000, step=1000),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+1000, step=1000),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 50000:
      plt.xticks(np.arange(0, x.max()+5000, step=5000),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+5000, step=5000),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 100000:
      plt.xticks(np.arange(0, x.max()+10000, step=10000),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+10000, step=10000),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 500000:
      plt.xticks(np.arange(0, x.max()+50000, step=50000),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+50000, step=50000),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 1000000:
      plt.xticks(np.arange(0, x.max()+100000, step=100000),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+100000, step=100000),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 5000000:
      plt.xticks(np.arange(0, x.max()+500000, step=500000),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+500000, step=500000),fontsize=10,fontfamily='Times New Roman')
    elif x.max() <= 10000000:
      plt.xticks(np.arange(0, x.max()+1000000, step=1000000),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+1000000, step=1000000),fontsize=10,fontfamily='Times New Roman')
    elif x.max() > 10000000:
      plt.xticks(np.arange(0, x.max()+5000000, step=5000000),fontsize=10,fontfamily='Times New Roman')
      plt.yticks(np.arange(0, y.max()+5000000, step=5000000),fontsize=10,fontfamily='Times New Roman')
    

    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.06), ncol=1)
    plt.tight_layout()
    plt.savefig(location+'/'+filename,dpi=int(dpi) )
    plt.show()
  else:
    print('Terdapat field kosong')