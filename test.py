from PIL import Image
import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;


import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;

#adjustible threshold slider for testing
def trackChanged(x):
    pass

cv2.namedWindow('Color Track Bar')
hh = 'Max'
h1 = 'Min'

wnd = 'Colobars'

cv2.createTrackbar("Max","Color Track Bar",0,255,trackChanged)
cv2.createTrackbar("Min","Color Track Bar",0,255,trackChanged)


cam =  cv2.VideoCapture(0)

while True:
    

    check, frame = cam.read()



    img = cv2.resize(frame,(320,240))

   
    img_empty = np.zeros((img.shape[0], img.shape[1]))
    img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)
    img3 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)[1]
    img4 = cv2.GaussianBlur(img3, (1, 1), 0)

    #more adjustible threshold slider for testing
    hu1 = cv2.getTrackbarPos("Max","Color Track Bar")
    hu2 = cv2.getTrackbarPos("min","Color Track Bar")

    ret, thresh1 = cv2.threshold(img2, hu1, hu2, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img2, hu1, hu2, cv2.THRESH_TOZERO)

    text1 = pytesseract.image_to_string(img)
    text2 = pytesseract.image_to_string(img2)
    text3 = pytesseract.image_to_string(img3)
    text4 = pytesseract.image_to_string(img4)

  



    # Output

    cv2.imshow("Original", img)
   # cv2.imshow("Normalized", img2)
   # cv2.imshow("Threshold", img3)
   # cv2.imshow("Blurred", img4)
  #  cv2.imshow("thresh 1", thresh1)
  #  cv2.imshow("thresh 2", thresh2)
    print("orgi:"+text1)
    print("norm:"+text2)
    print("thresh:"+text3)
    print("Blur:"+text4)
    


    

    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

cam.release()

cv2.destroyAllWindows()