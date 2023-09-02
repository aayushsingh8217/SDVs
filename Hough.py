import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(3,3),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def roi(image):
    height=image.shape[0]
    polygons=np.array([[(324,height),(977,height),(563,289)]])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)
    masked_img=cv2.bitwise_and(image,mask)
    return masked_img


def displines(image,lines):
    line_img=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv2.line(line_img,(x1,y1),(x2,y2),(255,0,0),10)
            #color of lines COLOR_RGB2GRAY
    return line_img



image=cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny=canny(lane_image)
cropped_image=roi(canny)
#hough tarns
lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
#lines 2D array
line_image=displines(lane_image,lines)

combo_img=cv2.addWeighted(lane_image,0.8,line_image,1,1)

cv2.imshow('results',combo_img)
cv2.waitKey(0)
#all pixel multiplied by 0.8
#20% more weight
#cam value substaintial value

#2ns and 3rd parameter for hough lines will be deciding
#factor larger bins less precision
#2 pixel with single degree precision
#4th paramter is finding the best fit threshold
#best threshold and rho
#np array just an empty arrays
#min length of line=40 to detect and draw a lines



# cv2.imshow('results',line_image)
# cv2.waitKey(0)

#Hough Transform
#to detect st lines in a images
#y=mx+b
#but b vs m
#called hough Transform in hough space
#to find lines from series of points
#bin with maximum number of votes
#line of bit fit
#vertical lines slope of infinity hough space mein problem
#more robust representation instead of cartesian we solve this porblem
#with polar coordinates system
#p=xcos(theta)+ysin(theta)
#sinusoidal curves
#number of intersection between curves more xtion points
#there is a single point that crosses all the points
#following parameters which would best fit the data
#line of best filter


#maximum number of xtion inside a bin
#line of best fit

#now to blend that image into our original img
