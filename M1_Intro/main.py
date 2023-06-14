import cv2
import os
# fix bug cannot read cv2.imread : file integrity. Ganti dengan direktori folder ini
os.chdir(r"D:\Kerja\Timedoor\Bahan Ajar\Coding Camp 2023\Coding Files\M1_Intro")
img= cv2.imread("angie.jpg")
print(img.shape)
img = cv2.GaussianBlur(img, (1, 1), 0)
green = (0, 255, 0)
blue = (255, 0, 0)
red = (0, 0, 255)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), green, 3)
cv2.line(img, (0, 20), (img.shape[1], 20), red, 3)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()