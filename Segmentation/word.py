import cv2
import numpy as np
from PIL import Image
import os, sys
path = "/home/hashrin/project/segmentation/word_input/"
dirs = (os.listdir( path ))
dirs=sorted(dirs,key=lambda x: int(os.path.splitext(x)[0]))
def seg():
    count=1
    for item in dirs:
        if os.path.isfile(path+item):
            image = cv2.imread(path+item)
            f, e = os.path.splitext(path+item)
            #print(image.shape[1])
            #grayscale
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            # cv2.imshow('gray',gray)
            # cv2.waitKey(0)

            #binary
            ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
            # cv2.imshow('second',thresh)
            # cv2.waitKey(0)

            # #dilation
            # kernel = np.ones((5,5), np.uint8)
            # img_dilation = cv2.dilate(thresh, kernel, iterations=1)
            # cv2.imshow('dilated',img_dilation)
            # cv2.waitKey(0)

            # #erosion
            # kernel = np.ones((5,5), np.uint8)
            # img_eroded = cv2.erode(img_dilation, kernel, iterations=1)
            # cv2.imshow('eroded',img_eroded)
            # cv2.waitKey(0)

            #closing
            kernel = np.ones((image.shape[0]//6,image.shape[1]//55), np.uint8)
            closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
            # cv2.imshow('closed',closing)
            # cv2.waitKey(0)

            #find contours
            im2,ctrs, hier = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            #sort contours
            sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

            for i, ctr in enumerate(sorted_ctrs):
                # Get bounding box
                x, y, w, h = cv2.boundingRect(ctr)

                # Getting ROI
                roi = image[y:y+h, x:x+w]

                # show ROI
                #cv2.imshow('segment no:'+str(i),roi)
                if(roi.shape[1]>image.shape[1]//50):
                    # if(image.shape[1]>1000):
                    #     cv2.namedWindow('segment no:'+str(i),cv2.WINDOW_NORMAL)
                    #     cv2.resizeWindow('segment no:'+str(i),(x//2,y//2))
                    # cv2.imshow('segment no:'+str(i),roi)
                    cv2.imwrite("/home/hashrin/project/segmentation/word_output/"+"00"+str(count)+".jpg",roi)
                    count=count+1
                    #cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
                    # cv2.waitKey(0)


            # cv2.imshow('marked areas',image)
            # cv2.waitKey(0)
seg()