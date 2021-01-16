import numpy as np
from PIL import Image

np.set_printoptions(threshold=np.inf)

img1 = Image.open("Images\img011-00001.png")
print("First Image -PNG image")
img_arr1 = np.array(img1)
print(img_arr1)

img2 = Image.open("Images\bmp_A1.bmp")
print("\nSecond Image - BMP image")
img_arr2 = np.array(img2)
print(img_arr2)

img3 = Image.open("Images\seg_A1.bmp")
print("\nThird Image - Segmented Image")
img_arr3 = np.array(img3)
print(img_arr3)

img4 = Image.open("Images\grad_A1.bmp")
print("\nFourth Image - Sobel + Erode + Dilation + Gradiant")
img_arr4 = np.array(img4)
print(img_arr4)

f = open("demofile2.txt", "a")
f.write(str(img_arr1))
f.close()