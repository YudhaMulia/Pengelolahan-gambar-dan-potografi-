import matplotlib.pyplot as plt
import cv2
img = cv2.imread("fuji.jpg")
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r = RGB_img[:,:,0]
g = RGB_img[:,:,1]
b = RGB_img[:,:,2]

red = RGB_img.copy() # red channel [0]
red[:,:,1]=0
red[:,:,2]=0
print('Red Shape = ',red.shape)

green = RGB_img.copy() # green channel [0]
green[:,:,0]=0
green[:,:,2]=0
print('Green Shape = ',green.shape)

blue = RGB_img.copy() # blue channel [0]
blue[:,:,0]=0
blue[:,:,1]=0
print('Blue Shape = ',blue.shape)

fig, axes = plt.subplots(2, 2, figsize=(6, 6))
ax = axes.ravel()
ax[0].imshow(RGB_img)
ax[0].set_title("Original")
ax[1].imshow(red)
ax[1].set_title("Red Channel")
ax[2].imshow(green)
ax[2].set_title("Green Channel")
ax[3].imshow(blue)
ax[3].set_title("Blue Channel")
fig.tight_layout()
plt.show()