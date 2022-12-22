from __future__ import print_function
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
# Prints the number of rows and columns from the image, as well as the channels
print(image.shape)
cv2.imshow("Original",image)
# Since we are resizing this, we will have to set a ratio, we do this by dividing our amount of pixels by the width
r = 1000/image.shape[1]
dim=(1000,int(image.shape[0]*r))
resized_area=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Inter area",resized_area)
resized_linear=cv2.resize(image,dim,interpolation=cv2.INTER_LINEAR)
cv2.imshow("Inter linear",resized_linear)
cv2.waitKey(0)