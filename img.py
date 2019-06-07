#!/usr/bin/env python3

import cv2
import numpy as np

img = cv2.imread('/home/ganga/Pictures/pinku1.jpeg')
img1= cv2.imread('/home/ganga/Pictures/pinku2.jpeg')
cv2.imshow('original',img1)
cv2.imshow('original1',img)

#a,threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
#cv2.imshow('pops',threshold)

diff1 = cv2.absdiff(img1, img)
cv2.imshow('allthediff', diff1)

#rows,cols,channels = diff.shape
#roi = img1[0:rows, 0:cols ]
#cv2.imshow('roi',roi)
img2gray = cv2.cvtColor(diff1,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',img2gray)

ret, thresholded = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

cv2.imshow('poy',thresholded)

diff2= cv2.bitwise_and(img1, img1, mask=thresholded)
cv2.imshow('popppy',diff2)
#hsv = cv2.cvtColor(diff2, cv2.COLOR_BGR2HSV) #to convert to hsv
lower_red = np.array([0,70,20]) 
upper_red = np.array([40,255,135]) 
  
# Here we are defining range of white colour
# This creates a mask of white coloured  
# objects found in the frame. 
mask = cv2.inRange(diff2, lower_red, upper_red) 

#Extractng only the white part of the bg
white_part= cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('bg', white_part)

mask_inv=cv2.bitwise_not(mask)
therest=cv2.bitwise_and(img1, img1, mask=mask_inv)
#cv2.imshow('the rest',therest) 

dst = cv2.add(therest,white_part)
cv2.imshow('total',dst) 
  
# The bitwise and of the frame and mask is done so  
# that only the blue coloured objects are highlighted  
# and stored in res 
#res = cv2.bitwise_and(roi,roi, mask= mask) 


#cv2.imshow('mask',mask) 
#cv2.imshow('res',res) 


cv2.waitKey(0)
cv2.destroyAllWindows()
