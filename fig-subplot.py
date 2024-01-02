from matplotlib import pyplot as plt
fig = plt.figure() # buat variabel kosong berupa fig
fig.add_subplot(131) # subplot untuk gambar output 1 (jumlah baris, kolom, urutan)
plt.imshow(b)# show image dengan variabel img
fig.add_subplot(132)#subplot untuk gambar output 2 (jumlah baris, kolom, urutan)
plt.imshow(g)
fig.add_subplot(133)##subplot untuk gambar output 3 (jumlah baris, kolom, urutan)
plt.imshow(r) # show image dari variabel img2
plt.show()# menampilkan plot