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
    image = cv2.imread(path+'/'+inputfile,0)
    cv2.imshow('orig',image)
    cv2.waitKey(0)