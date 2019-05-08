import cv2
import os
import numpy as np
import shutil
def segment():
    print("Segmenting")
    #import image
    path=os.path.join(os.getcwd(),'working/')
    # inputfile=os.listdir(path)[0]
    inputfile='print.jpg'
    gray = cv2.imread(path+inputfile,0)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,line_binary = cv2.threshold(blur,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    line_binary=255-line_binary
    line_image=line_binary
    word_count=1
    

    #LINE SEGMENTATION



    line_kernel = np.ones((3,line_image.shape[1]//8), np.uint8)
    line_closed=cv2.morphologyEx(line_binary,cv2.MORPH_CLOSE,line_kernel)
    #cv2.imshow('closed',line_closed)
    #cv2.waitKey(0)
    #find line contours
    im_line,line_ctrs, line_hier = cv2.findContours(line_closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #sort line contours
    line_sorted_ctrs = sorted(line_ctrs, key=lambda line_ctr: cv2.boundingRect(line_ctr)[1])


    for line_i, line_ctr in enumerate(line_sorted_ctrs):
        # Get bounding box
        line_x, line_y, line_w, line_h = cv2.boundingRect(line_ctr)

        # Getting ROI
        line_roi = line_image[line_y:line_y+line_h, line_x:line_x+line_w]
        line_roi_binary=line_binary[line_y:line_y+line_h,line_x:line_x+line_w]
        line_mask=np.zeros_like(line_binary)
        cv2.drawContours(line_mask,[line_ctr],0, (255,255,255), -1)
        # cv2.imshow('final',line_mask)
        # cv2.waitKey(0)
        line_roi_mask=line_mask[line_y:line_y+line_h,line_x:line_x+line_w]
        line_roi_binary=cv2.bitwise_and(line_roi_binary,line_roi_mask)
        
        #show line
        # cv2.imshow('segment no:',line_roi_binary)
        # cv2.waitKey(0)



        #WORD SEGMENTATION
        

        
        word_kernel = np.ones((line_roi_binary.shape[0]//6,line_roi_binary.shape[1]//55), np.uint8)
        word_closed=cv2.morphologyEx(line_roi_binary,cv2.MORPH_CLOSE,word_kernel)
        
        #find word contours
        im_word, word_ctrs, word_hier = cv2.findContours(word_closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #sort word contours
        word_sorted_ctrs = sorted(word_ctrs, key=lambda word_ctr: cv2.boundingRect(word_ctr)[0])
        
        for word_i, word_ctr in enumerate(word_sorted_ctrs):
                
                # Get bounding box
                word_x, word_y, word_w, word_h = cv2.boundingRect(word_ctr)

                # Get ROI
                word_roi = line_roi_binary[word_y:word_y+word_h, word_x:word_x+word_w]

                #show word
                # cv2.imshow('segment no:',word_roi)
                # cv2.waitKey(0)


                if(word_roi.shape[1]>line_roi_binary.shape[1]//50):
                        
                        #make a directory for each word
                        os.mkdir(path+'word/'+str(word_count))
                        
                        #CHARACTER SEGMENTATION
                        
                        dest=os.path.join(path,'word/')
                        char_count=1
                        #find contours
                        char_im2,char_ctrs, char_hier = cv2.findContours(word_roi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                        #sort contours
                        char_sorted_ctrs = sorted(char_ctrs, key=lambda char_ctr: cv2.boundingRect(char_ctr)[0])

                        for char_i, char_ctr in enumerate(char_sorted_ctrs):
                                
                                # Get bounding box
                                char_x, char_y, char_w, char_h = cv2.boundingRect(char_ctr)

                                # Getting ROI
                                char_roi_thresh=word_roi[char_y:char_y+char_h,char_x:char_x+char_w]
                                char_mask=np.zeros_like(word_roi)
                                cv2.drawContours(char_mask,[char_ctr],0, (255,255,255), -1)
                                char_roi_mask=char_mask[char_y:char_y+char_h,char_x:char_x+char_w]
                                char_roi_thresh=cv2.bitwise_and(char_roi_thresh,char_roi_mask)
                                char_roi_thresh=255-char_roi_thresh

                                if(char_roi_thresh.shape[1]>word_roi.shape[1]//20):

                                        #PADDING AND RESIZING


                                        shape=char_roi_thresh.shape
                                        w=shape[1]
                                        h=shape[0]
                                        for i in range(0,4):
                                                base_size=h+20,w+20
                                                #make a 3 channel image for base which is slightly larger than target img
                                                base=np.zeros(base_size,dtype=np.uint8)
                                                cv2.rectangle(base,(0,0),(w+20,h+20),(255,255,255),30)#really thick white rectangle
                                                base[10:h+10,10:w+10]=char_roi_thresh
                                                char_roi_thresh=base
                                                h=h+20  
                                                w=w+20
                                        dim=(86,86)
                                        resized = cv2.resize(char_roi_thresh, dim, interpolation=cv2.INTER_CUBIC)



                                        cv2.imwrite(dest+str(word_count)+'/'+str(char_count)+".jpg",resized)
                                        char_count+=1
                        word_count+=1
# shutil.rmtree('working/word')
# os.mkdir('/home/hashrin/project/final/working/word') 