import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("./ASSAY.CSV", sep=',')
plt.clf()
print(data)
ni=data[['Ni','Fe']]
# mengatur ukuran gambar/plot
plt.rcParams['figure.dpi'] = 100

plt.matshow(ni.corr())
plt.title('Plot correlation matriks dengan .matshow', size=14)
plt.tight_layout()
plt.show()