import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sudoku.jpg", 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

plt.imshow(laplacian, cmap="gray")
plt.title("Laplacian"), plt.xticks([]), plt.yticks([])
plt.show()
