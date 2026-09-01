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
    img3 = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY)[1]
    img4 = cv2.GaussianBlur(img3, (1, 1), 0)

    hImg, wImg, _ = img.shape

    boxes = pytesseract.image_to_boxes(img4)

    for b in boxes.splitlines():
        b = b.split(' ')
        print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50,50,255),1)
        cv2.putText(img, b[0], (x,hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50,205,50), 1)

    
    text4 = pytesseract.image_to_boxes(img4)

  



    # Output

    cv2.imshow("Original", img)
  
    cv2.imshow("Blurred", img4)

    
    print("Blur:"+text4)
    


    

    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

cam.release()

cv2.destroyAllWindows()