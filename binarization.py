from PIL import Image
import pytesseract
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


while True:
    

    check, frame = cam.read()



    img = cv2.resize(frame,(320,240))

   
    img_empty = np.zeros((img.shape[0], img.shape[1]))
    img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)
    greyscale = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img3 = cv2.adaptiveThreshold(greyscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5)
   # doesn't seem to help img4 = cv2.GaussianBlur(img3, (1, 1), 0)

    hImg, wImg, _ = img.shape

    boxes = pytesseract.image_to_boxes(img3)

    squares = img3

    for b in boxes.splitlines():
        b = b.split(' ')
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(squares, (x, hImg - y), (w, hImg - h), (50,50,255),1)
        cv2.putText(squares, b[0], (x,hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50,205,50), 1)

#checking org to debug 
    orgB = pytesseract.image_to_boxes(img)

    orgSquares = img

    for b in orgB.splitlines():
            b = b.split(' ')
            print(b)
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(orgSquares, (x, hImg - y), (w, hImg - h), (50,50,255),1)
            cv2.putText(orgSquares, b[0], (x,hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50,205,50), 1)

    
    text4 = pytesseract.image_to_boxes(img3)
    text = pytesseract.image_to_boxes(img)
  



    # Output

    cv2.imshow("Original", img)
    cv2.imshow("Thresh", img3)
    cv2.imshow("grey", greyscale)

    print("Thresh:"+text4)
    print("org:"+text)
    


    

    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

cam.release()

cv2.destroyAllWindows()