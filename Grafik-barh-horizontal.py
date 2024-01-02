import numpy as np
from matplotlib import pyplot as plt

penjualan = (40, 82, 13, 17, 28)
tahun = (2000, 2001, 2002, 2003, 2004)

plt.figure()
plt.barh(tahun, penjualan)
plt.title("Laporan Penjualan")
plt.xlabel("Tahun")
plt.ylabel("terjual (kg)")
plt.grid()
plt.show()