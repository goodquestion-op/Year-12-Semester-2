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

kernel = np.ones((2,2), np.uint8)


while True:
    

    check, frame = cam.read()



    img = cv2.resize(frame,(320,240))

   
    img_empty = np.zeros((img.shape[0], img.shape[1]))
    img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)
    greyscale = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img3 = cv2.adaptiveThreshold(greyscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 5)
    dilate = cv2.erode(img3, kernel, iterations = 1)
    color = cv2.cvtColor(dilate, cv2.COLOR_GRAY2BGR) #to debug better
    
   # doesn't seem to help img4 = cv2.GaussianBlur(img3, (1, 1), 0)

    hImg, wImg, _ = img.shape

    boxes = pytesseract.image_to_boxes(img3)

    squares = img3

    # for b in boxes.splitlines():
    #     b = b.split(' ')
    #     print(b)
    #     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #     cv2.rectangle(squares, (x, hImg - y), (w, hImg - h), (50,50,255),1)
    #     cv2.putText(squares, b[0], (x,hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50,205,50), 1)

#checking org to debug 
    # orgB = pytesseract.image_to_boxes(img)

    # orgSquares = img

    # for b in orgB.splitlines():
    #         b = b.split(' ')
    #        # print(b)
    #         x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #         cv2.rectangle(orgSquares, (x, hImg - y), (w, hImg - h), (50,50,255),1)
    #         cv2.putText(orgSquares, b[0], (x,hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50,205,50), 1)

# testing dilate 
    dilateB = pytesseract.image_to_boxes(dilate)
    bestX = int(0)
    bestY = int(0)
    bestW = int(0)
    bestH = int(0)

    for b in dilateB.splitlines():
            b = b.split(' ')
        #     print(b)
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
                                #  top left       bottom right 
            cv2.rectangle(color, (x, hImg - y), (w, hImg - h), (50,50,255),1)
            
            cv2.putText(color, b[0], (x,hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50,205,50), 1)
            if bestX > x:
                  bestX = x
                #   print(bestX)
            if bestY < (hImg - y):
                    bestY = (hImg - y)
                    # print(bestY)
            if bestW < w:
                    bestW = w
                    # print(bestW)
            if bestH > (hImg - h):
                    bestH = (hImg - h)
                    # print(bestH)
    cv2.rectangle(color, (bestX, bestY), (bestW, bestH), (255,150,0),2)

    
    text4 = pytesseract.image_to_boxes(img3)
    text = pytesseract.image_to_boxes(img)
    debug = pytesseract.image_to_boxes(dilate)

    

    #debuging 
    #cv2.rectangle(color, (-5, hImg - 100), (315, hImg - 80), (0,255,255),2)



    # Output

    # cv2.imshow("Original", img)
    # cv2.imshow("Thresh", img3)
    # cv2.imshow("grey", greyscale)
    # cv2.imshow("dilate", dilate)
    cv2.imshow("color2", color)


    #print("Thresh:"+text4)
    #print("org:"+text)
    print("debug:"+debug)
    


    

    key = cv2.waitKey(1)

    if key == 27: # exit on ESC

        break

cam.release()

cv2.destroyAllWindows()