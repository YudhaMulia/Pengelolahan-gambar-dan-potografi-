from matplotlib import pyplot as plt
fig = plt.figure() # buat variabel kosong berupa fig
fig.add_subplot(121) # subplot untuk gambar output 1 (jumlah baris, kolom, urutan)
plt.imshow(img)# show image dengan variabel img
fig.add_subplot(122)#subplot untuk gambar output 2 (jumlah baris, kolom, urutan)
img2= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#convert wara dari BRG to RGB
plt.imshow(img2) # show image dari variabel img2
plt.show()# menampilkan plot