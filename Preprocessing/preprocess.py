import cv2
import os
import numpy as np
def preprocess():
    print("Denoising")
    #import image
    path=os.path.join(os.getcwd(),'working/input')
    inputfile=os.listdir(path)[0]
    image = cv2.imread(path+'/'+inputfile)
    # cv2.imshow('input',image)
    # cv2.waitKey(0)
    cv2.imwrite('working/processed.jpg',image)