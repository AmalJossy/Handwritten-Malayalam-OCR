import cv2
import os
import numpy as np

def preprocess():
    print('preprocessing')
    path=os.path.join(os.getcwd(),'working/')
    inputfile=sorted(os.listdir(path))
    inputfile=inputfile[0]
    image = cv2.imread(path+inputfile,0)
    # cv2.imshow('input',image)
    # cv2.waitKey(0)
    blur = cv2.GaussianBlur(image,(5,5),0)
    #ret3,th3 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret,th3 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)    
    kernel = np.ones((5,5),np.uint8) # try different  kernal size
    opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)
    mask=255-th3
    # denoised=255-(image * (mask.astype(image.dtype)))
    cv2.imwrite('working/invbinary.jpg',mask)
    cv2.imwrite('working/processed.jpg',th3)