import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("photo.png")
img1= cv2.imread('ok.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
i = 0
circle=0
triangle=0
rect=0
square=0
for contour in contours:
    # findcontour function detects whole image as shape
    if i == 0:
        i = 1
        continue
  
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.0378 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
    cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
  
    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
  
    # putting shape name at center of each shape
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        triangle+=1
  
    elif len(approx) == 4:
        cv2.putText(img, 'Square', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        square+=1
  
    elif len(approx) == 6:
        cv2.putText(img, 'Rectangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        rect+=1
  
    else:
        cv2.putText(img, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
        circle+=1
  
# displaying the image after drawing contours

cv2.putText(img1, str(circle) ,(20,35), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
cv2.putText(img1, str(triangle) ,(20,90), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
cv2.putText(img1, str(rect) ,(20,170), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
cv2.putText(img1, str(square) ,(20,255), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
cv2.imshow('img', img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()