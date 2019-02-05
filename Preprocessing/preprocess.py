import cv2
import os
import numpy as np

def preprocess():
    print("Denoising")
    #import image
    path=os.path.join(os.getcwd(),'working/input')
    inputfile=os.listdir(path)[0]
    image = cv2.imread(path+'/'+inputfile,0)
    cv2.imshow('input',image)
    cv2.waitKey(0)
    blur = cv2.GaussianBlur(image,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)    
    # kernel = np.ones((5,5),np.uint8) // try different  kernal size
    # opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)
    mask=255-th3
    denoised=255-(image * (mask.astype(image.dtype)))
    # cv2.imshow('denoise',denoised)
    # cv2.imshow('inverse binary',mask)
    # cv2.waitKey(0)
    cv2.imwrite('working/invbinary.jpg',mask)
    cv2.imwrite('working/processed.jpg',denoised)