import cv2
import os
import numpy as np
def segment():
    print("segmenting")
    #import image
    path=os.path.join(os.getcwd(),'working')
    # inputfile=os.listdir(path)[0]
    inputfile='processed.jpg'
    # print(inputfile)
    binary = cv2.imread(path+'/invbinary.jpg',0)
    image = cv2.imread(path+'/'+inputfile,0)
    cv2.imshow('orig',image)
    cv2.imshow('inverse binary',binary)
    cv2.waitKey(0)

    #closing
    print(image[1])
    return
    kernel = np.ones((3,image.shape[1]//8), np.uint8)
    closed=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel)

    #find contours
    im2,line_ctrs, hier = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #sort contours
    sorted_ctrs = sorted(line_ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])


    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)

        # Getting ROI
        roi = image[y:y+h, x:x+w]
        roi_binary=binary[y:y+h,x:x+w]
        mask=np.zeros_like(binary)
        cv2.drawContours(mask,[ctr],0, (255,255,255), -1)
        roi_mask=mask[y:y+h,x:x+w]
        roi_binary=cv2.bitwise_and(roi_binary,roi_mask)
        cv2.imshow('segment no:'+str(i),roi_binary)
        cv2.waitKey(0)