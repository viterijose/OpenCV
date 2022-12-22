from __future__ import print_function
from matplotlib import pyplot as plt
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
# Prints the number of rows and columns from the image, as well as the channels
# print(image.shape)
# cv2.imshow("Original",image)
# Since we are resizing this, we will have to set a ratio, we do this by dividing our amount of pixels by the width
r = 1000/image.shape[1]
dim=(1000,int(image.shape[0]*r))
resized_area=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Inter area",resized_area)
# resized_linear=cv2.resize(image,dim,interpolation=cv2.INTER_LINEAR)
# cv2.imshow("Inter linear",resized_linear)
image = cv2.cvtColor(resized_area,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([image],[0],None,[256],[0,256])
plt.figure()
plt.title("Greyscale")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)