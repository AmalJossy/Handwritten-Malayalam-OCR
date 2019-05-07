import cv2
import numpy as np
from PIL import Image
import os, sys
path = "/home/hashrin/project/final/working/"
dirs = sorted(os.listdir( path ))
def seg():
    count=1
    for item in dirs:
        if os.path.isfile(path+item):
            image = cv2.imread(path+item)
            f, e = os.path.splitext(path+item)
            #cv2.imshow('orig',image)
            #cv2.waitKey(0)
            im=image.shape
            # print(im[1])
            #grayscale
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            # if(image.shape[0]>=1000 or image.shape[1] >=1000):
            #         cv2.namedWindow('gray',cv2.WINDOW_NORMAL)
            #         cv2.resizeWindow('gray',(im[1]//2,im[0]//2))
            # cv2.imshow('gray',gray)
            # cv2.waitKey(0)

            #binary_inverse
            ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            # if(image.shape[0]>=1000 or image.shape[1] >=1000):
            #         cv2.namedWindow('otsu',cv2.WINDOW_NORMAL)
            #         cv2.resizeWindow('otsu',(im[1]//2,im[0]//2))
            cv2.imshow('otsu',thresh)
            cv2.waitKey(0)
            thresh=255-thresh

            # if(image.shape[0]>=1000 or image.shape[1] >=1000):
            #         cv2.namedWindow('binary inverse',cv2.WINDOW_NORMAL)
            #         cv2.resizeWindow('binary inverse',(im[1]//2,im[0]//2))
            # cv2.imshow('binary inverse',thresh)
            # cv2.waitKey(0)
            # if(image.shape[0]>=1000 or image.shape[1] >=1000):
            #         cv2.namedWindow('second',cv2.WINDOW_NORMAL)
            #         cv2.resizeWindow('second',(im[1]//2,im[0]//2))
            # cv2.imshow('second',thresh)
            # cv2.waitKey(0)

            # #dilation
            # kernel = np.ones((5,im[1]*3//10), np.uint8)
            # img_dilation = cv2.dilate(thresh, kernel, iterations=1)
            # cv2.imshow('dilated',img_dilation)
            # cv2.waitKey(0)

            # #erosion
            # kernel = np.ones((5,im[1]*3//10), np.uint8)
            # img_erosion= cv2.erode(img_dilation, kernel, iterations=1)

            # cv2.imshow('eroded',img_erosion)
            # cv2.waitKey(0)

            #closing
            kernel = np.ones((3,im[1]//8), np.uint8)
            closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
            # if(image.shape[0]>=1000 or image.shape[1] >=1000):
            #         cv2.namedWindow('closed',cv2.WINDOW_NORMAL)
            #         cv2.resizeWindow('closed',(im[1]//2,im[0]//2))
            cv2.imshow('closed',closing)
            cv2.waitKey(0)

            #find contours
            im2,ctrs, hier = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            #sort contours
            sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])
            #sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.minAreaRect(ctr)[1])


            for i, ctr in enumerate(sorted_ctrs):
                    # Get bounding box
                    x, y, w, h = cv2.boundingRect(ctr)
                    # Getting ROI
                    roi = image[y:y+h, x:x+w]
                    roi_thresh=thresh[y:y+h,x:x+w]
                    mask=np.zeros_like(gray)
                    cv2.drawContours(mask,[ctr],0, (255,255,255), -1)
                    cv2.imshow('final',mask)
                    cv2.waitKey(0)
                    roi_mask=mask[y:y+h,x:x+w]
                    roi_thresh=cv2.bitwise_and(roi_thresh,roi_mask)
                    #roi_thresh=255-roi_thresh


                    # show ROI
                    if(roi.shape[1]>im[1]//15):
                            # if(image.shape[1]>1000):
                            #         cv2.namedWindow('segment no:'+str(i),cv2.WINDOW_NORMAL)
                            #         cv2.resizeWindow('segment no:'+str(i),(x//2,y//2))
                            cv2.imshow('segment no:'+str(i),roi_thresh)
                            cv2.imwrite("/home/hashrin/project/final/working/line/"+"00"+str(count)+".jpg",roi_thresh)
                            count=count+1
                            # cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
                            # cv2.waitKey(0)
                            # cv2.imshow('segment no:'+str(i),roi)
                            # cv2.imwrite("line/"+str(i)+".png",roi)
                            # cv2.waitKey(0)
            #cv2.imshow('marked areas',image)
            #cv2.waitKey(0)
seg()