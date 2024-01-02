sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
plt.imshow(sobelx, cmap="gray")
plt.title("sobel x"), plt.xticks([]), plt.yticks([])
plt.show()