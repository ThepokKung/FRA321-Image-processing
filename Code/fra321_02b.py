import numpy as np
import cv2

#Crate blank image 
img = np.zeros((512,512,3),np.uint8)

#Draw a diagolog blue line with thinkess of 5 px
cv2.line(img,(0,0),(500,511),(255,0,0),5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows