from __future__ import print_function
from matplotlib import pyplot as plt
import pandas as pd
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])

# # Prints the number of rows and columns from the image, as well as the channels
# print(image.shape)

# cv2.imshow("Original",image)

# # Since we are resizing this, we will have to set a ratio, we do this by dividing our amount of pixels by the width
r = 1500/image.shape[1]
dim=(1500,int(image.shape[0]*r))
resized_area=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Original - Inter area",resized_area)

# resized_linear=cv2.resize(image,dim,interpolation=cv2.INTER_LINEAR)
# cv2.imshow("Inter linear",resized_linear)

# Splitting the image into 3 channels
channels= cv2.split(resized_area)
print(len(channels[0]))
print(len(channels[1]))
print(len(channels[2]))
plt.figure()

# # Removed the grayscale since I will only be plotting the colors in histogram
# image = cv2.cvtColor(resized_area,cv2.COLOR_BGR2GRAY)
# hist = cv2.calcHist([image],[0],None,[256],[0,256])

colors = ("b","g","r")
for (channel,color) in zip(channels,colors):
    hist = cv2.calcHist([channel],[0],None,[256],[0,256])
    plt.plot(hist,color=color)
    plt.xlim([0,256])
plt.show()

blue = pd.DataFrame(data=channels[0])
green = pd.DataFrame(data=channels[1])
red = pd.DataFrame(data=channels[2])

print(blue)
cv2.waitKey(0)