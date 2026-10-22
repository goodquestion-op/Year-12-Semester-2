from PIL import Image
import easyocr
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;


import pytesseract
import cv2
import os, sys, inspect #For dynamic filepaths
import numpy as np;



cam =  cv2.VideoCapture(0, cv2.CAP_V4L2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, 15)

reader = easyocr.Reader(['en'])
kernel = np.ones((2,2), np.uint8)

while True:
    

    check, frame = cam.read()



    

   
    img = cv2.resize(frame,(320,240))
    img_empty = np.zeros((img.shape[0], img.shape[1]))
    img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)
    greyscale = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img3 = cv2.adaptiveThreshold(greyscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5)  
    erode = cv2.erode(img3, kernel, iterations = 1)
    color = cv2.cvtColor(erode, cv2.COLOR_GRAY2BGR)

    hImg, wImg, _ = img.shape


    
    

  

    result = reader.readtext(color)

    # Output

    cv2.imshow("Original", img)
  
    cv2.imshow("Blurred",color)

    
    print("Blur:",color)
    


    

    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

cam.release()

cv2.destroyAllWindows()