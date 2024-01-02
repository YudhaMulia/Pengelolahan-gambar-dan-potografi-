import numpy as np
from matplotlib import pyplot as plt

# membuat diagram grafik garis menggunakan phyton

# Data for plotting
penjualan1 = (40, 82, 13, 17, 28)
tahun1 = (2000, 2001, 2002, 2003, 2004)

penjualan2 = (50, 66, 25, 45, 31)
tahun2 = (2010, 2011, 2012, 2013, 2014)

# untuk memberikan ukuran pada output dengan urutan panjang x lebar

plt.figure(figsize=(7, 5))
plt.subplot(2, 2, 1)
plt.plot(tahun1, penjualan1)
plt.title("Laporan Penjualan Getah Karet Semester 1")
plt.xlabel("Tahun")
plt.ylabel("terjual (kg)")
plt.grid()

plt.subplot(2, 2, 2)
plt.bar(tahun2, penjualan2)
plt.title("Laporan Penjualan Getah Karet Semester 2")
plt.xlabel("Tahun")
plt.ylabel("terjual (kg)")

plt.subplot(2, 2, 3)
plt.pie(tahun2, labels=penjualan2)

plt.subplot(2, 2, 4)
explode = (0.4, 0.2, 0.1, 0, 0)
plt.pie(tahun1, labels=penjualan1, explode = explode)
plt.tight_layout()
plt.show()
# bar
# plot
# barh
# pie
# figsize untuk width(panjang) diagram
# explode untuk pemberitahu atau pemisah grafik
# subplot untuk membagi dalam dua grid
