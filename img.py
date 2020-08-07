#!/usr/bin/env python3

# this is a precursor to the popular program to make a video in which a blanket makes you invisibile
# here, you will make a a particular colour disappear if we obtain two images of a background and a person or any object in the sam ebackground
# we can, then make a certain colour in the new person or object disappear by replacing the portions with the colour with the background image.


import cv2   #importing opencv and numpy
import numpy as np

img = cv2.imread('/home/ganga/Pictures/pinku1.jpeg') #image with person
imgbg= cv2.imread('/home/ganga/Pictures/pinku2.jpeg')#background
cv2.imshow('original',img1)#display images
cv2.imshow('original1',img)

#a,threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
#cv2.imshow('pops',threshold)

diff1 = cv2.absdiff(img1, img) #extract the diff between the two images i.e, the person; dont mind the weird colours
#cv2.imshow('diff', diff1)

#rows,cols,channels = diff.shape #in case the 2 images are not of the same dimensions
#roi = img1[0:rows, 0:cols ]
#cv2.imshow('roi',roi)

img2gray = cv2.cvtColor(diff1,cv2.COLOR_BGR2GRAY) # converting the person to grayscale so we can easily threshold
#cv2.imshow('grayscale',img2gray)
ret, thresholded = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) #All the points with value greater 10 are converted to 255 and others to 0
                                                                       #So, the region with person is white, other areas are black
#cv2.imshow('white_person', thresholded)

diff2 = cv2.bitwise_and(img, img, mask=thresholded)  # extracting the person from img
#cv2.imshow('person', diff2)


# hsv = cv2.cvtColor(diff2, cv2.COLOR_BGR2HSV) #to convert to hsv
lower_red = np.array([200, 200, 200])
upper_red = np.array([255, 255, 255])  #Define the colour you want to make invisible, and find its range

mask = cv2.inRange(diff2, lower_red, upper_red) # Finding the region on the picture that u want to make invisible
#cv2.imshow('mask', mask)

# Extractng only the 'to be invisible' part from bg
white_part = cv2.bitwise_and(img1, img1, mask=mask)
#cv2.imshow('bg', white_part)

mask_inv = cv2.bitwise_not(mask)# inverting mask
therest = cv2.bitwise_and(img, img, mask=mask_inv)# getting all the parts except 'to be invisible' part
# cv2.imshow('the rest',therest)

dst = cv2.add(therest, white_part) #Adding both
cv2.imshow('total', dst)



cv2.waitKey(0)
cv2.destroyAllWindows()
