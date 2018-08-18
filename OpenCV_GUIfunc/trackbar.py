# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:47:53 2018

@author: 飯島直也
"""

import cv2
import numpy as np

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# parameter
radius = 1
color = (0, 0, 0)

def nothing(x):
    pass

def draw(event, x, y,flags,param):
    global radius, color
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),radius+1,color,-1)

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create trackbar for setting a radius
cv2.createTrackbar("radius", 'image',1,100,nothing)

cv2.setMouseCallback('image',draw)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    radius = cv2.getTrackbarPos("radius",'image')

    color = (b, g, r)

cv2.destroyAllWindows()