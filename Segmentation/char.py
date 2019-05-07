import cv2
import numpy as np
from PIL import Image
import os, sys
path = "/home/hashrin/project/segmentation/word_output/"
dirs = sorted(os.listdir( path ))
print(dirs)
def seg():
    count=1
    for item in dirs:
        if os.path.isfile(path+item):
            image = cv2.imread(path+item)
            f, e = os.path.splitext(path+item)
            im=image.shape[1]

            #grayscale
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            # cv2.imshow('gray',gray)
            # cv2.waitKey(0)

            #im = cv2.resize(gray,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

            #binary
            ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
            # cv2.imshow('second',thresh)
            # cv2.waitKey(0)

            # #dilation
            # kernel = np.ones((5,5), np.uint8)
            # img_dilated = cv2.dilate(thresh, kernel, iterations=1)
            # cv2.imshow('dilated',img_dilated)
            # cv2.waitKey(0)

            # #erosion
            # kernel = np.ones((5,5), np.uint8)
            # img_eroded = cv2.erode(img_dilated, kernel, iterations=1)
            # cv2.imshow('eroded',img_eroded)
            # cv2.waitKey(0)

            #find contours
            im2, ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            #sort contours
            sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

            for i, ctr in enumerate(sorted_ctrs):
                
                # Get bounding box
                x, y, w, h = cv2.boundingRect(ctr)

                # Getting ROI
                roi = image[y:y+h, x:x+w]
                roi_thresh=thresh[y:y+h,x:x+w]
                mask=np.zeros_like(gray)
                cv2.drawContours(mask,[ctr],0, (255,255,255), -1)
                roi_mask=mask[y:y+h,x:x+w]
                roi_thresh=cv2.bitwise_and(roi_thresh,roi_mask)
                roi_thresh=255-roi_thresh

                # #erode
                # kernel = np.ones((5,5), np.uint8)
                # roi_thresh = cv2.erode(roi_thresh, kernel, iterations=1)
            

                if(roi_thresh.shape[1]>image.shape[1]//30):
                    # show ROI
                    # cv2.imshow('segment no:'+str(i),roi_thresh)

                    cv2.imwrite("/home/hashrin/project/segmentation/char_output/"+str(count)+".jpg",roi_thresh)
                    count=count+1
                    #cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
                    cv2.waitKey(0)

            # cv2.imshow('marked areas',image)
            # cv2.waitKey(0)
seg()