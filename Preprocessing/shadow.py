import cv2
import numpy as np
img=cv2.imread("/home/hashrin/project/final/working/test.jpg",0)
rgb_planes=cv2.split(img)
result_planes=[]
result_norm_planes=[]
kernel = np.ones((7,7),np.uint8)
for plane in rgb_planes:
    dilated_img=cv2.dilate(plane,kernel)
    bg_img=cv2.medianBlur(dilated_img,21) #scratch text out
    diff_img=255-cv2.absdiff(plane,bg_img)
    norm_img=cv2.normalize(diff_img,diff_img,alpha=0,beta=255,norm_type=cv2.NORM_MINMAX,dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)
result=cv2.merge(result_norm_planes)
cv2.imwrite('result.jpg',result)

#  th=255-img

# mask=np.zeros_like(img)
# mask=255-mask
# diff=255-cv2.absdiff(img,mask)
# norm=cv2.normalize(diff,diff,alpha=0,beta=255,norm_type=cv2.NORM_MINMAX,dtype=cv2.CV_8UC1)
# cv2.imwrite('result1.jpg',norm)




