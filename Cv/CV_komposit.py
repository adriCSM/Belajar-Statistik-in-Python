import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import matplotlib.patches as patches
# import statsmodels.api as sm

lim_p1=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="LIM P1",engine="calamine")
lim_p2=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="LIM P2",engine="calamine")
lim_p3=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="LIM P3",engine="calamine")
lim_p4=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="LIM P4",engine="calamine")
lim_p5=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="LIM P5",engine="calamine")
sap_p1=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="SAP P1",engine="calamine")
sap_p2=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="SAP P2",engine="calamine")
sap_p3=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="SAP P3",engine="calamine")
sap_p4=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="SAP P4",engine="calamine")
sap_p5=pd.read_excel('./CV_KOMPOSIT.XLSX',sheet_name="SAP P5",engine="calamine")

def scatterplot(x,y,power,filename,dpi,layer,color='darkorange'):
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
  plt.title(f'Komposit Ni x Estimasi IDW Zona {layer}',fontsize=12,fontfamily='Times New Roman')
  plt.text(0.5, 1.05, 'SCATTERPLOT',fontsize=20,fontfamily='Times New Roman',fontweight="bold", ha='center', transform=plt.gca().transAxes)

  plt.text(0.02, y.max()+0.05, f'$y={round(intercept,2)}+{round(slope,2)}x$'+'\n'+f'$R^2={round(korelasi,6)}$',family='Times New Roman', size=8, ha='left',va='top',bbox=dict(facecolor='white', edgecolor='black'))

  plt.xlim(left=0)
  plt.xlabel('Komposit Ni',fontsize=14,fontfamily='Times New Roman')
  plt.xticks(np.arange(0, x.max()+0.1, step=0.1),fontsize=10,fontfamily='Times New Roman')
  plt.ylabel(f'Estimasi IDW Power {power}',fontsize=14,fontfamily='Times New Roman')
  plt.yticks(np.arange(0, y.max()+0.1, step=0.1),fontsize=10,fontfamily='Times New Roman')
  plt.legend(loc='upper right', bbox_to_anchor=(1, 1.06), ncol=1)
  plt.tight_layout()
  plt.savefig(f'./{filename}.png',dpi=dpi )
  plt.show()

# ======lim
x_lim_p1=lim_p1["Ni"]
y_lim_p1=lim_p1["ESTIMATE"]
x_lim_p2=lim_p2["Ni"]
y_lim_p2=lim_p2["ESTIMATE"]
x_lim_p3=lim_p3["Ni"]
y_lim_p3=lim_p3["ESTIMATE"]
x_lim_p4=lim_p4["Ni"]
y_lim_p4=lim_p4["ESTIMATE"]
x_lim_p5=lim_p5["Ni"]
y_lim_p5=lim_p5["ESTIMATE"]

scatterplot(x_lim_p1,y_lim_p1,1,'lim_p1',600,layer='Limonit')
scatterplot(x_lim_p2,y_lim_p2,2,'lim_p2',600 ,layer='Limonit')
scatterplot(x_lim_p3,y_lim_p3,3,'lim_p3',600 ,layer='Limonit')
scatterplot(x_lim_p4,y_lim_p4,4,'lim_p4',600 ,layer='Limonit')
scatterplot(x_lim_p5,y_lim_p5,5,'lim_p5',600 ,layer='Limonit')

# =====sap
x_sap_p1=sap_p1["Ni"]
y_sap_p1=sap_p1["ESTIMATE"]
x_sap_p2=sap_p2["Ni"]
y_sap_p2=sap_p2["ESTIMATE"]
x_sap_p3=sap_p3["Ni"]
y_sap_p3=sap_p3["ESTIMATE"]
x_sap_p4=sap_p4["Ni"]
y_sap_p4=sap_p4["ESTIMATE"]
x_sap_p5=sap_p5["Ni"]
y_sap_p5=sap_p5["ESTIMATE"]

# scatterplot(x_sap_p1,y_sap_p1,1,'sap_p1',600,color='lime',layer='Saprolit')
# scatterplot(x_sap_p2,y_sap_p2,2,'sap_p2',600,color='lime',layer='Saprolit')
# scatterplot(x_sap_p3,y_sap_p3,3,'sap_p3',600,color='lime',layer='Saprolit')
# scatterplot(x_sap_p4,y_sap_p4,4,'sap_p4',600,color='lime',layer='Saprolit')
# scatterplot(x_sap_p5,y_sap_p5,5,'sap_p5',600,color='lime',layer='Saprolit')