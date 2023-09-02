import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(3,3),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def roi(image):
    #number of destroyAllWindows
    height=image.shape[0]
    polygons=np.array([[(324,height),(977,height),(563,289)]])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)
    #masked karna
    masked_img=cv2.bitwise_and(image,mask)
    return masked_img

image=cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny=canny(lane_image)
cropped_image=roi(canny)
cv2.imshow('results',cropped_image)
cv2.waitKey(0)
#Region of intrest
#using matplotlib lib
#based on this will be using traingle to limit the region
#of intrest
# we are going to show only apsecific
#part of an image

#using binary numbers and bitwise_and
#binary to decimal conversion
#255------>11111111 8 bit byte
# ab ye canny image aur polygon ko ek saath represent
#karna hai toh BITWISE and
#polygon ka sirf 1111 baaki poora polygin image hai zero
#masking the entire region the corresponding regions
#of other array
#to mask our canny images


# Computing the bitwise & of both
# images as we saw earlier in the
# theory section, takes the bitwise
# & of each homologous pixel in
# both arrays, ultimately masking
# the canny image to only show the
# region of interest traced by the
# polygonal contour of the mask.
